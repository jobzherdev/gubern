# -*- coding: utf-8 -*-
"""Собирает всю страницу /workshops одним блоком T123 — по образцу /warehouses."""
import sys, os, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import content as C

e = html.escape
B = {b['n']: b for b in C.BLOCKS}

IMG = dict(
    hero="https://static.tildacdn.com/tild6635-3766-4431-b032-653035343361/blob.webp",        # фасад Г6, панорама
    facade="https://static.tildacdn.com/tild3163-3132-4263-b837-386431373236/blob.webp",      # ворота крупно
    truck="https://static.tildacdn.com/tild3362-3064-4662-b561-333738353733/photo_2026-08-30_18-.jpg",
    gates="https://static.tildacdn.com/tild3766-6535-4239-a139-336364316338/blob.webp",       # корпус Д6/Д7
    aerial="https://static.tildacdn.com/tild3865-6265-4234-a461-636531353731/blob.webp",      # вид сверху
    genplan="https://static.tildacdn.com/tild3338-6139-4135-b438-653263313631/0020_1.jpg",
    plan500="https://static.tildacdn.com/tild3465-3637-4735-b261-393234383766/blob.webp",
    plan750="https://static.tildacdn.com/tild3331-3333-4230-b763-376338653061/image_20.png",
    plan1000="https://static.tildacdn.com/tild6563-6539-4033-b830-636564636430/image_21.png",
    plan1500="https://static.tildacdn.com/tild6539-3836-4432-b139-663131373538/image_22.png",
    s2000="https://static.tildacdn.com/tild3161-6233-4933-b935-326363313134/Frame_892.png",
    s3000="https://static.tildacdn.com/tild3565-3738-4761-b965-656633383531/Frame_893.png",
    s7000="https://static.tildacdn.com/tild6137-6239-4666-a633-653466353432/Frame_894.png",
    s10000="https://static.tildacdn.com/tild3464-3961-4631-b465-656332383533/Frame_895.png",
)
POPUP = "#zeropopup"

