# -*- coding: utf-8 -*-
import sys, os, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import content as C

def esc(s): return html.escape(str(s))

CSS = """
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Manrope',Arial,sans-serif;color:#111;background:#fff;font-size:14px;line-height:1.5}
h1,h2,h3,.ttl{font-family:'Oswald',Arial,sans-serif;font-weight:500;text-transform:uppercase;letter-spacing:.2px;color:#111}
.page{width:1440px;margin:0 auto}
.wrap{max-width:1240px;margin:0 auto;padding:0 40px}
section{position:relative;padding:54px 0}
.lbl{position:absolute;left:0;top:0;z-index:5;font-family:'Manrope';font-size:11px;font-weight:700;color:#fff;padding:4px 10px;letter-spacing:.3px}
.l-old{background:#E07B1E}.l-new{background:#7B3FBF}.l-hid{background:#8A8A8A}.l-sys{background:#4A5A6A}
.tag{display:inline-block;font-size:11px;font-weight:700;color:#012d66;background:#e5eaef;padding:2px 8px;border-radius:2px;margin-left:8px;vertical-align:middle;font-family:'Manrope'}
.eyebrow{font-size:12px;color:#012d66;font-weight:700;margin-bottom:14px;letter-spacing:.4px}
.eyebrow:before{content:'';display:inline-block;width:6px;height:6px;background:#012d66;margin-right:8px;vertical-align:middle}
h2{font-size:32px;line-height:1.15;margin-bottom:14px}
h3{font-size:18px;line-height:1.2;margin-bottom:8px}
p{margin-bottom:10px;color:#333}
.lead{color:#555;max-width:760px;margin-bottom:26px}
.btn{display:inline-block;background:#012d66;color:#fff;padding:13px 26px;font-size:13px;font-weight:600;border:1px solid #012d66}
.btn.ghost{background:transparent;color:#012d66}
.btn.white{background:#fff;color:#012d66;border-color:#fff}
.ph{background:repeating-linear-gradient(45deg,#e9e6df,#e9e6df 10px,#f3f1ec 10px,#f3f1ec 20px);border:1px solid #ddd8cf;display:flex;align-items:center;justify-content:center;text-align:center;color:#8d8madd;font-size:12px;color:#8a8375;padding:14px}
/* header */
.hdr{background:#012d66;color:#fff;padding:0}
.hdr .in{display:flex;align-items:center;gap:32px;height:74px}
.logo{width:96px;height:44px;border:1px solid rgba(255,255,255,.5);display:flex;align-items:center;justify-content:center;font-family:'Oswald';font-size:16px;letter-spacing:3px}
.hdr a{color:#fff;font-size:13px;opacity:.92}
.hdr .sp{flex:1}
.crumbs{padding:16px 0;font-size:12px;color:#777;border-bottom:1px solid #eee}
.crumbs b{color:#111;font-weight:600}
/* hero */
.hero{background:linear-gradient(180deg,rgba(0,15,35,.62),rgba(0,15,35,.72)),repeating-linear-gradient(45deg,#4a5561,#4a5561 14px,#556170 14px,#556170 28px);color:#fff;padding:70px 0 54px}
.hero h1{color:#fff;font-size:50px;line-height:1.08;max-width:900px;margin-bottom:18px}
.hero .sub{max-width:720px;font-size:16px;color:#e7ecf2;margin-bottom:22px}
.hero .price{font-family:'Oswald';font-size:22px;color:#fff;margin-bottom:24px}
.hero .btns{display:flex;gap:14px;margin-bottom:34px}
.chips{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}
.chip{border:1px solid rgba(255,255,255,.45);padding:14px;font-size:12.5px;color:#fff;min-height:74px;display:flex;align-items:center}
/* numbers */
.nums{display:grid;grid-template-columns:repeat(6,1fr);gap:20px;border-top:1px solid #e5eaef;border-bottom:1px solid #e5eaef;padding:30px 0}
.num b{display:block;font-family:'Oswald';font-size:28px;color:#012d66;margin-bottom:6px}
.num span{font-size:12px;color:#666;line-height:1.35;display:block}
/* text2col */
.t2{display:grid;grid-template-columns:1.15fr .85fr;gap:40px}
.t2 .ph{min-height:330px}
/* catalog */
.tabs{display:flex;gap:10px;margin-bottom:22px}
.tab{border:1px solid #d8dee6;padding:9px 22px;font-size:13px;color:#333}
.tab.on{background:#012d66;color:#fff;border-color:#012d66}
.cards2{display:grid;grid-template-columns:1fr 1fr;gap:22px}
.card{border:1px solid #e5eaef;padding:22px;background:#fff}
.card .ph{height:120px;margin-bottom:14px}
.card .pr{display:flex;gap:18px;margin:12px 0;font-family:'Oswald';font-size:16px;color:#012d66}
.card .pr i{font-style:normal;font-size:11px;color:#888;font-family:'Manrope';display:block}
.small{font-size:12px;color:#777}
/* spec table */
table{width:100%;border-collapse:collapse;font-size:13px}
th,td{border:1px solid #e1e6ec;padding:11px 13px;text-align:left;vertical-align:top}
th{background:#012d66;color:#fff;font-weight:600;font-size:12.5px}
tr:nth-child(even) td{background:#fafbfc}
/* genplan */
.gp{display:grid;grid-template-columns:repeat(12,1fr);gap:6px;margin-bottom:14px}
.gp div{height:44px;border:1px solid #cfd8e2;background:#eef2f6;font-size:10px;display:flex;align-items:center;justify-content:center;color:#5a6b7d}
.gp div.free{background:#e6f0e6;border-color:#a9c7a9;color:#3c6b3c}
.gp div.sold{background:#f1e6e6;border-color:#cba9a9;color:#8a4a4a}
/* accordion */
.acc{border:1px solid #e5eaef;margin-bottom:10px;padding:18px 22px}
.acc.first{background:#012d66;color:#fff;border-color:#012d66}
.acc .ttl{font-size:16px;margin-bottom:8px;display:block}
.acc.first .ttl,.acc.first p{color:#fff}
.acc p{margin:0;font-size:13px}
/* location */
.loc{display:grid;grid-template-columns:.9fr 1.1fr;gap:36px}
.pin{background:#012d66;color:#fff;font-size:13px;padding:11px 16px;margin-bottom:9px;display:block}
.map{min-height:340px}
/* gallery */
.gal{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}
.gal .ph{height:180px}
/* cards grid */
.cards3{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
.cards6{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
.cardb{background:#f5f7f9;border-left:3px solid #012d66;padding:20px}
.cardb .ttl{font-size:15px;margin-bottom:8px;display:block}
.cardb p{font-size:13px;margin:0}
/* steps */
.steps{display:grid;grid-template-columns:repeat(6,1fr);gap:14px}
.step{border-top:3px solid #012d66;padding-top:14px}
.step b{font-family:'Oswald';font-size:26px;color:#012d66;display:block;margin-bottom:6px}
.step .ttl{font-size:14px;display:block;margin-bottom:6px}
.step p{font-size:12px;margin:0}
/* docs */
.docs{display:grid;grid-template-columns:1.2fr .8fr;gap:36px}
.docs li{font-size:13px;color:#333;margin-bottom:11px;padding-left:18px;position:relative;list-style:none}
.docs li:before{content:'';position:absolute;left:0;top:7px;width:7px;height:7px;background:#012d66}
.docfile{border:1px solid #e5eaef;padding:13px 16px;font-size:13px;margin-bottom:10px;display:flex;justify-content:space-between;color:#012d66}
/* faq */
.q{border-bottom:1px solid #e5eaef;padding:15px 0}
.q .ttl{font-size:15px;text-transform:none;font-family:'Manrope';font-weight:700;display:flex;justify-content:space-between}
.q p{font-size:13px;margin-top:9px;max-width:960px}
/* form */
.formrow{display:grid;grid-template-columns:1fr 1fr;gap:40px;background:#f5f7f9}
.formrow .ph{min-height:420px;border:none}
.fbox{padding:42px 44px 42px 0}
.fld{border-bottom:1px solid #c9d2db;padding:12px 0;color:#9aa5b1;font-size:13px;margin-bottom:8px}
/* cta */
.cta{background:#0b2b1f;color:#fff;padding:26px 0}
.cta .in{display:flex;align-items:center;justify-content:space-between;gap:30px}
.cta .ttl{font-size:20px;color:#fff}
/* seo tail */
.tail{background:#f5f7f9}
.tail p{font-size:12.5px;color:#555}
.links{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-top:18px}
.links a{font-size:13px;color:#012d66;border:1px solid #d8dee6;background:#fff;padding:11px 14px;display:block}
/* footer */
.ftr{background:#012d66;color:#fff;padding:48px 0 26px}
.ftr .cols{display:grid;grid-template-columns:1.2fr 1fr 1fr 1fr;gap:30px}
.ftr .h{font-size:12px;font-weight:700;margin-bottom:14px}
.ftr .h:before{content:'';display:inline-block;width:6px;height:6px;background:#fff;margin-right:7px}
.ftr a,.ftr p{color:#c3cfdd;font-size:12.5px;margin-bottom:9px;display:block}
.ftr .bot{border-top:1px solid rgba(255,255,255,.2);margin-top:30px;padding-top:16px;display:grid;grid-template-columns:1.2fr 1fr 1fr 1fr;font-size:12px;color:#c3cfdd}
.rev{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
.rev .ph{height:150px}
.hint{font-size:11.5px;color:#9aa5b1;margin-top:12px;font-style:italic}
"""

