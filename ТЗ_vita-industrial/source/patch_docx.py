# -*- coding: utf-8 -*-
import os, json, re
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn

ROOT=os.path.dirname(os.path.abspath(__file__))
SRC=os.path.join(ROOT,'v2','new.docx')
OUT=os.path.join(ROOT,'out','TZ_vita-industrial_workshops.docx')
MEDIA=os.path.join(ROOT,'media')
doc=Document(SRC)

def set_text(par, text):
    runs=par.runs
    if not runs:
        par.add_run(text); return
    runs[0].text=text
    for r in runs[1:]: r.text=''

changed=[]
for par in doc.paragraphs:
    t=par.text
    if t.startswith('CTA-строки. После блоков'):
        set_text(par,'CTA-строки. После блоков 5, 12 и 16 размещается тёмная полоса с текстом и кнопкой '
                     '«Оставить заявку». Посетитель не должен пролистать больше двух экранов без кнопки обращения.')
        changed.append('CTA')
    elif t.startswith('Скрытые блоки.'):
        par._p.getparent().remove(par._p); changed.append('hidden-line removed')
    elif t.startswith('Макет показывает страницу'):
        set_text(par,'Макет показывает страницу /workshops сверху вниз: все 20 блоков, CTA-строки, шапку и футер сайта — '
                     'с заголовками и текстами из раздела 2, в цветах и шрифтах vita-industrial.ru. '
                     'Фотографии, планировки, карта и схема парка показаны заглушками: их берут из текущих материалов сайта.')
        changed.append('appendix intro')

# в тексте блока 2 ссылка на блок цен (был 13, стал 12)
for par in doc.paragraphs:
    if 'Смотреть цены и планировки' in par.text and 'блок 13' in par.text:
        set_text(par, par.text.replace('блок 13','блок 12')); changed.append('anchor 13->12')

# блок 11: убираем жаргон «пищёвка»
for tbl in doc.tables:
    for row in tbl.rows:
        c=row.cells[0]
        if 'пищёвка' in c.text:
            set_text(c.paragraphs[0], 'Пищевое производство')
            set_text(row.cells[1].paragraphs[0],
                'Газовое отопление, вода из скважины, зонирование под санитарные требования, '
                'отдельный вход для персонала и зона приёмки сырья. Подходит и для контрактного '
                'производства продуктов питания.')
            changed.append('block 11 wording')

# легенда: убираем строку про скрытые блоки
legend=doc.tables[-1]
for row in list(legend.rows):
    if row.cells[0].text.strip().startswith('Серая'):
        row._tr.getparent().remove(row._tr); changed.append('legend row removed')

# ================= правки по бизнес-модели: аренды нет, только продажа =================
def tbl_by_header(*cells):
    for t in doc.tables:
        head=[c.text.strip() for c in t.rows[0].cells]
        if all(any(x==h for h in head) for x in cells): return t
    return None

def del_column(tbl, idx):
    for row in tbl.rows:
        tcs=row._tr.findall(qn('w:tc'))
        if idx < len(tcs): row._tr.remove(tcs[idx])
    grid=tbl._tbl.find(qn('w:tblGrid'))
    if grid is not None:
        gcs=grid.findall(qn('w:gridCol'))
        if idx < len(gcs):
            w=int(gcs[idx].get(qn('w:w')) or 0); grid.remove(gcs[idx])
            rest=grid.findall(qn('w:gridCol'))
            if rest:
                add=w//len(rest)
                for gc in rest: gc.set(qn('w:w'), str(int(gc.get(qn('w:w')) or 0)+add))
    # ширины ячеек подтягиваем под новый грид
    grid=tbl._tbl.find(qn('w:tblGrid'))
    widths=[int(gc.get(qn('w:w')) or 0) for gc in grid.findall(qn('w:gridCol'))] if grid is not None else []
    for row in tbl.rows:
        for i,tc in enumerate(row._tr.findall(qn('w:tc'))):
            if i < len(widths):
                tcW=tc.find(qn('w:tcPr')).find(qn('w:tcW'))
                if tcW is not None: tcW.set(qn('w:w'), str(widths[i]))

def del_row(tbl, first_cell_starts):
    for row in list(tbl.rows):
        if row.cells[0].text.strip().startswith(first_cell_starts):
            row._tr.getparent().remove(row._tr); return True
    return False

