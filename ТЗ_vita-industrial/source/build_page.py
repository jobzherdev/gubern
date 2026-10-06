# -*- coding: utf-8 -*-
"""Страница /workshops одним блоком T123 — на CSS и приёмах готовой страницы /warehouses."""
import sys, os, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import content as C

e = html.escape
B = {b['n']: b for b in C.BLOCKS}
HERE = os.path.dirname(os.path.abspath(__file__))
CSS = open(os.path.join(HERE, 'ref_css.txt'), encoding='utf8').read().strip()

I = dict(
    hero="https://static.tildacdn.com/tild6635-3766-4431-b032-653035343361/blob.webp",
    heroMob="https://static.tildacdn.com/tild3163-3132-4263-b837-386431373236/blob.webp",
    facade="https://static.tildacdn.com/tild3163-3132-4263-b837-386431373236/blob.webp",
    truck="https://static.tildacdn.com/tild3362-3064-4662-b561-333738353733/photo_2026-08-30_18-.jpg",
    gates="https://static.tildacdn.com/tild3766-6535-4239-a139-336364316338/blob.webp",
    aerial="https://static.tildacdn.com/tild3865-6265-4234-a461-636531353731/blob.webp",
    genplan="https://static.tildacdn.com/tild3338-6139-4135-b438-653263313631/0020_1.jpg",
    p500="https://static.tildacdn.com/tild3465-3637-4735-b261-393234383766/blob.webp",
    p750="https://static.tildacdn.com/tild3331-3333-4230-b763-376338653061/image_20.png",
    p1000="https://static.tildacdn.com/tild6563-6539-4033-b830-636564636430/image_21.png",
    p1500="https://static.tildacdn.com/tild6539-3836-4432-b139-663131373538/image_22.png",
    c2000="https://static.tildacdn.com/tild3161-6233-4933-b935-326363313134/Frame_892.png",
    c3000="https://static.tildacdn.com/tild3565-3738-4761-b965-656633383531/Frame_893.png",
    c7000="https://static.tildacdn.com/tild6137-6239-4666-a633-653466353432/Frame_894.png",
    c10000="https://static.tildacdn.com/tild3464-3961-4631-b465-656332383533/Frame_895.png",
)
POP = "#zeropopup"
PLANS = [
    ("500",  "436,11 м²", "75,65 м²",  "511,75 м²",  "15 × 32 м", "от 53,7 млн ₽",  I['p500'],
     "Подходит под небольшое сборочное или пищевое производство, мастерскую, участок с ЧПУ."),
    ("750",  "637,56 м²", "89,15 м²",  "726,72 м²",  "18 × 38 м", "от 76,3 млн ₽",  I['p750'],
     "Самый востребованный формат: производственная линия, зона упаковки и склад в одном блоке."),
    ("1000", "836,02 м²", "118,92 м²", "954,94 м²",  "24 × 38 м", "от 100,3 млн ₽", I['p1000'],
     "Место под станочный парк, кран-балку и отдельную зону контроля качества."),
    ("1500", "1274,09 м²","178,56 м²", "1452,65 м²", "36 × 38 м", "от 152,5 млн ₽", I['p1500'],
     "Полноценное производство с участком отгрузки и складом на одной площадке."),
]

O=[]; A=O.append
A("""<!-- /workshops: всё наполнение страницы одним блоком T123. Собрано по ТЗ.
     Оформление и приёмы — как на странице /warehouses.
     Все кнопки заявки открывают окно #zeropopup (форма «Закажите обратный звонок»), оно уже есть на странице. -->""")
A("<style>\n"+CSS+"""
.vi-stats>div b{display:block;margin-bottom:4px;line-height:1.1}
.vi-stats>div span{display:block;line-height:1.35}
.vi-geo td:first-child{width:46%}
@media screen and (max-width:960px){.vi-geo{min-width:0}.vi-geo td,.vi-geo th{padding:10px 12px;font-size:14px}}
.vi-map .vi-btn{position:relative;z-index:1}
"""+"\n</style>")

