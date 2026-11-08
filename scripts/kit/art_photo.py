import base64
from pathlib import Path

from .theme import SIGNAL

# Фото уже обработано (ч/б, розовые тени); здесь только виньетка из маски.
PHOTO = base64.b64encode(Path(__file__).with_name('art_photo.jpg').read_bytes()).decode()


def photo(x, y, w, h):
    svg = f'''
<defs>
 <radialGradient id="vg" cx=".6" cy=".46" r=".62"><stop offset="0" stop-color="#fff"/><stop offset=".5" stop-color="#fff"/><stop offset=".78" stop-color="#fff" stop-opacity=".45"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient>
 <linearGradient id="vl" x1="0" x2="1"><stop offset="0" stop-color="#000"/><stop offset=".25" stop-color="#000" stop-opacity="0"/></linearGradient>
 <mask id="vm" maskUnits="userSpaceOnUse" x="{x}" y="{y}" width="{w}" height="{h}">
  <rect x="{x}" y="{y}" width="{w}" height="{h}" fill="url(#vg)"/>
  <rect x="{x}" y="{y}" width="{w}" height="{h}" fill="url(#vl)"/>
  <rect x="{x}" y="{y}" width="{w}" height="{h}" fill="url(#vr)"/>
  <rect x="{x}" y="{y}" width="{w}" height="{h}" fill="url(#vt)"/>
 </mask>
 <linearGradient id="vr" x1="0" x2="1"><stop offset=".72" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000"/></linearGradient>
 <linearGradient id="vt" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#000"/><stop offset=".2" stop-color="#000" stop-opacity="0"/><stop offset=".72" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000"/></linearGradient>
 <radialGradient id="pg"><stop offset="0" stop-color="{SIGNAL}" stop-opacity=".5"/><stop offset="1" stop-color="{SIGNAL}" stop-opacity="0"/></radialGradient>
</defs>
<ellipse class="pulse fb" cx="{x + w * .6}" cy="{y + h * .5}" rx="{w * .5}" ry="{h * .55}" fill="url(#pg)"/>
<g mask="url(#vm)"><image x="{x}" y="{y}" width="{w}" height="{h}" preserveAspectRatio="xMidYMid slice" href="data:image/jpeg;base64,{PHOTO}" xlink:href="data:image/jpeg;base64,{PHOTO}"/></g>'''
    return svg, ''
