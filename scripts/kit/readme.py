from html import escape

PREVIEW = '''<!doctype html>
<html lang="ru"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Lekarctv0-creator — preview</title>
<style>
:root{color-scheme:dark}
body{margin:0;background:#0d1117;color:#e6edf3;font:16px/1.5 -apple-system,"Segoe UI",sans-serif}
a{color:#e6edf3}
.wrap{max-width:1280px;margin:0 auto;padding:32px 24px;display:flex;gap:24px;align-items:flex-start}
aside{width:296px;flex:none}
.side{background:#161b22;border:1px solid #30363d;border-radius:6px;padding:16px}
.avatar{width:100%;border-radius:50%;border:1px solid #30363d;background:#010409;display:block}
h1{font-size:24px;margin:12px 0 0;font-weight:600}
.nick{color:#7d8590;font-size:20px;font-weight:300;margin:0 0 12px}
.bio{font-size:14px;color:#e6edf3;margin:0 0 12px}
.btn{display:block;text-align:center;background:#21262d;border:1px solid #30363d;border-radius:6px;padding:5px 16px;font-size:14px;font-weight:500;text-decoration:none;color:#e6edf3}
.btn:hover{background:#30363d}
main{flex:1;min-width:0}
.tabs{display:flex;gap:8px;border-bottom:1px solid #30363d;margin-bottom:16px;font-size:14px}
.tabs span{padding:8px 12px;color:#7d8590}
.tabs .on{color:#e6edf3;border-bottom:2px solid #ff2d78;font-weight:600}
.readme{background:#161b22;border:1px solid #30363d;border-radius:6px}
.rhead{padding:12px 16px;border-bottom:1px solid #30363d;font-size:14px;color:#7d8590}
.rbody{padding:16px}
img{max-width:100%;height:auto}
p{margin:0 0 16px}
@media(max-width:900px){.wrap{flex-direction:column}aside{width:100%}}
</style>
<div class="wrap">
<aside><div class="side">
<img class="avatar" src="./assets/avatar.png" alt="аватар — TSUKI | ✞ RΛKKΛ ✞">
<h1>TSUKI | ✞ RΛKKΛ ✞</h1>
<p class="nick">Lekarctv0-creator</p>
<p class="bio">✞ TSUKI | RΛKKΛ ✞ · dark-mode dev · код и музыка в темноте · PlayLek · Python · Kotlin · Rust</p>
<a class="btn" href="https://t.me/Oko_Kleima" style="margin-bottom:8px">Telegram — @Oko_Kleima</a>
<a class="btn" href="#">Follow</a>
</div></aside>
<main>
<div class="tabs"><span class="on">Overview</span><span>Repositories</span><span>Projects</span><span>Packages</span><span>Stars</span></div>
<div class="readme"><div class="rhead">README.md</div><div class="rbody">@@BODY@@</div></div>
</main>
</div></html>'''


def image(src, alt, width):
    return f'<img src="{src}" width="{width}" alt="{escape(alt, quote=True)}" />'


def linked(href, src, alt, width):
    return f'<a href="{href}">{image(src, alt, width)}</a>'


def block(*items):
    inner = '\n  '.join(items)
    return f'<p align="center">\n  {inner}\n</p>'


def render(blocks):
    return '\n\n'.join(blocks) + '\n'


def preview(readme):
    return PREVIEW.replace('@@BODY@@', readme)