def lab(b):
    st = b["status"]
    cls = "l-new" if st.startswith("новый") and "скрыт" not in st else ("l-hid" if "скрыт" in st else ("l-sys" if b["layout"] in ("header","footer") else "l-old"))
    return f'<div class="lbl {cls}">Блок {b["n"]} · {esc(b["name"])} · {esc(st)}</div>'

def head(b):
    if b["tag"] in ("H1","H2"):
        t = "h1" if b["tag"]=="H1" else "h2"
        return f'<{t}>{esc(b["head"])}</{t}>'
    return ""

def ph(text, cls=""):
    return f'<div class="ph {cls}">{esc(text)}</div>'

def render(b):
    L=b["layout"]; d=b.get("data"); o=[]
    if L=="header":
        return ('<section class="hdr" style="padding:0">'+lab(b)+'<div class="wrap in">'
          '<div class="logo">VITA</div><a>О компании</a><a>Объекты</a><a>Ход строительства</a>'
          '<a>Документация</a><a>Цены</a><a>Контакты</a><div class="sp"></div>'
          '<a>+7 (812) 574-47-47</a><a class="btn white">Заказать звонок</a></div></section>')
    if L=="crumbs":
        return ('<section style="padding:0" class="">'+lab(b)+'<div class="wrap crumbs" style="padding-top:26px">'
          'Главная / Объекты / <b>Производственные помещения</b></div></section>')
    if L=="hero":
        o.append('<section class="hero">'+lab(b)+'<div class="wrap">')
        o.append(f'<h1>{esc(d["h1"])}</h1><div class="sub">{esc(d["sub"])}</div>')
        o.append(f'<div class="price">{esc(d["price"])}</div><div class="btns">'
                 f'<span class="btn white">{esc(d["btns"][0])}</span><span class="btn" style="border-color:#fff;background:transparent">{esc(d["btns"][1])}</span></div>')
        o.append('<div class="chips">'+''.join(f'<div class="chip">{esc(c)}</div>' for c in d["chips"])+'</div>')
        o.append('</div></section>'); return ''.join(o)
    if L=="numbers":
        o.append('<section>'+lab(b)+'<div class="wrap"><div class="eyebrow">О парке</div>'+head(b))
        o.append('<div class="nums">'+''.join(f'<div class="num"><b>{esc(x)}</b><span>{esc(y)}</span></div>' for x,y in d)+'</div>')
        o.append('</div></section>'); return ''.join(o)
    if L=="text2col":
        o.append('<section>'+lab(b)+'<div class="wrap"><div class="eyebrow">Об объекте</div>'+head(b))
        o.append('<div class="t2"><div>'+''.join(f'<p>{esc(p)}</p>' for p in d["paras"])+'</div>'+ph(d["img"])+'</div>')
        o.append('</div></section>'); return ''.join(o)
    if L=="catalog":
        o.append('<section style="background:#f8f9fb">'+lab(b)+'<div class="wrap"><div class="eyebrow">Планировки</div>'+head(b))
        o.append(f'<p class="lead">{esc(d["lead"])}</p>')
        o.append('<div class="tabs"><span class="tab on">500 м²</span><span class="tab">750 м²</span><span class="tab">1000 м²</span><span class="tab">1500 м²</span><span class="tab">Объединённый блок</span></div>')
        o.append('<div class="cards2">')
        for t,tg,txt,p1,p2 in d["items"]:
            o.append('<div class="card">'+ph("План помещения: цех, офис на втором этаже, ворота")+
                     f'<h3>{esc(t)}<span class="tag">{tg}</span></h3><p style="font-size:13px">{esc(txt)}</p>'
                     f'<div class="pr"><span><i>Покупка</i>{esc(p1)}</span><span><i>Аренда</i>{esc(p2)}</span></div>'
                     '<span class="btn">Получить консультацию</span> <span class="btn ghost">Скачать планировку PDF</span></div>')
        o.append('</div>')
        o.append(f'<p class="small" style="margin-top:16px">{esc(d["note"])}</p>')
        o.append('</div></section>'); return ''.join(o)
    if L=="spectable":
        o.append('<section>'+lab(b)+'<div class="wrap"><div class="eyebrow">Характеристики</div>'+head(b))
        o.append('<table><tr><th style="width:34%">Параметр</th><th>Значение</th></tr>'+
                 ''.join(f'<tr><td>{esc(x)}</td><td>{esc(y)}</td></tr>' for x,y in d)+'</table>')
        o.append('</div></section>'); return ''.join(o)
    if L=="genplan":
        cells=''.join(f'<div class="{"free" if i%4 else "sold"}">{i+1:02d}</div>' for i in range(36))
        o.append('<section style="background:#f8f9fb">'+lab(b)+'<div class="wrap"><div class="eyebrow">Ген план объекта</div>'+head(b))
        o.append('<div class="gp">'+cells+'</div>')
        o.append(f'<p class="small">{esc(d)} Зелёный — свободно, серо-красный — продано. Статус обновляется еженедельно, дата обновления выводится под схемой.</p>')
        o.append('</div></section>'); return ''.join(o)
    if L=="accordion":
        o.append('<section>'+lab(b)+'<div class="wrap"><div class="eyebrow">О наших цехах</div>'+head(b))
        for i,(t,x) in enumerate(d):
            o.append(f'<div class="acc{" first" if i==0 else ""}"><span class="ttl">{esc(t)}</span><p>{esc(x)}</p></div>')
        o.append('</div></section>'); return ''.join(o)
    if L=="location":
        o.append('<section>'+lab(b)+'<div class="wrap"><div class="eyebrow">Локация</div>'+head(b))
        o.append('<div class="loc"><div>'+''.join(f'<span class="pin">{esc(p)}</span>' for p in d["points"])+'</div>'
                 +ph("Карта: Санкт-Петербург, Пушкинский район, Шушары, выезд на Московское шоссе","map")+'</div>')
        o.append('<div style="margin-top:24px;columns:2;column-gap:40px">'+''.join(f'<p>{esc(p)}</p>' for p in d["paras"])+'</div>')
        o.append('</div></section>'); return ''.join(o)
    if L=="gallery":
        o.append('<section style="background:#f8f9fb">'+lab(b)+'<div class="wrap"><div class="eyebrow">Фотографии</div>'+head(b))
        o.append('<div class="gal">'+''.join(ph(x) for x in d)+'</div>')
        o.append('<p class="hint">У каждого фото свой alt по шаблону из раздела 8. Под галереей — ссылка «Смотреть ход строительства».</p>')
        o.append('</div></section>'); return ''.join(o)
    if L=="cards6":
        o.append('<section>'+lab(b)+'<div class="wrap"><div class="eyebrow">Применение</div>'+head(b))
        o.append('<div class="cards6">'+''.join(f'<div class="cardb"><span class="ttl">{esc(t)}</span><p>{esc(x)}</p></div>' for t,x in d)+'</div>')
        o.append('</div></section>'); return ''.join(o)
    if L=="cards3":
        o.append('<section>'+lab(b)+'<div class="wrap"><div class="eyebrow">Сравнение</div>'+head(b))
        o.append('<div class="cards3">'+''.join(f'<div class="cardb"><span class="ttl">{esc(t)}</span><p>{esc(x)}</p></div>' for t,x in d)+'</div>')
        o.append('</div></section>'); return ''.join(o)
    if L=="pricetable":
        o.append('<section style="background:#f8f9fb">'+lab(b)+'<div class="wrap"><div class="eyebrow">Цены</div>'+head(b))
        o.append('<table><tr><th>Помещение</th><th>Общая площадь</th><th>Цена за м²</th><th>Стоимость покупки</th><th>Аренда</th></tr>'+
                 ''.join('<tr>'+''.join(f'<td>{esc(c)}</td>' for c in r)+'</tr>' for r in d["rows"])+'</table>')
        o.append('<p class="small" style="margin:10px 0 22px">Прайс актуален на [дата]. Кнопка «Скачать прайс PDF».</p>')
        o.append('<div style="columns:2;column-gap:40px">'+''.join(f'<p>{esc(p)}</p>' for p in d["paras"])+'</div>')
        o.append('<h3 style="margin-top:26px">Условия оплаты<span class="tag">H3</span></h3>')
        o.append('<div class="cards2" style="grid-template-columns:repeat(4,1fr)">'+
                 ''.join(f'<div class="cardb"><span class="ttl">{esc(t)}</span><p>{esc(x)}</p></div>' for t,x in d["terms"])+'</div>')
        o.append('</div></section>'); return ''.join(o)
    if L=="compare":
        o.append('<section>'+lab(b)+'<div class="wrap"><div class="eyebrow">Покупка или аренда</div>'+head(b))
        o.append('<table><tr>'+''.join(f'<th>{esc(h)}</th>' for h in d["header"])+'</tr>'+
                 ''.join('<tr>'+''.join(f'<td>{esc(c)}</td>' for c in r)+'</tr>' for r in d["rows"])+'</table>')
        o.append(f'<p style="margin-top:14px">{esc(d["after"])}</p>')
        o.append('</div></section>'); return ''.join(o)
    if L=="steps":
        o.append('<section style="background:#f8f9fb">'+lab(b)+'<div class="wrap"><div class="eyebrow">Сделка</div>'+head(b))
        o.append('<div class="steps">'+''.join(
            f'<div class="step"><b>{i+1}</b><span class="ttl">{esc(t)}</span><p>{esc(x)}</p></div>' for i,(t,x) in enumerate(d))+'</div>')
        o.append('<p class="small" style="margin-top:18px">Средний срок от первого звонка до ключей — около трёх недель. Менеджер: +7 (812) 574-47-47.</p>')
        o.append('</div></section>'); return ''.join(o)
    if L=="docs":
        o.append('<section>'+lab(b)+'<div class="wrap"><div class="eyebrow">Документы</div>'+head(b))
        o.append('<div class="docs"><ul>'+''.join(f'<li>{esc(x)}</li>' for x in d)+'</ul><div>'+
                 ''.join(f'<div class="docfile"><span>{n}</span><span>PDF</span></div>' for n in
                         ["Разрешение на ввод объекта","Выписка ЕГРН (образец)","Технические условия на сети","Типовой договор купли-продажи","Планировки блоков"])+
                 '</div></div>')
        o.append('</div></section>'); return ''.join(o)
    if L=="cases":
        o.append('<section style="background:#f8f9fb">'+lab(b)+'<div class="wrap"><div class="eyebrow">Резиденты</div>'+head(b))
        o.append('<div class="cards3">'+''.join(
            f'<div class="card">{ph("Фото цеха резидента")}<h3 style="font-size:16px">{esc(t)} · {esc(s)}</h3><p style="font-size:13px">{esc(x)}</p></div>'
            for t,s,x in d)+'</div>')
        o.append('<p class="hint">Блок свёрстан, показываем после согласования с резидентами.</p>')
        o.append('</div></section>'); return ''.join(o)
    if L=="reviews":
        o.append('<section>'+lab(b)+'<div class="wrap"><div class="eyebrow">Отзывы</div>'+head(b))
        o.append('<div class="rev">'+ph("Виджет Яндекс.Карт: карточка организации и рейтинг")+ph("Отзыв покупателя текстом в HTML")+ph("Отзыв покупателя текстом в HTML")+'</div>')
        o.append('<p class="hint">Блок свёрстан и скрыт до появления отзывов.</p>')
        o.append('</div></section>'); return ''.join(o)
    if L=="faq":
        o.append('<section style="background:#f8f9fb">'+lab(b)+'<div class="wrap"><div class="eyebrow">Вопросы и ответы</div>'+head(b))
        for i,(q,a) in enumerate(d):
            body=f'<p>{esc(a)}</p>' if i<3 else ''
            o.append(f'<div class="q"><span class="ttl">{esc(q)}<span>{"–" if i<3 else "+"}</span></span>{body}</div>')
        o.append('<p style="margin-top:20px"><span class="btn">Задать вопрос менеджеру</span></p>')
        o.append('</div></section>'); return ''.join(o)
    if L=="form":
        o.append('<section style="padding-bottom:0">'+lab(b)+'<div class="wrap"><div class="eyebrow">Контакты</div>')
        o.append('<div class="formrow">'+ph("Фото: ворота цехов парка")+f'<div class="fbox">{head(b)}'
                 f'<p style="margin-bottom:20px">{esc(d["text"])}</p>'+
                 ''.join(f'<div class="fld">{esc(f)}</div>' for f in d["fields"])+
                 '<div class="fld" style="border:none;color:#333">☐ Нужна рассрочка &nbsp;&nbsp; ☐ Согласен с политикой конфиденциальности</div>'
                 f'<div class="btn" style="width:100%;text-align:center;margin-top:10px">{esc(d["btn"])}</div></div>')
        o.append('</div></div></section>'); return ''.join(o)
    if L=="seotail":
        o.append('<section class="tail">'+lab(b)+'<div class="wrap">'+head(b))
        o.append(''.join(f'<p>{esc(p)}</p>' for p in d["paras"]))
        o.append('<div class="links">'+''.join(f'<a>{esc(t)} <span style="color:#9aa5b1">{esc(u)}</span></a>' for t,u in d["links"])+'</div>')
        o.append('</div></section>'); return ''.join(o)
    if L=="footer":
        return ('<section class="ftr">'+lab(b)+'<div class="wrap"><div class="cols">'
          '<div><div class="logo" style="margin-bottom:14px">VITA</div></div>'
          '<div><div class="h">Контакты</div><a>+7 (812) 574-47-47</a><a>info@isk-vita.ru</a>'
          '<div class="h" style="margin-top:22px">Адрес офиса</div><p>Санкт-Петербург, площадь Конституции, д. 3а, БЦ «Пирамида», 9 этаж, офис 901–914</p></div>'
          '<div><div class="h">Навигация</div><a>О компании</a><a>Документация</a><a>Ход строительства</a><a>Контакты</a></div>'
          '<div><div class="h">Объекты</div><a>Цеха</a><a>Склады</a></div></div>'
          '<div class="bot"><span>ООО «Иск Вита»</span><span>Политика конфиденциальности</span><span>Разработка сайта</span><span></span></div>'
          '</div></section>')
    return '<section>'+lab(b)+'<div class="wrap">'+head(b)+'</div></section>'

def cta(text):
    return ('<section class="cta" style="padding:26px 0"><div class="lbl l-new" style="background:#0b2b1f">CTA-строка</div>'
            f'<div class="wrap in"><span class="ttl">{esc(text)}</span><span class="btn white">Оставить заявку</span></div></section>')

def build():
    parts=[]
    for b in C.BLOCKS:
        parts.append(render(b))
        if b["n"] in C.CTA_AFTER: parts.append(cta(C.CTA_AFTER[b["n"]]))
    doc=('<!doctype html><html lang="ru"><head><meta charset="utf-8">'
         '<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@300;400;500;600&family=Manrope:wght@300;400;500;600;700&display=swap" rel="stylesheet">'
         f'<style>{CSS}</style></head><body><div class="page">'+''.join(parts)+'</div></body></html>')
    out=os.path.join(os.path.dirname(os.path.abspath(__file__)),'mock.html')
    open(out,'w',encoding='utf8').write(doc)
    print('written',out,len(doc))

if __name__=="__main__": build()
