import json
from PIL import Image, ImageDraw, ImageFont
secs=json.load(open('sections.json'))
im=Image.open('shots/mock_full.png'); W,H=im.size; k=W/1440.0
assert abs(H - (secs[-1]['top']+secs[-1]['h'])*k) < 30, 'скриншот и замеры не совпадают'
MAX=1250; parts=[];cur=[];curh=0
for s in secs:
    if cur and curh+s['h']>MAX: parts.append(cur);cur=[];curh=0
    cur.append(s);curh+=s['h']
if cur: parts.append(cur)
if sum(x['h'] for x in parts[-1])<450: parts[-2]+=parts[-1]; parts.pop()
res=[]
for i,pt in enumerate(parts):
    top=pt[0]['top']; bot=pt[-1]['top']+pt[-1]['h']
    crop=im.crop((0,max(0,int(top*k)),W,min(H,int(bot*k))))
    fn=f'shots/mock_part{i+1:02d}.png'; crop.save(fn)
    res.append({"file":fn,"labels":[s['label'] for s in pt],"size":crop.size})
    print(i+1, crop.size[1], ' | '.join(s['label'].replace('Блок ','').split(' · ')[0] for s in pt))
json.dump(res,open('parts.json','w'),ensure_ascii=False,indent=1)
cols=3;scale=0.30;sw=int(W*scale);bounds=[0]
for c in range(1,cols):
    t=H/cols*c; best=min(secs,key=lambda s: abs(s['top']*k-t)); bounds.append(int(best['top']*k))
bounds.append(H)
sc=[im.crop((0,bounds[i],W,bounds[i+1])).resize((sw,int((bounds[i+1]-bounds[i])*scale)),Image.LANCZOS) for i in range(cols)]
maxh=max(c.size[1] for c in sc);gap=26;pad=30;topbar=34
out=Image.new('RGB',(pad*2+sw*cols+gap*(cols-1),pad*2+topbar+maxh),'white')
dr=ImageDraw.Draw(out);f=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',26)
for i,c in enumerate(sc):
    x=pad+i*(sw+gap); out.paste(c,(x,pad+topbar)); dr.text((x,pad+2),str(i+1),fill='#333',font=f)
    dr.rectangle([x-1,pad+topbar-1,x+sw,pad+topbar+c.size[1]],outline='#cccccc')
out.save('shots/mock_overview.png')
def save(src,dst,maxw,q=84):
    i2=Image.open(src).convert('RGB')
    if i2.size[0]>maxw: i2=i2.resize((maxw,int(i2.size[1]*maxw/i2.size[0])),Image.LANCZOS)
    i2.save(dst,'JPEG',quality=q,optimize=True)
save('shots/mock_overview.png','media/fig_overview.jpg',1700,85)
save('shots/mock_mobile.png','media/fig_mobile.jpg',560,88)
for i,p in enumerate(res,1): save(p['file'],f'media/fig_part{i:02d}.jpg',1500,84)
print('parts',len(parts),'overview',out.size)