# ---------- первый экран ----------
h=B[2]['data']
A(f"""
<div class="vi-top">
<picture>
  <source media="(max-width:640px)" srcset="{I['heroMob']}">
  <img src="{I['hero']}" alt="Производственные цеха индустриального парка «Вита» в Шушарах: корпуса с секционными воротами и зоной разгрузки" fetchpriority="high">
</picture>
<div class="vi-hero">
  <div class="vi">
    <div class="vi-crumbs" style="color:#cfd8e3;padding-top:0"><a href="/" style="color:#cfd8e3">Главная</a> / <span>Производственные помещения</span></div>
    <h1>{e(h['h1'])}</h1>
    <p>{e(h['sub'])}</p>
    <div class="vi-price">{e(h['price'])}</div>
    <div class="vi-cta-btns">
      <a href="{POP}" class="vi-btn vi-btn--white">{e(h['btns'][0])}</a>
      <a href="#prices" class="vi-btn vi-btn--ghost" style="color:#fff!important;border-color:rgba(255,255,255,.7)">{e(h['btns'][1])}</a>
    </div>
    <div class="vi-pills">
      <div class="vi-pill"><b>36 зданий</b><span>в парке, свободные блоки 500–1500 м²</span></div>
      <div class="vi-pill"><b>8 м</b><span>высота до низа конструкций, пол 5 т/м²</span></div>
      <div class="vi-pill"><b>Газ, 25 кВт</b><span>вода и септик заведены в каждый блок</span></div>
      <div class="vi-pill"><b>7–14 дней</b><span>регистрация права в Росреестре</span></div>
    </div>
  </div>
</div>
</div>""")

# ---------- об объекте + цифры ----------
d4=B[4]['data']
A(f"""
<div class="vi-sect">
  <div class="vi">
    <div class="vi-eyebrow">О парке</div>
    <h2>{e(B[4]['head'])}</h2>""")
for p in d4['paras']: A(f'    <p>{e(p)}</p>')
A('    <div class="vi-stats vi-grid-3" style="margin-top:24px">')
for num,txt in B[3]['data']:
    A(f'      <div><b>{e(num)}</b><span>{e(txt)}</span></div>')
A("""    </div>
  </div>
</div>""")

# ---------- что входит в цену ----------
ld=B[8].get('lead',{})
A(f"""
<div class="vi-sect">
  <div class="vi">
    <div class="vi-eyebrow">{e(ld.get('eyebrow','О наших цехах'))}</div>
    <h2>{e(B[8]['head'])}</h2>
    <p>{e(ld.get('text',''))}</p>
    <div class="vi-grid-3" style="margin-top:20px">""")
for t,x in B[8]['data']:
    A(f'      <div class="vi-card"><span class="vi-ttl">{e(t)}</span><p>{e(x)}</p></div>')
A(f"""    </div>
    <p style="margin-top:20px"><a href="{POP}" class="vi-btn">{e(ld.get('btn','Получить консультацию'))}</a></p>
  </div>
</div>""")

# ---------- планировки и цены (табы) ----------
c5=B[5]['data']
A(f"""
<div class="vi-sect" id="prices">
  <div class="vi">
    <div class="vi-eyebrow">Планировки и цены</div>
    <h2>Планировки и цены: производственные помещения 500, 750, 1000 и 1500 м²</h2>
    <div class="vi-scroll"><table class="vi-table">
      <tr><th>Блок</th><th>Цех, 1 этаж</th><th>Офис, 2 этаж</th><th>Суммарно</th><th>Габариты</th><th>Цена объекта</th></tr>""")
for a_,ceh,off,tot,gab,price,_,_ in PLANS:
    A(f'      <tr><td>{a_} м²</td><td>{ceh}</td><td>{off}</td><td>{tot}</td><td>{gab}</td><td><b>{price}</b></td></tr>')
A(f"""    </table></div>
    <p style="margin-top:16px">{e(c5['lead'])}</p>
    <p>Цена рассчитывается от суммарной площади помещения вместе с офисно-бытовой частью. Стоимость конкретного блока и порядок оплаты менеджер проекта подтверждает при обращении.</p>
    <div class="vi-tabs">
      <input type="radio" name="vi-plan" id="vi-t500" checked><input type="radio" name="vi-plan" id="vi-t750"><input type="radio" name="vi-plan" id="vi-t1000"><input type="radio" name="vi-plan" id="vi-t1500"><input type="radio" name="vi-plan" id="vi-tcombo">
      <div class="vi-tablabels">
        <label for="vi-t500">500 м²</label><label for="vi-t750">750 м²</label><label for="vi-t1000">1000 м²</label><label for="vi-t1500">1500 м²</label><label for="vi-tcombo">2000–10 000 м²</label>
      </div>
      <div class="vi-panels">""")