CSS = """<style>
.vi{font-family:'Manrope',Arial,sans-serif;color:#111;font-size:16px;line-height:1.55;max-width:1240px;margin:0 auto;padding:0 20px;box-sizing:border-box}
.vi *{box-sizing:border-box}
.vi h2,.vi h3,.vi .vi-ttl{font-family:'Oswald',Arial,sans-serif;font-weight:500;color:#111;margin:0 0 14px}
.vi h2{font-size:34px;line-height:1.15;text-transform:uppercase}
.vi h3{font-size:21px;line-height:1.2;margin:26px 0 10px}
.vi p{margin:0 0 12px;color:#333}
.vi a{color:#012d66}
.vi-eyebrow{font-size:13px;font-weight:700;color:#012d66;margin-bottom:12px;letter-spacing:.3px}
.vi-eyebrow:before{content:'';display:inline-block;width:6px;height:6px;background:#012d66;margin-right:8px;vertical-align:middle}
.vi-btn{display:inline-block;background:#012d66;color:#fff!important;padding:14px 28px;font-size:14px;font-weight:600;text-decoration:none;border:1px solid #012d66;margin:4px 10px 4px 0}
.vi-btn--ghost{background:transparent;color:#012d66!important}
.vi-btn--white{background:#fff;color:#012d66!important;border-color:#fff}
.vi-note{font-size:13.5px;color:#666;margin-top:12px}
.vi-table{width:100%;border-collapse:collapse;font-size:15px}
.vi-table th,.vi-table td{border:1px solid #e1e6ec;padding:12px 15px;text-align:left;vertical-align:top}
.vi-table th{background:#012d66;color:#fff;font-weight:600;font-size:14px}
.vi-table tr:nth-child(even) td{background:#fafbfc}
.vi-grid-2{display:grid;grid-template-columns:1fr 1fr;gap:26px}
.vi-grid-2--text{grid-template-columns:1.1fr .9fr;align-items:start}
.vi-grid-3{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
.vi-grid-4{display:grid;grid-template-columns:repeat(4,1fr);gap:20px}
.vi-card{background:#f5f7f9;border-left:3px solid #012d66;padding:22px}
.vi-card .vi-ttl{font-size:17px;display:block;margin-bottom:8px}
.vi-card p{font-size:14.5px;margin:0}
.vi-sect{padding:56px 0}
.vi-sect--grey{background:#f8f9fb}
.vi-cta{background:#0b2b1f;color:#fff;padding:28px 0}
.vi-cta .vi{display:flex;align-items:center;justify-content:space-between;gap:20px;flex-wrap:wrap}
.vi-cta .vi-ttl{color:#fff;font-size:22px;margin:0}
.vi-top img{width:100%;height:auto;display:block}
.vi-hero{background:#012d66;color:#fff;padding:30px 0 34px}
.vi-hero .vi,.vi-hero .vi-price,.vi-hero .vi-pill b{color:#fff}
.vi-hero h1{font-family:'Oswald',Arial,sans-serif;font-weight:500;font-size:40px;line-height:1.12;text-transform:uppercase;margin:0 0 14px;color:#fff}
.vi-hero p{color:#fff;opacity:.92;font-size:18px;max-width:880px}
.vi-price{display:inline-block;border:1px solid rgba(255,255,255,.35);background:rgba(255,255,255,.1);padding:10px 18px;font-family:'Oswald',Arial,sans-serif;font-size:19px;margin:4px 0 16px}
.vi-pills{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:22px}
.vi-pill{border:1px solid rgba(255,255,255,.25);background:rgba(255,255,255,.08);padding:14px 16px}
.vi-pill b{display:block;font-family:'Oswald',Arial,sans-serif;font-size:20px;font-weight:500;margin-bottom:4px}
.vi-pill span{font-size:13.5px;opacity:.85}
.vi-crumbs{font-size:13px;color:#666;padding:12px 0}
.vi-crumbs a{color:#666;text-decoration:none}
.vi-plan{border:1px solid #e5eaef;background:#fff;padding:0 0 22px}
.vi-plan img{width:100%;height:auto;display:block;background:#f5f7f9}
.vi-plan .in{padding:0 22px}
.vi-plan .pr{font-family:'Oswald',Arial,sans-serif;font-size:19px;color:#012d66;margin:10px 0 14px}
.vi-steps{counter-reset:s;margin:0;padding:0;list-style:none}
.vi-steps li{display:grid;grid-template-columns:44px 1fr 220px;gap:16px;padding:16px 0;border-bottom:1px solid #e5eaef}
.vi-steps .n{font-family:'Oswald',Arial,sans-serif;font-size:26px;color:#012d66}
.vi-steps b{display:block;font-size:16px;margin-bottom:4px}
.vi-steps p{margin:0;font-size:15px}
.vi-steps .r{font-size:14px;color:#012d66;font-weight:600}
.vi-map{position:relative;background:#eef2f6;min-height:340px}
.vi-map iframe{position:absolute;inset:0;width:100%;height:100%;border:0}
.vi-pin{background:#012d66;color:#fff;font-size:14px;padding:11px 16px;margin-bottom:9px;display:block}
.vi-gal{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}
.vi-gal img{width:100%;height:220px;object-fit:cover;display:block}
.vi-docs li{font-size:15px;color:#333;margin-bottom:11px;padding-left:18px;position:relative;list-style:none}
.vi-docs li:before{content:'';position:absolute;left:0;top:8px;width:7px;height:7px;background:#012d66}
.vi-q{border-bottom:1px solid #e5eaef;padding:4px 0}
.vi-q summary{list-style:none;cursor:pointer;padding:16px 36px 16px 0;position:relative;font-weight:700;font-size:16.5px;color:#111}
.vi-q summary::-webkit-details-marker{display:none}
.vi-q summary:after{content:'+';position:absolute;right:6px;top:13px;font-size:22px;color:#012d66;font-weight:400}
.vi-q[open] summary:after{content:'\\2212'}
.vi-q .vi-a{padding:0 36px 16px 0}
.vi-q .vi-a p{margin:0;font-size:15px}
.vi-links{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
.vi-links a{display:block;border:1px solid #d8dee6;background:#fff;padding:14px 16px;text-decoration:none;font-size:15px}
.vi-links small{display:block;color:#777;margin-top:4px;font-size:13px}
@media screen and (max-width:960px){
  .vi h2{font-size:26px}
  .vi-hero h1{font-size:28px}
  .vi-grid-2,.vi-grid-2--text,.vi-grid-3,.vi-grid-4,.vi-pills,.vi-links{grid-template-columns:1fr}
  .vi-gal{grid-template-columns:1fr 1fr}
  .vi-sect{padding:38px 0}
  .vi-steps li{grid-template-columns:34px 1fr}
  .vi-steps .r{grid-column:2}
  .vi-scroll{overflow-x:auto;-webkit-overflow-scrolling:touch}
  .vi-scroll .vi-table{min-width:580px}
}
</style>"""

