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
