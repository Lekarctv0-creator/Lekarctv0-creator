INK = '#08080a'
PANEL = '#0b0b0d'
PAPER = '#f4f4f6'
GREY = '#8b8b93'
DIM = '#55555d'
LINE = '#26262b'
SIGNAL = '#ff2d78'
SIGNAL_DEEP = '#2a0c18'

from pathlib import Path

# Neucha (SIL OFL) вшит в каждый SVG: внешние шрифты в <img> не грузятся.
FONT_B64 = (Path(__file__).with_name('font_neucha.b64')).read_text().strip()
SANS = "'Neucha','Ink Free','Segoe UI',system-ui,sans-serif"
MONO = SANS

FULL_WIDTH = 1100
HALF_WIDTH = 540
REGISTER_CYCLE = 10

STYLE = f'''
@font-face{{font-family:'Neucha';src:url(data:font/woff2;base64,{FONT_B64}) format('woff2')}}
text{{font-family:{SANS}}}
.mono{{font-family:{MONO}}}
.fb{{transform-box:fill-box;transform-origin:center}}
.fbl{{transform-box:fill-box;transform-origin:left center}}
.fbb{{transform-box:fill-box;transform-origin:center bottom}}
.pivot{{transform-box:view-box;transform-origin:0 0}}

@keyframes reveal{{from{{transform:translateY(105%)}}to{{transform:none}}}}
@keyframes rise{{from{{opacity:0;transform:translateY(10px)}}to{{opacity:1;transform:none}}}}
@keyframes fade{{from{{opacity:0}}to{{opacity:1}}}}
@keyframes blink{{0%,49%{{opacity:1}}50%,100%{{opacity:0}}}}
@keyframes eq{{0%,100%{{transform:scaleY(.2)}}50%{{transform:scaleY(1)}}}}
@keyframes draw{{from{{stroke-dashoffset:100}}to{{stroke-dashoffset:0}}}}
@keyframes grow{{from{{transform:scaleX(0)}}to{{transform:scaleX(1)}}}}
@keyframes marquee{{to{{transform:translateX(var(--shift))}}}}
@keyframes flicker{{0%,100%{{opacity:.12}}40%{{opacity:.12}}42%{{opacity:1}}78%{{opacity:1}}80%{{opacity:.12}}}}
@keyframes pulse{{0%,100%{{opacity:.25}}50%{{opacity:1}}}}
@keyframes spin{{to{{transform:rotate(360deg)}}}}
@keyframes ripple{{0%{{transform:scale(.7);opacity:0}}15%{{opacity:.6}}100%{{transform:scale(1.8);opacity:0}}}}
@keyframes register{{0%{{transform:translateX(0)}}100%{{transform:translateX(var(--run))}}}}

.reveal{{animation:reveal 1.1s cubic-bezier(.77,0,.18,1) both}}
.rise{{animation:rise .9s cubic-bezier(.19,1,.22,1) both}}
.fade{{animation:fade 1.2s ease both}}
.blink{{animation:blink 1.1s steps(1,end) infinite}}
.eq{{animation:eq 1.5s cubic-bezier(.45,0,.55,1) infinite}}
.draw{{stroke-dasharray:100;animation:draw 1.8s cubic-bezier(.65,0,.35,1) both}}
.grow{{animation:grow 1.4s cubic-bezier(.77,0,.18,1) both}}
.flicker{{animation:flicker 7s steps(1,end) infinite}}
.pulse{{animation:pulse 2.6s ease-in-out infinite}}
.spin{{animation:spin 40s linear infinite}}
.ripple{{animation:ripple 3.4s cubic-bezier(.2,.6,.3,1) infinite}}
.register{{animation:register {REGISTER_CYCLE}s cubic-bezier(.77,0,.18,1) infinite alternate}}
@media (prefers-reduced-motion:reduce){{*{{animation:none!important}}}}
'''