O=[]
A=O.append

A("""<!-- /workshops: всё наполнение страницы одним блоком T123. Собрано по ТЗ.
     Все кнопки заявки открывают окно #zeropopup (форма «Закажите обратный звонок»), оно уже есть на странице.
     Изображения — файлы, уже загруженные в этот проект Tilda. -->""")
A(CSS)

# ---------- 2. Первый экран ----------
hero=B[2]['data']
A(f"""
<div class="vi-top">
<picture>
  <source media="(max-width:640px)" srcset="{IMG['facade']}">
  <img src="{IMG['hero']}" alt="Производственные цеха индустриального парка «Вита» в Шушарах: корпуса с секционными воротами и проездами" fetchpriority="high">
</picture>
<div class="vi-hero">
  <div class="vi">
    <div class="vi-crumbs" style="color:#cfd8e3;padding-top:0"><a href="/" style="color:#cfd8e3">Главная</a> / <span>Производственные помещения</span></div>
    <h1>{e(hero['h1'])}</h1>
    <p>{e(hero['sub'])}</p>
    <div class="vi-price">{e(hero['price'])}</div>
    <div>
      <a href="{POPUP}" class="vi-btn vi-btn--white">{e(hero['btns'][0])}</a>
      <a href="#prices" class="vi-btn vi-btn--ghost" style="color:#fff!important;border-color:rgba(255,255,255,.7)">{e(hero['btns'][1])}</a>
    </div>
    <div class="vi-pills">""")
PILLS = [("36 зданий", "в парке, свободные блоки 500–1500 м²"),
         ("8 м", "высота до низа конструкций, нагрузка на пол 5 т/м²"),
         ("Газ, 25 кВт", "вода и септик заведены в каждый блок"),
         ("7–14 дней", "регистрация права собственности в Росреестре")]
for b_, s_ in PILLS:
    A(f'      <div class="vi-pill"><b>{e(b_)}</b><span>{e(s_)}</span></div>')
A("""    </div>
  </div>
</div>
</div>""")

# ---------- 3. Парк в цифрах ----------
A(f"""
<div class="vi-sect">
  <div class="vi">
    <div class="vi-eyebrow">О парке</div>
    <h2>{e(B[3]['head'])}</h2>
    <div class="vi-grid-3">""")
for num, txt in B[3]['data']:
    A(f'      <div class="vi-card"><span class="vi-ttl" style="font-size:26px">{e(num)}</span><p>{e(txt)}</p></div>')
A("""    </div>
  </div>
</div>""")

# ---------- 4. Вводный SEO-блок ----------
d=B[4]['data']
A(f"""
<div class="vi-sect vi-sect--grey">
  <div class="vi">
    <div class="vi-eyebrow">Об объекте</div>
    <h2>{e(B[4]['head'])}</h2>
    <div class="vi-grid-2 vi-grid-2--text">
      <div>""")
for p in d['paras']: A(f'        <p>{e(p)}</p>')
A(f"""      </div>
      <div><img src="{IMG['facade']}" alt="Производственное помещение в индустриальном парке «Вита», Шушары — секционные ворота цеха и зона разгрузки" loading="lazy" style="width:100%;height:auto;display:block"></div>
    </div>
  </div>
</div>""")

# ---------- 5. Каталог ----------
cat=B[5]['data']
PLANS=[(IMG['plan500'],'500'),(IMG['plan750'],'750'),(IMG['plan1000'],'1000'),(IMG['plan1500'],'1500')]
A(f"""
<div class="vi-sect" id="plans">
  <div class="vi">
    <div class="vi-eyebrow">Планировки</div>
    <h2>{e(B[5]['head'])}</h2>
    <p style="max-width:860px">{e(cat['lead'])}</p>
    <div class="vi-grid-2" style="margin-top:26px">""")
