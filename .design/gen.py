# -*- coding: utf-8 -*-
import io, math

NAVN = {1:("Havtor Øvergård","f. 1965"),2:("Lars Magnus Thomassen","1934–2017"),3:("Brit Hansen","f. 1941"),
4:("Jørgen Emil Thomassen","1898–1965"),5:("Guro Fredrikke Hapalahti","1909–1986"),6:("Andreas Hansen","1912–1986"),
7:("Anna Noste","1915–2006"),8:("Mons Thomassen","1861–1922"),9:("Britha Marie Suhr","1868–1936"),
10:("Lars Magnus Hapalahti","1882–1919"),11:("Charlotte (Lotta) Romsdal","1877–1930"),
12:("Nils Anders Hansen (Madvig)","1890–1947"),13:("Sigrid Gunhild Larsdatter Koi","1880–1932"),
14:("Mathis Nilsen Noste","1871–1957"),15:("Risten (Kristine) Bigga Persdatter Halt","1877–1924"),
16:("Thomas Mathias Olsen","1832–1911"),17:("Karen Monsdatter","1827–1908"),18:("Fredrik Johannes (Johan) Suhr","1843–1911"),
19:("Berith (Britha) Olsdatter Monsen","1829–1893"),20:("Johan Fredrik Hapalahti","1845–1905"),
21:("Guro Larsdatter Romsdal","1846–1900"),22:("Ole S. Romsdal","1851–1911"),23:("Randi Larsdatter Sætrum","1856–1950"),
24:("Hans Saraksen Madvig","1845–1920"),25:("Gunhild Nilsdatter","1848–1892"),26:("Lars Persen Koi","1839–1901"),
27:("Birgit Saraksdatter Madvig","1842–1920"),28:("Nils Mortensen Noste","1835–1916"),29:("Birthe (Bigga) Olsdatter","1828–1906"),
30:("Petrus (Per) Mathisen Halt","1837–1888"),31:("Marta (Magga) Persdatter Sjang","1842–etter 1888")}
SIK = {1:'b',2:'b',3:'b',4:'b',5:'b',6:'b',7:'b',8:'b',9:'b',10:'b',11:'b',12:'b',13:'s',14:'b',15:'s',
16:'b',17:'b',18:'b',19:'b',20:'b',21:'b',22:'b',23:'b',24:'b',25:'s',26:'b',27:'s',28:'b',29:'s',30:'b',31:'u'}
FARGE = {'b':'#1f7d55','s':'#c98f10','u':'#a63a44'}

def side(a):
    while a > 3: a //= 2
    return 'far' if a == 2 else ('mor' if a == 3 else 'meg')

BLA, TERRA = '#8fa9c0', '#d9a98c'

def esc(s): return s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')

def kort(x, y, w, h, anenr, navnfs=15, aarfs=11.5, stor=False):
    navn, aar = NAVN[anenr]
    s = side(anenr)
    bar = '#b9c4cd' if s == 'meg' else (BLA if s == 'far' else TERRA)
    pad = 14 if not stor else 18
    return f'''    <div style="position: absolute; left: {x}px; top: {y}px; width: {w}px; height: {h}px; box-sizing: border-box; background: #ffffff; border: 1px solid #e3e6ea; border-left: 4px solid {bar}; border-radius: 10px; box-shadow: 0 1px 2px rgba(20, 30, 50, 0.05); padding: {pad-4}px {pad}px; display: flex; flex-direction: column; justify-content: center; gap: 3px; overflow: hidden;">
      <div style="font: {'600 ' if stor else ''}{navnfs}px/1.25 'Iowan Old Style', 'Palatino Linotype', Palatino, Georgia, serif; color: #14161a; text-wrap: pretty;">{esc(navn)}</div>
      <div style="display: flex; align-items: center; gap: 7px;">
        <span style="width: 6px; height: 6px; border-radius: 50%; background: {FARGE[SIK[anenr]]}; flex-shrink: 0;"></span>
        <span style="font: {aarfs}px/1.2 -apple-system, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; color: #6b7280;">{esc(aar)}</span>
      </div>
    </div>
'''

def linje(x1, y1, x2, y2, midt):
    return (f'    <path d="M {x1} {y1} H {midt} V {y2} H {x2}" fill="none" '
            f'stroke="#d7dde4" stroke-width="1.4" stroke-linejoin="round"></path>\n')