for a_,ceh,off,tot,gab,price,img,note in PLANS:
    A(f"""      <div class="vi-panel vi-p{a_}">
        <div>
          <h3>Производственный цех {a_} м² с офисом-мезонином {off.replace(' м²','')} м²</h3>
          <table class="vi-table">
            <tr><td>Цех, 1 этаж</td><td>{ceh}</td></tr>
            <tr><td>Офис, 2 этаж</td><td>{off}</td></tr>
            <tr><td>Суммарная площадь</td><td>{tot}</td></tr>
            <tr><td>Габариты в осях</td><td>{gab}</td></tr>
            <tr><td><b>Цена объекта</b></td><td><b>{price}</b></td></tr>
          </table>
          <p style="font-size:14.5px">{e(note)}</p>
          <ul><li>Возможность установки кран-балки грузоподъёмностью до 5 т</li><li>Технические изменения объекта под ваш запрос</li></ul>
          <a href="{POP}" class="vi-btn">Рассчитать стоимость</a>
          <a href="#genplan-map" class="vi-btn vi-btn--ghost">Смотреть генплан</a>
        </div>
        <img src="{img}" alt="План производственного помещения {a_} м²: цех {ceh} на первом этаже, офис-мезонин {off} на втором" loading="lazy">
      </div>""")
A(f"""      <div class="vi-panel vi-pcombo">
        <div>
          <h3>Комплексные решения 2000–10 000 м²</h3>
          <p style="font-size:14.5px">{e(c5['note'])}</p>
          <ul><li>Объединяем смежные блоки в один контур с общей зоной отгрузки</li><li>Изменения вносим в проект до начала отделки</li></ul>
          <a href="{POP}" class="vi-btn">Обсудить проект</a>
        </div>
        <div class="vi-combo">
          <figure><img src="{I['c2000']}" alt="Схема комплексного производственного решения 2000 м²" loading="lazy"><figcaption>2000 м²</figcaption></figure>
          <figure><img src="{I['c3000']}" alt="Схема комплексного производственного решения 3000 м²" loading="lazy"><figcaption>3000 м²</figcaption></figure>
          <figure><img src="{I['c7000']}" alt="Схема комплексного производственного решения 7000 м²" loading="lazy"><figcaption>7000 м²</figcaption></figure>
          <figure><img src="{I['c10000']}" alt="Схема комплексного производственного решения 10 000 м²" loading="lazy"><figcaption>10 000 м²</figcaption></figure>
        </div>
      </div>
      </div>
    </div>
  </div>
</div>""")

def cta(text, btn="Оставить заявку"):
    A(f"""
<div class="vi-cta">
  <div class="vi"><span class="vi-ttl">{e(text)}</span>
    <span class="vi-cta-btns"><a href="{POP}" class="vi-btn vi-btn--white">{e(btn)}</a></span></div>
</div>""")
cta(C.CTA_AFTER[5])

# ---------- технические характеристики ----------
A(f"""
<div class="vi-sect" id="characteristics">
  <div class="vi">
    <div class="vi-eyebrow">Характеристики</div>
    <h2>{e(B[6]['head'])}</h2>
    <div class="vi-scroll"><table class="vi-table">
      <tr><th style="width:34%">Параметр</th><th>Значение</th></tr>""")
for k,v in B[6]['data']: A(f'      <tr><td>{e(k)}</td><td>{e(v)}</td></tr>')
A("""    </table></div>
  </div>
</div>""")

# ---------- генплан ----------
A(f"""
<div class="vi-sect" id="genplan-map">
  <div class="vi">
    <div class="vi-eyebrow">Генеральный план</div>
    <h2>{e(B[7]['head'])}</h2>
    <img src="{I['genplan']}" alt="Генеральный план индустриального парка «Вита» в Шушарах: 36 зданий, внутренние проезды и выезд на Московское шоссе" loading="lazy" style="width:100%;height:auto;display:block;border:1px solid #dfe5ec">
    <p class="vi-note">На схеме — 36 зданий парка с внутренними проездами и зонами разгрузки. Свободные производственные помещения и их площади менеджер показывает на актуальной версии плана: статус свободных блоков обновляется еженедельно.</p>
    <p><a href="{POP}" class="vi-btn">Узнать свободные помещения</a></p>
  </div>
</div>""")

# ---------- локация ----------
loc=B[9]['data']
GEO=[("КАД","6 км"),("Московское шоссе","прямой выезд"),
     ("Трассы М-10 и М-11","рядом: Москва, Великий Новгород, юг региона"),
     ("Железнодорожная станция Шушары","рядом"),
     ("Аэропорт Пулково","20 минут, южное направление"),
     ("Граница Тосненского района Ленобласти","10 минут")]