for (t,_,txt,price),(img,area) in zip(cat['items'],PLANS):
    A(f"""      <div class="vi-plan">
        <img src="{img}" alt="План производственного помещения {area} м² в индустриальном парке «Вита», Шушары: цех на первом этаже и офис-мезонин" loading="lazy">
        <div class="in"><h3>{e(t)}</h3><p>{e(txt)}</p>
          <div class="pr">{e(price)}</div>
          <a href="{POPUP}" class="vi-btn">Получить консультацию</a></div>
      </div>""")
A(f"""    </div>
    <h3 style="margin-top:34px">Комплексные решения 2000–10 000 м²</h3>
    <p style="max-width:860px">{e(cat['note'])}</p>
    <div class="vi-grid-4" style="margin-top:18px">
      <div><img src="{IMG['s2000']}" alt="Схема комплексного производственного решения 2000 м²" loading="lazy" style="width:100%;height:auto"><p class="vi-note">2000 м²</p></div>
      <div><img src="{IMG['s3000']}" alt="Схема комплексного производственного решения 3000 м²" loading="lazy" style="width:100%;height:auto"><p class="vi-note">3000 м²</p></div>
      <div><img src="{IMG['s7000']}" alt="Схема комплексного производственного решения 7000 м²" loading="lazy" style="width:100%;height:auto"><p class="vi-note">7000 м²</p></div>
      <div><img src="{IMG['s10000']}" alt="Схема комплексного производственного решения 10 000 м²" loading="lazy" style="width:100%;height:auto"><p class="vi-note">10 000 м²</p></div>
    </div>
  </div>
</div>""")

def cta(text):
    A(f"""
<div class="vi-cta">
  <div class="vi"><span class="vi-ttl">{e(text)}</span><a href="{POPUP}" class="vi-btn vi-btn--white">Оставить заявку</a></div>
</div>""")
cta(C.CTA_AFTER[5])

# ---------- 6. Технические характеристики ----------
A(f"""
<div class="vi-sect vi-sect--grey">
  <div class="vi">
    <div class="vi-eyebrow">Характеристики</div>
    <h2>{e(B[6]['head'])}</h2>
    <div class="vi-scroll"><table class="vi-table">
      <tr><th style="width:34%">Параметр</th><th>Значение</th></tr>""")
for k,v in B[6]['data']: A(f'      <tr><td>{e(k)}</td><td>{e(v)}</td></tr>')
A("""    </table></div>
  </div>
</div>""")

# ---------- 7. Генплан ----------
A(f"""
<div class="vi-sect" id="genplan-map">
  <div class="vi">
    <div class="vi-eyebrow">Генеральный план</div>
    <h2>{e(B[7]['head'])}</h2>
    <img src="{IMG['genplan']}" alt="Генеральный план индустриального парка «Вита» в Шушарах: 36 зданий, внутренние проезды и выезд на Московское шоссе" loading="lazy" style="width:100%;height:auto;display:block">
    <p class="vi-note">На схеме — 36 зданий парка с внутренними проездами и зонами разгрузки. Свободные производственные помещения и их площади менеджер показывает на актуальной версии плана: статус свободных блоков обновляется еженедельно.</p>
    <p><a href="{POPUP}" class="vi-btn">Узнать свободные помещения</a></p>
  </div>
</div>""")

# ---------- 8. Что входит в цену ----------
ld=B[8].get('lead',{})
A(f"""
<div class="vi-sect vi-sect--grey">
  <div class="vi">
    <div class="vi-eyebrow">{e(ld.get('eyebrow','О наших цехах'))}</div>
    <h2>{e(B[8]['head'])}</h2>
    <p style="max-width:860px">{e(ld.get('text',''))}</p>
    <div class="vi-grid-3" style="margin-top:22px">""")
for t,x in B[8]['data']:
    A(f'      <div class="vi-card"><span class="vi-ttl">{e(t)}</span><p>{e(x)}</p></div>')
