import base64
from pathlib import Path

PHOTO = base64.b64encode(Path(__file__).with_name('art_photo.jpg').read_bytes()).decode()
SRC = 640  # сторона исходного квадрата


def photo(x, y, w, h):
    size = h - 44                                  # фото целиком, с отступом от рамок
    fx, fy = x + (w - size) / 2, y + (h - size) / 2
    cover = max(w, h) / SRC                        # размытая копия закрывает всю плашку
    bx, by = x + (w - SRC * cover) / 2, y + (h - SRC * cover) / 2
    svg = f'''
<defs>
 <image id="ph" width="{SRC}" height="{SRC}" href="data:image/jpeg;base64,{PHOTO}" xlink:href="data:image/jpeg;base64,{PHOTO}"/>
 <filter id="bl" x="-10%" y="-10%" width="120%" height="120%"><feGaussianBlur stdDeviation="22"/></filter>
 <filter id="ft" x="-10%" y="-10%" width="120%" height="120%"><feGaussianBlur stdDeviation="9"/></filter>
 <radialGradient id="bg-fade" cx=".5" cy=".5" r=".62"><stop offset=".35" stop-color="#fff"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient>
 <mask id="bm" maskUnits="userSpaceOnUse" x="{x}" y="{y}" width="{w}" height="{h}"><rect x="{x}" y="{y}" width="{w}" height="{h}" fill="url(#bg-fade)"/></mask>
 <mask id="fm" maskUnits="userSpaceOnUse" x="{fx - 12}" y="{fy - 12}" width="{size + 24}" height="{size + 24}">
  <rect x="{fx + 7}" y="{fy + 7}" width="{size - 14}" height="{size - 14}" rx="10" fill="#fff" filter="url(#ft)"/>
 </mask>
 <clipPath id="bc"><rect x="{x}" y="{y}" width="{w}" height="{h}"/></clipPath>
</defs>
<g clip-path="url(#bc)" mask="url(#bm)" opacity=".55"><g filter="url(#bl)"><use href="#ph" xlink:href="#ph" transform="translate({bx:.1f} {by:.1f}) scale({cover:.4f})"/></g></g>
<g mask="url(#fm)"><use href="#ph" xlink:href="#ph" transform="translate({fx:.1f} {fy:.1f}) scale({size / SRC:.4f})"/></g>'''
    return svg, ''