def hode(bredde, hoyde_bar, tittel, knapper):
    kn = ''.join(f'<div style="padding: 8px 14px; border: 1px solid #e3e6ea; border-radius: 999px; background: #ffffff; font: 13px -apple-system, \'Segoe UI\', Roboto, Helvetica, Arial, sans-serif; color: #14161a; white-space: nowrap;">{esc(k)}</div>' for k in knapper)
    return f'''  <div style="position: absolute; left: 0; top: 0; width: {bredde}px; height: {hoyde_bar}px; box-sizing: border-box; background: rgba(251, 252, 253, 0.94); border-bottom: 1px solid #e3e6ea; display: flex; align-items: center; gap: 12px; padding: 0 18px; z-index: 5;">
    <div style="font: 600 17px/1.2 'Iowan Old Style', 'Palatino Linotype', Palatino, Georgia, serif; color: #14161a; white-space: nowrap;">{esc(tittel)}</div>
    <div style="flex-grow: 1;"></div>
    <div style="display: flex; align-items: center; gap: 8px;">{kn}</div>
  </div>
'''

def fil(navn, tittel, bredde, hoyde, innhold, bakgrunn='#fbfcfd'):
    return f'''<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
  <style>
    body {{ margin: 0; background: {bakgrunn}; }}
    a {{ color: #1f4e79; }} a:hover {{ color: #14385a; }}
  </style>
</helmet>
<div style="position: relative; width: {bredde}px; height: {hoyde}px; background: {bakgrunn}; overflow: hidden;">
{innhold}</div>
</x-dc>
</body>
</html>
'''

# ---------- 1: kart, PC ----------
W, H = 1440, 900
KB, KH, KOL = 190, 62, 232
BAR = 56
PITCH4 = 78
sentre = {}
for i in range(16): sentre[16+i] = i*PITCH4 + KH/2
for g in (3,2,1,0):
    for i in range(2**g):
        a = 2**g + i
        sentre[a] = (sentre[2*a] + sentre[2*a+1]) / 2
OFF = 90
def yy(a): return sentre[a] - KH/2 - OFF + BAR
def xx(g): return 34 + g*KOL

kort_html, linje_html = '', ''
for g in range(5):
    for i in range(2**g):
        a = 2**g + i
        y = yy(a)
        if y < -KH or y > H: continue
        kort_html += kort(xx(g), y, KB, KH, a)
for g in range(4):
    for i in range(2**g):
        a = 2**g + i
        for f in (2*a, 2*a+1):
            y1, y2 = yy(a)+KH/2, yy(f)+KH/2
            if max(y1, y2) < -40 or min(y1, y2) > H+40: continue
            linje_html += linje(xx(g)+KB, y1, xx(g+1), y2, xx(g)+KB+(KOL-KB)/2)

