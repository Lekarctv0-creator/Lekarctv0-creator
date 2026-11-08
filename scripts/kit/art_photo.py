import base64
from pathlib import Path

PHOTO = base64.b64encode(Path(__file__).with_name('art_photo.jpg').read_bytes()).decode()
SRC = 640  # сторона встроенного квадратного фото


def photo(x, y, w, h):
    size = h - 20                                   # фото целиком, в тонкой рамке
    fx, fy = x + w - size - 79, y + 10
    cover = max(w, h) / SRC                         # размытая копия за рамкой — лёгкая дымка
    bx, by = x + (w - SRC * cover) / 2, y + (h - SRC * cover) / 2
    svg = f'''
<defs>
 <image id="ph" width="{SRC}" height="{SRC}" href="data:image/jpeg;base64,{PHOTO}" xlink:href="data:image/jpeg;base64,{PHOTO}"/>
 <filter id="bl" x="-10%" y="-10%" width="120%" height="120%"><feGaussianBlur stdDeviation="26"/></filter>
 <radialGradient id="bg-fade" cx=".62" cy=".5" r=".6"><stop offset=".25" stop-color="#fff"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient>
 <mask id="bm" maskUnits="userSpaceOnUse" x="{x}" y="{y}" width="{w}" height="{h}"><rect x="{x}" y="{y}" width="{w}" height="{h}" fill="url(#bg-fade)"/></mask>
 <clipPath id="bc"><rect x="{x}" y="{y}" width="{w}" height="{h}"/></clipPath>
 <clipPath id="win"><rect x="{fx}" y="{fy}" width="{size}" height="{size}" rx="3"/></clipPath>
</defs>
<g clip-path="url(#bc)" mask="url(#bm)" opacity=".4"><g filter="url(#bl)"><use href="#ph" xlink:href="#ph" transform="translate({bx:.1f} {by:.1f}) scale({cover:.4f})"/></g></g>
<g clip-path="url(#win)"><use href="#ph" xlink:href="#ph" transform="translate({fx} {fy}) scale({size / SRC:.4f})"/></g>
<rect x="{fx}" y="{fy}" width="{size}" height="{size}" rx="3" fill="none" stroke="#f4f4f6" stroke-opacity=".6" stroke-width="1.5"/>'''
    return svg, ''