A(f"""    </div>
    <p style="margin-top:20px"><a href="{POPUP}" class="vi-btn">{e(ld.get('btn','Получить консультацию'))}</a></p>
  </div>
</div>""")

# ---------- 9. Локация ----------
loc=B[9]['data']
A(f"""
<div class="vi-sect">
  <div class="vi">
    <div class="vi-eyebrow">Локация</div>
    <h2>{e(B[9]['head'])}</h2>
    <div class="vi-grid-2">
      <div>""")
for p in loc['points']: A(f'        <span class="vi-pin">{e(p)}</span>')
A("""      </div>
      <div class="vi-map"><iframe src="https://yandex.ru/map-widget/v1/?ll=30.432597%2C59.772195&amp;z=12&amp;pt=30.432597%2C59.772195%2Cpm2rdm" loading="lazy" allowfullscreen title="Индустриальный парк «Вита» на карте: Санкт-Петербург, Пушкинский район, Шушары"></iframe></div>
    </div>
    <div style="margin-top:24px">""")
for p in loc['paras']: A(f'      <p>{e(p)}</p>')
A("""    </div>
  </div>
</div>""")

# ---------- 10. Фотографии ----------
A(f"""
<div class="vi-sect vi-sect--grey">
  <div class="vi">
    <div class="vi-eyebrow">Фотографии</div>
    <h2>{e(B[10]['head'])}</h2>
    <div class="vi-gal">
      <img src="{IMG['facade']}" alt="Производственные помещения парка «Вита», Шушары — фасад корпуса с секционными воротами" loading="lazy">
      <img src="{IMG['gates']}" alt="Производственный корпус индустриального парка «Вита» — ворота и зона разгрузки у цеха" loading="lazy">
      <img src="{IMG['aerial']}" alt="Индустриальный парк «Вита» в Шушарах с высоты: корпуса, проезды и парковка" loading="lazy">
      <img src="{IMG['truck']}" alt="Производственное помещение парка «Вита» — подъезд фуры к воротам цеха" loading="lazy">
    </div>
    <p class="vi-note">Строительство идёт очередями. Актуальные фотографии — в разделе <a href="/progress">«Ход строительства»</a>.</p>
  </div>
</div>""")

# ---------- 11. Для каких производств ----------
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

# ---------- 12. Цены ----------
pr=B[12]['data']
A(f"""
<div class="vi-sect vi-sect--grey" id="prices">
  <div class="vi">
    <div class="vi-eyebrow">Цены</div>
    <h2>{e(B[12]['head'])}</h2>
    <div class="vi-scroll"><table class="vi-table">
      <tr><th>Помещение</th><th>Общая площадь</th><th>Цена за м²</th><th>Стоимость покупки</th></tr>""")
for r in pr['rows']: A('      <tr>'+''.join(f'<td>{e(c)}</td>' for c in r)+'</tr>')
A("""    </table></div>
    <p class="vi-note">Цена указана за квадратный метр общей площади помещения. Точную стоимость выбранного блока менеджер подтверждает при бронировании.</p>
    <div class="vi-grid-2" style="margin-top:24px">""")
for p in pr['paras']: A(f'      <p>{e(p)}</p>')
A("""    </div>
    <h3>Условия оплаты</h3>
    <div class="vi-grid-4">""")
for t,x in pr['terms']:
    A(f'      <div class="vi-card"><span class="vi-ttl">{e(t)}</span><p>{e(x)}</p></div>')
A("""    </div>
  </div>
</div>""")
cta(C.CTA_AFTER[12])

# ---------- 13. Купить или арендовать ----------
cmp_=B[13]['data']
A(f"""
<div class="vi-sect">
  <div class="vi">
    <div class="vi-eyebrow">Покупка или аренда</div>
    <h2>{e(B[13]['head'])}</h2>
    <div class="vi-scroll"><table class="vi-table">
      <tr>"""+''.join(f'<th>{e(x)}</th>' for x in cmp_['header'])+"</tr>")
for r in cmp_['rows']: A('      <tr>'+''.join(f'<td>{e(c)}</td>' for c in r)+'</tr>')
A(f"""    </table></div>
    <p style="margin-top:14px">{e(cmp_['after'])}</p>
  </div>
</div>""")