def set_cell(tbl, r, c, text):
    set_text(tbl.rows[r].cells[c].paragraphs[0], text)

# каталог (блок 5) и прайс (блок 12): убираем колонку «Аренда»
for t in doc.tables:
    head=[c.text.strip() for c in t.rows[0].cells]
    if 'Аренда' in head and ('Покупка' in head or 'Стоимость покупки' in head):
        del_column(t, head.index('Аренда')); changed.append('колонка «Аренда» убрана')

# каталог: колонку «Покупка» приводим к виду «цена за м² · стоимость блока»
cat=tbl_by_header('Карточка (H3)','Текст карточки')
if cat is not None:
    head=[c.text.strip() for c in cat.rows[0].cells]
    if 'Покупка' in head:
        ci=head.index('Покупка')
        set_text(cat.rows[0].cells[ci].paragraphs[0],'Стоимость покупки')
        TOTALS={'500':'от 53,7 млн ₽','750':'от 76,3 млн ₽','1000':'от 100,3 млн ₽','1500':'от 152,5 млн ₽'}
        for row in cat.rows[1:]:
            for k,v in TOTALS.items():
                if row.cells[0].text.strip().endswith(k+' м²'):
                    set_text(row.cells[ci].paragraphs[0], '105 000 ₽/м²  ·  '+v)
        changed.append('каталог: стоимость блока в карточке')

# условия оплаты: «Аренда с правом выкупа» → «Бронирование»
pay=tbl_by_header('Вариант','Условия')
if pay is not None:
    for row in pay.rows:
        if row.cells[0].text.strip().startswith('Аренда с правом выкупа'):
            set_text(row.cells[0].paragraphs[0],'Бронирование')
            set_text(row.cells[1].paragraphs[0],
                     'Выбранный блок бронируется на 5 рабочих дней, пока готовятся документы. Бронь бесплатная.')
            changed.append('условия оплаты: аренда с выкупом → бронирование')

# блок 13: сравнение с рыночной арендой, без своей ставки
cmp_t=tbl_by_header('Параметр','Покупка блока в парке')
if cmp_t is not None:
    set_cell(cmp_t,0,2,'Аренда цеха на рынке')
    for row in cmp_t.rows:
        k=row.cells[0].text.strip()
        if k=='Платёж':
            set_text(row.cells[2].paragraphs[0],
                     'Ставка по рынку [уточнить] ₽/м² в месяц бессрочно, с ежегодной индексацией')
        elif k.startswith('Окупаемость'):
            set_text(row.cells[1].paragraphs[0],
                     'Цена за м² ÷ (рыночная ставка аренды × 12 месяцев): ориентировочно 10–12 лет, '
                     'без учёта роста стоимости объекта')
    changed.append('блок 13 переведён на рыночную аренду')

# точечные замены в абзацах
PARA_REPL=[
 ('Покупка от 105 000 ₽ за м² · Аренда от 800 ₽ за м² в месяц',
  'Покупка от 105 000 ₽ за м² · блок 500 м² — от 53,7 млн ₽'),
 ('Аренда - 800 ₽ за м² в месяц, коммунальные платежи по счётчикам.',
  'Помещения парка продаются, аренда не предлагается: блок сразу оформляется в собственность покупателя.'),
 ('Аренда — 800 ₽ за м² в месяц, коммунальные платежи по счётчикам.',
  'Помещения парка продаются, аренда не предлагается: блок сразу оформляется в собственность покупателя.'),
 ('рассчитает условия покупки или аренды.', 'рассчитает стоимость и график платежей.'),
 ('в кредит или лизинг; есть вариант аренды с последующим выкупом.',
  'в кредит или лизинг. Аренда в парке не предлагается: блок сразу оформляется в собственность.'),
]
for par in doc.paragraphs:
    for a,b in PARA_REPL:
        if a in par.text:
            set_text(par, par.text.replace(a,b)); changed.append('текст: '+a[:34])
    if par.text.startswith('Если производство уже работает стабильно'):
        set_text(par,'Индустриальный парк «Вита» помещения только продаёт. Блок сравнивает покупку с арендой цеха на стороне: '
                     'если производство уже работает стабильно и оборудование привязано к площадке, покупка почти всегда '
                     'выгоднее — арендная ставка индексируется каждый год, а платёж за собственный цех заканчивается.')
        changed.append('вывод блока 13')
    if par.text.startswith('Расчёт окупаемости:'):
        set_text(par,'Перед публикацией подставить актуальную рыночную ставку аренды производственных помещений в Шушарах '
                     'и пересчитать окупаемость по формуле: цена за м² ÷ (ставка × 12).')
        changed.append('примечание об окупаемости')