# antydning av femte kolonne: aner som dukker opp når man drar videre
antyd = ''
for i in range(0, 32):
    a = 32+i
    yv = ((sentre.get(16+i//2, 0)) if False else (i*(PITCH4/2) + KH/2)) - KH/2 - OFF + BAR
    if yv < -KH or yv > H: continue
    antyd += (f'    <div style="position: absolute; left: {xx(5)}px; top: {yv}px; width: {KB}px; height: {KH}px; '
              f'box-sizing: border-box; background: #ffffff; border: 1px dashed #e3e6ea; border-radius: 10px; opacity: 0.5;"></div>\n')

innhold1 = f'''  <svg viewBox="0 0 {W} {H}" width="{W}" height="{H}" style="position: absolute; left: 0; top: 0;">
{linje_html}  </svg>
{antyd}{kort_html}  <div style="position: absolute; right: 0; top: {BAR}px; width: 230px; height: {H-BAR}px; background: linear-gradient(to right, rgba(251, 252, 253, 0), rgba(251, 252, 253, 0.96)); pointer-events: none;"></div>
  <div style="position: absolute; left: 0; bottom: 0; width: {W}px; height: 120px; background: linear-gradient(to bottom, rgba(251, 252, 253, 0), rgba(251, 252, 253, 0.96)); pointer-events: none;"></div>
  <div style="position: absolute; right: 26px; bottom: 22px; display: flex; align-items: center; gap: 9px; padding: 9px 16px; border: 1px solid #e3e6ea; border-radius: 999px; background: rgba(255, 255, 255, 0.94); font: 12.5px -apple-system, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; color: #6b7280;">
    <span style="width: 8px; height: 8px; border-radius: 50%; background: {BLA};"></span>farsslekt
    <span style="width: 8px; height: 8px; border-radius: 50%; background: {TERRA}; margin-left: 8px;"></span>morsslekt
    <span style="margin-left: 12px;">Dra for å se flere ledd</span>
  </div>
{hode(W, BAR, "Anetavlen til Havtor Øvergård", ["Finn person", "Tilbake til meg", "?"])}'''

io.open('Main.dc.html','w',encoding='utf-8').write(fil('Main','Kart', W, H, innhold1))

print('Main.dc.html skrevet')

# ---------- 2: telefon, stående ----------
PW, PH, PBAR = 390, 844, 52
pk_h, pad = 58, 14
bandnavn = [("Meg", [1]), ("Foreldre", [2,3]), ("Besteforeldre", [4,5,6,7]),
            ("Oldeforeldre", [8,9,10,11,12,13,14,15]), ("Tippoldeforeldre", list(range(16,32)))]
innhold2 = ''
y = PH - 26
rader = []
for tittel_b, anerekke in bandnavn:
    bredde_k = 196 if len(anerekke) == 1 else 176
    h_band = 18 + pk_h
    y -= h_band + 20
    rader.append((y, tittel_b, anerekke, bredde_k))
for y0, tittel_b, anerekke, bredde_k in rader:
    if y0 < PBAR - 40: continue
    innhold2 += (f'''  <div style="position: absolute; left: {pad}px; top: {y0}px; font: 10.5px/1 -apple-system, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; letter-spacing: 0.14em; text-transform: uppercase; color: #9aa3ad;">{esc(tittel_b)}</div>\n''')
    x = pad
    for a in anerekke:
        if x > PW: break
        innhold2 += kort(x, y0 + 18, bredde_k, pk_h, a, navnfs=14.5, aarfs=11)
        x += bredde_k + 10
# antydning: neste ledd ligger klart over toppen
innhold2 += f'''  <div style="position: absolute; left: {pad}px; top: {PBAR + 34}px; font: 10.5px/1 -apple-system, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; letter-spacing: 0.14em; text-transform: uppercase; color: #c3cad2;">2 × tippoldeforeldre</div>
'''
for i in range(3):
    innhold2 += (f'''  <div style="position: absolute; left: {pad + i*186}px; top: {PBAR + 52}px; width: 176px; height: {pk_h}px; box-sizing: border-box; background: #ffffff; border: 1px dashed #e3e6ea; border-radius: 10px; opacity: 0.55;"></div>
''')
innhold2 += f'''  <div style="position: absolute; right: 0; top: {PBAR}px; width: 64px; height: {PH-PBAR}px; background: linear-gradient(to right, rgba(251, 252, 253, 0), rgba(251, 252, 253, 0.97)); pointer-events: none;"></div>
  <div style="position: absolute; left: 0; top: {PBAR}px; width: {PW}px; height: 80px; background: linear-gradient(to bottom, rgba(251, 252, 253, 0.97), rgba(251, 252, 253, 0)); pointer-events: none;"></div>
'''
innhold2 += hode(PW, PBAR, "Havtor Øvergård", ["Finn", "?"])
io.open('Telefon.dc.html','w',encoding='utf-8').write(fil('Telefon','Telefon', PW, PH, innhold2))

# ---------- 3: fokusvisning ----------
FW, FH, FBAR = 980, 760, 56
mid_x, mid_y = FW/2, FH/2 + 30
innhold3 = ''
# besteforeldre (4) øverst, foreldre (2), fokus i midten, barn under
rad_bf_y, rad_f_y = FBAR + 34, FBAR + 168
bf = [4,5,6,7]
for i, a in enumerate(bf):
    innhold3 += kort(70 + i*212, rad_bf_y, 190, 62, a, navnfs=14.5)
for i, a in enumerate([2,3]):
    innhold3 += kort(176 + i*424, rad_f_y, 214, 68, a, navnfs=16)
# fokus
innhold3 += f'''  <div style="position: absolute; left: {FW/2-176}px; top: {mid_y-58}px; width: 352px; height: 112px; box-sizing: border-box; background: #ffffff; border: 1px solid #d6dce3; border-left: 5px solid #b9c4cd; border-radius: 14px; box-shadow: 0 6px 22px rgba(20, 30, 50, 0.09); padding: 18px 24px; display: flex; flex-direction: column; justify-content: center; gap: 6px;">
    <div style="font: 600 25px/1.2 'Iowan Old Style', 'Palatino Linotype', Palatino, Georgia, serif; color: #14161a;">Havtor Øvergård</div>
    <div style="display: flex; align-items: center; gap: 8px;">
      <span style="width: 7px; height: 7px; border-radius: 50%; background: #1f7d55;"></span>
      <span style="font: 13px/1.2 -apple-system, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; color: #6b7280;">f. 1965 · Belagt · Tverrelvdalen</span>
    </div>
  </div>
'''
innhold3 += f'''  <div style="position: absolute; left: {FW/2-104}px; top: {mid_y+86}px; width: 208px; height: 52px; box-sizing: border-box; background: #ffffff; border: 1px solid #e3e6ea; border-radius: 10px; padding: 9px 14px; display: flex; flex-direction: column; justify-content: center; gap: 2px; opacity: 0.92;">
    <div style="font: 10.5px/1 -apple-system, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; letter-spacing: 0.14em; text-transform: uppercase; color: #9aa3ad;">Barn</div>
    <div style="font: 14.5px/1.2 'Iowan Old Style', 'Palatino Linotype', Palatino, Georgia, serif; color: #14161a;">Karl Tore Øvergård · f. 1980</div>
  </div>
'''
lin3 = ''
for i, a in enumerate([2,3]):
    lin3 += f'    <path d="M {FW/2 + (-70 if i==0 else 70)} {mid_y-58} V {rad_f_y+68+18} H {283 + i*424} V {rad_f_y+68}" fill="none" stroke="#d7dde4" stroke-width="1.4"></path>\n'
for i, a in enumerate(bf):
    fx = 283 + (0 if i < 2 else 424)
    lin3 += f'    <path d="M {fx + (-60 if i%2==0 else 60)} {rad_f_y} V {rad_bf_y+62+16} H {165 + i*212} V {rad_bf_y+62}" fill="none" stroke="#d7dde4" stroke-width="1.4"></path>\n'
innhold3 = f'''  <svg viewBox="0 0 {FW} {FH}" width="{FW}" height="{FH}" style="position: absolute; left: 0; top: 0;">
{lin3}  </svg>
''' + innhold3
innhold3 += f'''  <div style="position: absolute; left: 0; top: {FBAR}px; width: 54px; height: {FH-FBAR}px; background: linear-gradient(to right, rgba(251, 252, 253, 0.97), rgba(251, 252, 253, 0)); pointer-events: none;"></div>
  <div style="position: absolute; right: 0; top: {FBAR}px; width: 54px; height: {FH-FBAR}px; background: linear-gradient(to left, rgba(251, 252, 253, 0.97), rgba(251, 252, 253, 0)); pointer-events: none;"></div>
  <div style="position: absolute; left: 50%; transform: translateX(-50%); bottom: 20px; padding: 9px 16px; border: 1px solid #e3e6ea; border-radius: 999px; background: rgba(255, 255, 255, 0.94); font: 12.5px -apple-system, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; color: #6b7280;">Dra oppover for å gå et ledd bakover</div>
'''
innhold3 += hode(FW, FBAR, "Anetavlen til Havtor Øvergård", ["Finn person", "Hele tavlen", "?"])
io.open('Fokus.dc.html','w',encoding='utf-8').write(fil('Fokus','Fokus', FW, FH, innhold3))

io.open('canvas.json','w',encoding='utf-8').write('''{
  "artboards": [
    { "file": "Main.dc.html", "x": 0, "y": 0, "w": 1440, "h": 900, "title": "1 · Kart (PC)" },
    { "file": "Telefon.dc.html", "x": 1560, "y": 0, "w": 390, "h": 844, "title": "2 · Kart (telefon)" },
    { "file": "Fokus.dc.html", "x": 2070, "y": 0, "w": 980, "h": 760, "title": "3 · Fokusvisning" }
  ],
  "annotations": [
    { "id": "note-kart", "x": 0, "y": -150, "w": 460, "text": "1 · KART\\nLike store kort, generasjoner i kolonner venstre mot høyre. Du panorerer fritt; nye ledd kommer til syne når du drar utover (de stiplede til høyre). Samme skriftstørrelse overalt." },
    { "id": "note-telefon", "x": 1560, "y": -150, "w": 390, "text": "2 · TELEFON\\nSamme kort, stablet i bånd nedenfra: meg, foreldre, besteforeldre. Hvert bånd dras sidelengs; hele tavlen rulles oppover." },
    { "id": "note-fokus", "x": 2070, "y": -150, "w": 460, "text": "3 · FOKUS\\nÉn person stor i midten, foreldre og besteforeldre rundt i like kort. Drar du oppover, blir foreldrene den nye midten." }
  ],
  "launch": { "view": "canvas" }
}
''')
print('alle skrevet')