# ---------- 14. Новый или вторичка ----------
A(f"""
<div class="vi-sect vi-sect--grey">
  <div class="vi">
    <div class="vi-eyebrow">Сравнение</div>
    <h2>{e(B[14]['head'])}</h2>
    <div class="vi-grid-3">""")
for t,x in B[14]['data']:
    A(f'      <div class="vi-card"><span class="vi-ttl">{e(t)}</span><p>{e(x)}</p></div>')
A("""    </div>
  </div>
</div>""")

# ---------- 15. Этапы ----------
STEP_R=['1 день','в любой будний день','5 рабочих дней','по готовности документов','7–14 рабочих дней','передача по акту']
A(f"""
<div class="vi-sect">
  <div class="vi">
    <div class="vi-eyebrow">Сделка</div>
    <h2>{e(B[15]['head'])}</h2>
    <ul class="vi-steps">""")
for i,((t,x),r) in enumerate(zip(B[15]['data'],STEP_R),1):
    A(f'      <li><span class="n">{i}</span><div><b>{e(t)}</b><p>{e(x)}</p></div><span class="r">{e(r)}</span></li>')
A("""    </ul>
    <p class="vi-note">Средний срок от первого звонка до получения ключей — около трёх недель. Менеджер: <a href="tel:+78125744747">+7 (812) 574-47-47</a>.</p>
  </div>
</div>""")

# ---------- 16. Документы ----------
A(f"""
<div class="vi-sect vi-sect--grey">
  <div class="vi">
    <div class="vi-eyebrow">Документы</div>
    <h2>{e(B[16]['head'])}</h2>
    <ul class="vi-docs" style="padding:0;margin:0">""")
for x in B[16]['data']: A(f'      <li>{e(x)}</li>')
A(f"""    </ul>
    <p style="margin-top:18px">Полный пакет — в разделе <a href="/documentation">«Документация»</a>. <a href="{POPUP}" class="vi-btn" style="margin-left:10px">Запросить документы</a></p>
  </div>
</div>""")
cta(C.CTA_AFTER[16])

# ---------- 17. FAQ ----------
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
A(f"""    <p style="margin-top:24px"><a href="{POPUP}" class="vi-btn">Задать вопрос менеджеру</a></p>
  </div>
</div>""")

# ---------- 18. Заявка ----------
f18=B[18]['data']
A(f"""
<div class="vi-sect vi-sect--grey" id="contacts">
  <div class="vi">
    <div class="vi-eyebrow">Контакты</div>
    <h2>{e(B[18]['head'])}</h2>
    <div class="vi-grid-2">
      <div>
        <p>{e(f18['text'])}</p>
        <p><a href="{POPUP}" class="vi-btn">Оставить заявку</a>
           <a href="tel:+78125744747" class="vi-btn vi-btn--ghost">+7 (812) 574-47-47</a></p>
        <p class="vi-note">Почта: <a href="mailto:info@isk-vita.ru">info@isk-vita.ru</a>. Объект: Санкт-Петербург, Пушкинский район, Шушары, выезд на Московское шоссе. Офис: площадь Конституции, д. 3а, БЦ «Пирамида», офис 901–914.</p>
      </div>
      <div><img src="{IMG['aerial']}" alt="Индустриальный парк «Вита» в Шушарах — вид на корпуса и территорию" loading="lazy" style="width:100%;height:auto;display:block"></div>
    </div>
  </div>
</div>""")

# ---------- 19. Текст низа ----------
tail=B[19]['data']
A(f"""
<div class="vi-sect">
  <div class="vi">
    <h2 style="font-size:26px">{e(B[19]['head'])}</h2>""")
for p in tail['paras']: A(f'    <p style="font-size:15px;color:#555">{e(p)}</p>')
A('    <div class="vi-links" style="margin-top:18px">')
for t,u in tail['links']:
    A(f'      <a href="{u}">{e(t)}<small>{u}</small></a>')
A("""    </div>
  </div>
</div>""")

out=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'deliver2','workshops_одним_блоком_T123.html')
os.makedirs(os.path.dirname(out),exist_ok=True)
open(out,'w',encoding='utf8').write('\n'.join(O))
print('готово:',out, round(os.path.getsize(out)/1024,1),'КБ')
