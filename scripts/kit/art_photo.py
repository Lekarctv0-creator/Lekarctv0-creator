import base64
from pathlib import Path

PHOTO = base64.b64encode(Path(__file__).with_name('art_photo.jpg').read_bytes()).decode()
HAND = base64.b64encode(Path(__file__).with_name('art_hand.png').read_bytes()).decode()
SRC = 640                      # сторона встроенного фото
HAND_AT = (61, 263, 119, 123)  # вырезка руки в координатах оригинала 1080x1080: x, y, w, h


def photo(x, y, w, h):
    size = 560                                  # фото крупнее окна, «ближе к зрителю»
    k = size / 1080
    ww, wh = 300, h - 24                        # окно-рамка
    wx, wy = x + w * .56 - ww / 2, y + 12
    px, py = wx - 62 * k - 0, wy + wh * .40 - 330 * k   # левый край окна проходит через середину руки
    hx, hy, hw, hh = HAND_AT
    grow = 1.1                                  # рука чуть крупнее: эффект выхода из кадра
    hdx, hdy = hx * k - (grow - 1) * hw * k / 2, hy * k - (grow - 1) * hh * k / 2
    cover = max(w, h) / SRC
    bx, by = x + (w - SRC * cover) / 2, y + (h - SRC * cover) / 2
    svg = f'''
<defs>
 <image id="ph" width="{SRC}" height="{SRC}" href="data:image/jpeg;base64,{PHOTO}" xlink:href="data:image/jpeg;base64,{PHOTO}"/>
 <filter id="bl" x="-10%" y="-10%" width="120%" height="120%"><feGaussianBlur stdDeviation="22"/></filter>
 <filter id="sh" x="-30%" y="-30%" width="160%" height="170%"><feDropShadow dx="-3" dy="5" stdDeviation="4" flood-color="#000" flood-opacity=".75"/></filter>
 <radialGradient id="bg-fade" cx=".5" cy=".5" r=".62"><stop offset=".3" stop-color="#fff"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient>
 <mask id="bm" maskUnits="userSpaceOnUse" x="{x}" y="{y}" width="{w}" height="{h}"><rect x="{x}" y="{y}" width="{w}" height="{h}" fill="url(#bg-fade)"/></mask>
 <clipPath id="bc"><rect x="{x}" y="{y}" width="{w}" height="{h}"/></clipPath>
 <clipPath id="win"><rect x="{wx:.1f}" y="{wy:.1f}" width="{ww}" height="{wh}" rx="3"/></clipPath>
</defs>
<g clip-path="url(#bc)" mask="url(#bm)" opacity=".45"><g filter="url(#bl)"><use href="#ph" xlink:href="#ph" transform="translate({bx:.1f} {by:.1f}) scale({cover:.4f})"/></g></g>
<g clip-path="url(#win)"><use href="#ph" xlink:href="#ph" transform="translate({px:.1f} {py:.1f}) scale({size / SRC:.4f})"/></g>
<rect x="{wx:.1f}" y="{wy:.1f}" width="{ww}" height="{wh}" rx="3" fill="none" stroke="#f4f4f6" stroke-opacity=".55" stroke-width="1.5"/>
<g filter="url(#sh)"><image x="{px + hdx:.1f}" y="{py + hdy:.1f}" width="{hw * k * grow:.1f}" height="{hh * k * grow:.1f}" href="data:image/png;base64,{HAND}" xlink:href="data:image/png;base64,{HAND}"/></g>'''
    return svg, ''