MAPURL="https://yandex.ru/maps/?pt=30.432597,59.772195&z=14&l=map"
A(f"""
<div class="vi-sect" id="location">
  <div class="vi">
    <div class="vi-eyebrow">Локация</div>
    <h2>{e(B[9]['head'])}</h2>""")
for p in loc['paras']: A(f'    <p>{e(p)}</p>')
A(f"""    <div class="vi-grid-2" style="margin-top:20px">
      <div class="vi-map" style="display:flex;align-items:center;justify-content:center">
        <iframe src="https://yandex.ru/map-widget/v1/?ll=30.432597%2C59.772195&amp;z=13&amp;pt=30.432597%2C59.772195%2Cpm2rdm" loading="lazy" allowfullscreen title="Индустриальный парк «Вита» на карте: Санкт-Петербург, Пушкинский район, Шушары"></iframe>
        <a href="{MAPURL}" target="_blank" rel="noopener" class="vi-btn">Показать на карте</a>
      </div>
      <div>
        <table class="vi-table vi-geo">
          <tr><th>Точка</th><th>Как связан объект</th></tr>""")
for a_,b_ in GEO: A(f'          <tr><td>{e(a_)}</td><td>{e(b_)}</td></tr>')
A(f"""        </table>
        <p class="vi-note">Координаты объекта: 59.772195, 30.432597. <a href="{MAPURL}" target="_blank" rel="noopener">Построить маршрут</a></p>
      </div>
    </div>
  </div>
</div>""")

# ---------- фотографии ----------
A(f"""
<div class="vi-sect">
  <div class="vi">
    <div class="vi-eyebrow">Фотографии</div>
    <h2>{e(B[10]['head'])}</h2>
    <div class="vi-grid-4">
      <img src="{I['facade']}" alt="Производственные помещения парка «Вита», Шушары — фасад корпуса с секционными воротами" loading="lazy" style="width:100%;height:220px;object-fit:cover;display:block">
      <img src="{I['gates']}" alt="Производственный корпус индустриального парка «Вита» — ворота и зона разгрузки у цеха" loading="lazy" style="width:100%;height:220px;object-fit:cover;display:block">
      <img src="{I['aerial']}" alt="Индустриальный парк «Вита» в Шушарах с высоты: корпуса, проезды и парковка" loading="lazy" style="width:100%;height:220px;object-fit:cover;display:block">
      <img src="{I['truck']}" alt="Производственное помещение парка «Вита» — подъезд фуры к воротам цеха" loading="lazy" style="width:100%;height:220px;object-fit:cover;display:block">
    </div>
    <p class="vi-note">Строительство идёт очередями. Актуальные фотографии — в разделе <a href="/progress">«Ход строительства»</a>.</p>
  </div>
</div>""")

# ---------- применение ----------
A(f"""
<div class="vi-sect">
  <div class="vi">
    <div class="vi-eyebrow">Применение</div>
    <h2>{e(B[11]['head'])}</h2>
    <div class="vi-grid-3">""")
for t,x in B[11]['data']:
    A(f'      <div class="vi-card"><span class="vi-ttl">{e(t)}</span><p>{e(x)}</p></div>')
A("""    </div>
  </div>
</div>""")

# ---------- цены и условия ----------
pr=B[12]['data']
A(f"""
<div class="vi-sect">
  <div class="vi">
    <div class="vi-eyebrow">Цены</div>
    <h2>{e(B[12]['head'])}</h2>""")
for p in pr['paras']: A(f'    <p>{e(p)}</p>')
A('    <h3>Условия оплаты</h3>\n    <div class="vi-grid-4">')
for t,x in pr['terms']:
    A(f'      <div class="vi-card"><span class="vi-ttl">{e(t)}</span><p>{e(x)}</p></div>')
A("""    </div>
  </div>
</div>""")
cta(C.CTA_AFTER[12])

# ---------- покупка или аренда ----------
cm=B[13]['data']
A(f"""
<div class="vi-sect">
  <div class="vi">
    <div class="vi-eyebrow">Покупка или аренда</div>
    <h2>{e(B[13]['head'])}</h2>
    <div class="vi-scroll"><table class="vi-table">
      <tr>"""+''.join(f'<th>{e(x)}</th>' for x in cm['header'])+"</tr>")
for r in cm['rows']: A('      <tr>'+''.join(f'<td>{e(c)}</td>' for c in r)+'</tr>')
A(f"""    </table></div>
    <p style="margin-top:14px">{e(cm['after'])}</p>
  </div>
</div>""")