# FAQ
for t in doc.tables:
    if t.rows[0].cells[0].text.strip()!='Вопрос': continue
    for row in t.rows:
        a=row.cells[1]
        if 'покупка окупается примерно за 11 лет при текущей арендной ставке' in a.text:
            set_text(a.paragraphs[0],
              'Помещения в парке только продаются. Если производство работает стабильно и оборудование привязано '
              'к площадке, покупка окупается примерно за 10–12 лет по сравнению с рыночной арендой цеха — и дальше '
              'вы платите только за эксплуатацию. Аренда на стороне подходит новому или сезонному проекту, которому важна гибкость.')
            changed.append('FAQ: покупка или аренда')
        elif 'именно под арендный бизнес при текущей ставке' in a.text:
            set_text(a.paragraphs[0],
              'Да. Помещение оформлено как самостоятельный объект, поэтому его можно сдавать, закладывать и продавать '
              'по своему решению. Часть покупателей берёт блок именно под арендный бизнес.')
            changed.append('FAQ: сдавать в аренду')

# блок 8: возвращаем левую колонку «О наших цехах» (текст + кнопка)
for i,par in enumerate(doc.paragraphs):
    if par.text.strip()=='H2: Что входит в цену производственного помещения':
        newp=par.insert_paragraph_before(
            'Надзаголовок блока: «О наших цехах». Вёрстка как сейчас на сайте: слева заголовок, текст и кнопка '
            '«Получить консультацию», справа аккордеон. Текст слева: «Мы продаём не просто коробку, а готовую '
            'инфраструктуру: инженерные сети, документы и управление территорией уже включены в цену квадратного '
            'метра. Ниже — что именно вы получаете вместе с блоком».')
        par._p.addnext(newp._p)
        changed.append('блок 8: левая колонка описана')
        break

# --- удаляем всё после таблицы-легенды (старые рисунки и подписи)
body=doc.element.body
last_tbl=legend._tbl
seen=False; removed=0
for el in list(body):
    if el is last_tbl: seen=True; continue
    if seen and el.tag in (qn('w:p'), qn('w:tbl')):
        body.remove(el); removed+=1
changed.append(f'old figures removed: {removed}')

# --- новые рисунки
CAP=dict(size=Pt(8.5), color=RGBColor.from_string('555555'))
def pic(fname, caption, width=17.0):
    p=doc.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before=Pt(8); p.paragraph_format.space_after=Pt(2)
    p.add_run().add_picture(os.path.join(MEDIA,fname), width=Cm(width))
    c=doc.add_paragraph(); c.alignment=WD_ALIGN_PARAGRAPH.CENTER
    c.paragraph_format.space_after=Pt(12)
    r=c.add_run(caption); r.italic=True; r.font.size=CAP['size']; r.font.color.rgb=CAP['color']

N=[0]
def fig(fname, text, width=17.0):
    N[0]+=1; pic(fname, f'Рис. {N[0]}. {text}', width)

fig('fig_overview.jpg','Общий вид страницы: читать сверху вниз, колонки 1, 2, 3')
fig('fig_mobile.jpg','Первый экран на мобильном (390 px): H1, подзаголовок, цена и кнопка заявки видны без прокрутки', width=7.2)

parts=json.load(open(os.path.join(ROOT,'parts.json')))
def short(lbls):
    out=[]
    for l in lbls:
        l=l.strip()
        if l.startswith('CTA'): out.append('CTA-строка')
        else:
            t=l.replace('Блок ','').split(' · ')
            out.append(f'{t[0]} — {t[1]}' if len(t)>1 else t[0])
    return '; '.join(out)
for i,pt in enumerate(parts,1):
    fig(f'fig_part{i:02d}.jpg', f'Макет страницы, часть {i} из {len(parts)}: {short(pt["labels"])}')

os.makedirs(os.path.dirname(OUT),exist_ok=True)
doc.save(OUT)
print('\n'.join(changed))
print('figures added:', N[0])
print('saved', OUT, os.path.getsize(OUT)//1024,'KB')