# ---------- новый или вторичка ----------
A(f"""
<div class="vi-sect">
  <div class="vi">
    <div class="vi-eyebrow">Сравнение</div>
    <h2>{e(B[14]['head'])}</h2>
    <div class="vi-grid-3">""")
for t,x in B[14]['data']:
    A(f'      <div class="vi-card"><span class="vi-ttl">{e(t)}</span><p>{e(x)}</p></div>')
A("""    </div>
  </div>
</div>""")

# ---------- этапы ----------
R=['1 день','в любой будний день','5 рабочих дней','по готовности документов','7–14 рабочих дней','передача по акту']
A(f"""
<div class="vi-sect">
  <div class="vi">
    <div class="vi-eyebrow">Сделка</div>
    <h2>{e(B[15]['head'])}</h2>
    <ul class="vi-steps">""")
for i,((t,x),r) in enumerate(zip(B[15]['data'],R),1):
    A(f'      <li><span class="n">{i}</span><div><b>{e(t)}</b><p>{e(x)}</p></div><span class="r">{e(r)}</span></li>')
A("""    </ul>
    <p class="vi-note">Средний срок от первого звонка до получения ключей — около трёх недель. Менеджер: <a href="tel:+78125744747">+7 (812) 574-47-47</a>.</p>
  </div>
</div>""")

# ---------- документы ----------
A(f"""
<div class="vi-sect">
  <div class="vi">
    <div class="vi-eyebrow">Документы</div>
    <h2>{e(B[16]['head'])}</h2>
    <ul style="margin:0;padding-left:18px">""")
for x in B[16]['data']: A(f'      <li style="margin-bottom:10px">{e(x)}</li>')
A(f"""    </ul>
    <p style="margin-top:18px">Полный пакет — в разделе <a href="/documentation">«Документация»</a>.</p>
    <p><a href="{POP}" class="vi-btn">Запросить документы</a></p>
  </div>
</div>""")
cta(C.CTA_AFTER[16])

# ---------- FAQ ----------
A(f"""
<div class="vi-sect">
  <div class="vi">
    <div class="vi-eyebrow">Вопросы и ответы</div>
    <h2>{e(B[17]['head'])}</h2>""")
for i,(q,a) in enumerate(B[17]['data']):
    op=' open' if i<3 else ''
    A(f"""    <details class="vi-q"{op}>
      <summary>{e(q)}</summary>
      <div class="vi-a"><p>{e(a)}</p></div>
    </details>""")
A("""  </div>
</div>""")

# ---------- заявка ----------
f18=B[18]['data']
A(f"""
<div class="vi-sect" id="contacts">
  <div class="vi">
    <div class="vi-eyebrow">Контакты</div>
    <h2>{e(B[18]['head'])}</h2>
    <div class="vi-grid-2">
      <div>
        <p>{e(f18['text'])}</p>
        <div class="vi-cta-btns" style="margin:14px 0">
          <a href="{POP}" class="vi-btn">Оставить заявку</a>
          <a href="tel:+78125744747" class="vi-btn vi-btn--ghost">+7 (812) 574-47-47</a>
        </div>
        <p class="vi-note">Почта: <a href="mailto:info@isk-vita.ru">info@isk-vita.ru</a>. Объект: Санкт-Петербург, Пушкинский район, Шушары, выезд на Московское шоссе. Офис: площадь Конституции, д. 3а, БЦ «Пирамида», офис 901–914.</p>
      </div>
      <div><img src="{I['aerial']}" alt="Индустриальный парк «Вита» в Шушарах — вид на корпуса и территорию" loading="lazy" style="width:100%;height:100%;object-fit:cover;display:block;max-height:320px"></div>
    </div>
  </div>
</div>""")

# ---------- текст низа ----------
t19=B[19]['data']
A(f"""
<div class="vi-sect">
  <div class="vi">
    <div class="vi-eyebrow">Коротко о главном</div>
    <h2>{e(B[19]['head'])}</h2>""")
for p in t19['paras']: A(f'    <p>{e(p)}</p>')
A('    <h3>Другие разделы по объекту</h3>\n    <div class="vi-links">')
for t,u in t19['links']:
    A(f'      <a href="{u}">{e(t)}<small>{u}</small></a>')
A("""    </div>
  </div>
</div>""")

out=os.path.join(os.path.dirname(HERE),'deliver2','workshops_одним_блоком_T123.html')
open(out,'w',encoding='utf8').write('\n'.join(O))
print('готово:',out, round(os.path.getsize(out)/1024,1),'КБ')
