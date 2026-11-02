from .canvas import text, label, delay, window_keyframes
from .theme import PAPER, GREY, DIM, LINE, SIGNAL, SIGNAL_DEEP, INK

CLI_CYCLE = 13
ROUTER_CYCLE = 8
MODELS = ['claude-opus', 'gpt-5', 'local / qwen']
TARGETS = ['Claude', 'GPT', 'Gemini', 'DeepSeek']

# Иконка приложения PlayLek (mime, base64) — подставляется в build.py.
LOGO = None


def appear(name, start, cycle, end=94):
    return window_keyframes(name, start, end, fade=2.5, lift=4) + f'.{name}{{animation:{name} {cycle}s cubic-bezier(.2,.8,.2,1) infinite}}'


def model_ticker(x, y):
    step = 22
    items = MODELS + MODELS[:1]
    labels = ''.join(text(x, y + i * step, item, 12, SIGNAL, 600, anchor='end', mono=True) for i, item in enumerate(items))
    frames = [f'{100 * i / len(MODELS):.2f}%,{100 * i / len(MODELS) + 26:.2f}%{{transform:translateY({-i * step}px)}}' for i in range(len(MODELS))]
    frames.append(f'100%{{transform:translateY({-len(MODELS) * step}px)}}')
    css = f'@keyframes mtick{{{"".join(frames)}}}.mtick{{animation:mtick 7.5s cubic-bezier(.77,0,.18,1) infinite}}'
    return f'<clipPath id="mclip"><rect x="{x - 140}" y="{y - 14}" width="150" height="19"/></clipPath><g clip-path="url(#mclip)"><g class="mtick">{labels}</g></g>', css


def cli(x, y, w, h):
    prompt = 'добавь авторизацию в API'
    char = 8.4
    widths = ';'.join(f'{i * char:.1f}' for i in range(len(prompt) + 1)) + f';{len(prompt) * char:.1f};0'
    times = ';'.join(f'{.2 * i / len(prompt):.4f}' for i in range(len(prompt) + 1)) + ';.95;1'
    steps = [('read', 'src/api/auth.go', 26), ('lsp', '3 references · AuthService', 36),
             ('mcp', 'github.create_pull_request', 46), ('edit', '+128 −14 · 4 files', 56)]
    css = ''
    rows = []
    for index, (tag, value, start) in enumerate(steps):
        css += appear(f'cl{index}', start, CLI_CYCLE)
        rows.append(f'<g class="cl{index}">{text(x + 24, y + 112 + index * 28, tag.upper(), 11, DIM, 700, mono=True, spacing=1.5)}'
                    f'{text(x + 92, y + 112 + index * 28, value, 13.5, GREY, mono=True)}</g>')
    css += appear('cldone', 68, CLI_CYCLE)
    rows.append(f'<g class="cldone"><rect x="{x + 24}" y="{y + 216}" width="8" height="8" fill="{SIGNAL}"/>'
                f'{text(x + 40, y + 225, "готово за 42s — PR открыт", 13.5, PAPER, 700, mono=True)}</g>')
    ticker, ticker_css = model_ticker(x + w - 20, y + 25)
    css += ticker_css
    svg = f'''
<path d="M{x} {y + 40}H{x + w}" stroke="{LINE}"/>
{label(x + 20, y + 25, 'prime — ~/project', GREY)}
{ticker}
{text(x + 24, y + 74, '›', 16, SIGNAL, 700, mono=True)}
<clipPath id="cli-type"><rect x="{x + 44}" y="{y + 58}" width="0" height="24"><animate attributeName="width" dur="{CLI_CYCLE}s" repeatCount="indefinite" calcMode="discrete" values="{widths}" keyTimes="{times}"/></rect></clipPath>
<g clip-path="url(#cli-type)">{text(x + 44, y + 74, prompt, 14, PAPER, mono=True)}</g>
{"".join(rows)}
<path d="M{x} {y + h - 44}H{x + w}" stroke="{LINE}"/>
{text(x + 24, y + h - 17, '›', 15, GREY, 700, mono=True)}<rect class="blink" x="{x + 42}" y="{y + h - 29}" width="8" height="15" fill="{PAPER}"/>
{label(x + w - 20, y + h - 18, 'ctrl+p palette', DIM, anchor='end', size=10)}'''
    return svg, css


def router(x, y, w, h):
    cy = y + h / 2
    sx, rx, tx = x + 56, x + 214, x + w - 120
    ys = [cy - 54, cy - 18, cy + 18, cy + 54]
    css, paths, boxes, pulses = '', [], [], []
    feed = f'M{sx + 28} {cy}H{rx - 30}'
    for index, (target, ty) in enumerate(zip(TARGETS, ys)):
        route = f'M{rx + 30} {cy}H{rx + 60}V{ty}H{tx}'
        paths.append(f'<path d="{route}" fill="none" stroke="{DIM}"/>')
        start = index / len(TARGETS)
        end = start + .12
        pulses.append(f'<rect x="-3.5" y="-3.5" width="7" height="7" fill="{SIGNAL}" opacity="0"><animateMotion dur="{ROUTER_CYCLE}s" repeatCount="indefinite" path="{route}" keyPoints="0;0;1;1" keyTimes="0;{start:.3f};{end:.3f};1" calcMode="linear"/>'
                      f'<animate attributeName="opacity" dur="{ROUTER_CYCLE}s" repeatCount="indefinite" values="0;0;1;1;0;0" keyTimes="0;{max(start - .001, 0):.3f};{start + .001:.3f};{end:.3f};{end + .002:.3f};1"/></rect>')
        hit = 100 * end
        css += (f'@keyframes rt{index}{{0%,{max(hit - 1, 0):.1f}%{{stroke:{DIM};fill:{INK}}}{hit + 1:.1f}%,{hit + 14:.1f}%{{stroke:{SIGNAL};fill:{SIGNAL_DEEP}}}{hit + 16:.1f}%,100%{{stroke:{DIM};fill:{INK}}}}}'
                f'.rt{index}{{animation:rt{index} {ROUTER_CYCLE}s steps(1,end) infinite}}')
        boxes.append(f'<rect class="rt{index}" x="{tx}" y="{ty - 13}" width="100" height="26" fill="{INK}" stroke="{DIM}"/>'
                     + text(tx + 12, ty + 4.5, target, 12.5, PAPER, mono=True))
    svg = f'''
{"".join(paths)}
<path d="{feed}" fill="none" stroke="{GREY}"/>
<rect x="-3" y="-3" width="6" height="6" fill="{PAPER}"><animateMotion dur="1.6s" repeatCount="indefinite" path="{feed}"/></rect>
<rect x="{sx - 28}" y="{cy - 20}" width="56" height="40" fill="{INK}" stroke="{PAPER}"/>
{text(sx, cy + 4.5, 'TG', 12.5, PAPER, 700, anchor='middle')}
<g transform="rotate(45 {rx} {cy})"><rect x="{rx - 26}" y="{cy - 26}" width="52" height="52" fill="{INK}" stroke="{PAPER}" stroke-width="1.4"/></g>
<g class="fb spin"><g transform="rotate(45 {rx} {cy})"><rect x="{rx - 36}" y="{cy - 36}" width="72" height="72" fill="none" stroke="{DIM}" stroke-dasharray="3 5"/></g></g>
{text(rx, cy + 4, 'ROUTER', 10.5, PAPER, 700, anchor='middle', mono=True, spacing=1)}
{"".join(boxes)}
{"".join(pulses)}'''
    return svg, css


def proxy(x, y, w, h):
    cy = y + h / 2 + 6
    lx, rx = x + 54, x + w - 54
    t0, t1 = lx + 44, rx - 44
    rings = ''.join(f'<rect x="{t0 + (t1 - t0) * i / 9 - 1:.1f}" y="{cy - (32 - abs(i - 4.5) * 3):.1f}" width="2" height="{2 * (32 - abs(i - 4.5) * 3):.1f}" fill="{DIM}" class="pulse" style="{delay(-i * .25)}"/>' for i in range(10))
    span = t1 - t0
    css = (f'@keyframes pkt{{from{{transform:translateX(0);opacity:0}}10%,90%{{opacity:1}}to{{transform:translateX({span:.0f}px);opacity:0}}}}.pkt{{animation:pkt 2.6s linear infinite}}'
           f'@keyframes pktr{{from{{transform:translateX(0);opacity:0}}10%,90%{{opacity:1}}to{{transform:translateX(-{span:.0f}px);opacity:0}}}}.pktr{{animation:pktr 3.2s linear infinite}}')
    packets = ''.join(f'<rect class="pkt" style="{delay(-i * .65)}" x="{t0}" y="{cy - 9}" width="16" height="6" fill="{SIGNAL}"/>' for i in range(4))
    packets += ''.join(f'<rect class="pktr" style="{delay(-i * .8)}" x="{t1 - 12}" y="{cy + 4}" width="12" height="5" fill="{PAPER}"/>' for i in range(4))
    lock_x, lock_y = (t0 + t1) / 2, y + 30
    svg = f'''
<path d="M{t0} {cy - 34}H{t1}M{t0} {cy + 34}H{t1}" stroke="{LINE}"/>
{rings}{packets}
<rect x="{lx - 28}" y="{cy - 28}" width="56" height="56" fill="{INK}" stroke="{PAPER}"/>
<path d="M{lx - 13} {cy}L{lx + 12} {cy - 10}L{lx + 6} {cy + 13}L{lx - 1} {cy + 5}Z" fill="none" stroke="{PAPER}" stroke-width="1.6" stroke-linejoin="round"/>
<rect x="{rx - 28}" y="{cy - 28}" width="56" height="56" fill="{INK}" stroke="{PAPER}"/>
{"".join(f'<path d="M{rx - 15} {cy - 12 + k * 12}H{rx + 9}" stroke="{GREY}"/><rect class="pulse" style="{delay(-k * .7)}" x="{rx + 11}" y="{cy - 14 + k * 12}" width="4" height="4" fill="{SIGNAL}"/>' for k in range(3))}
<rect x="{lock_x - 12}" y="{lock_y}" width="24" height="18" fill="none" stroke="{PAPER}" stroke-width="1.5"/>
<path d="M{lock_x - 7} {lock_y}V{lock_y - 6}A7 7 0 0 1 {lock_x + 7} {lock_y - 6}V{lock_y}" fill="none" stroke="{PAPER}" stroke-width="1.5"/>
<rect x="{lock_x - 2}" y="{lock_y + 6}" width="4" height="6" fill="{SIGNAL}"/>
{label(lock_x, cy + 58, 'mtproto ⇄ websocket', GREY, anchor='middle', size=10)}
{label(lx, cy + 46, 'tg', DIM, anchor='middle', size=9)}{label(rx, cy + 46, 'dc', DIM, anchor='middle', size=9)}'''
    return svg, css


DESK_CYCLE = 12
MENU = ['Музыка', 'Библиотека', 'Статистика', 'PhosmAi', 'Профиль', 'Пульт', 'Настройки', 'Поддержка']
TRACKS = [('Ночной эфир', 'RΛKKΛ', '3:41'), ('Тёмная комната', 'Nova', '2:58'),
          ('Лофт', 'Ksusha', '3:20'), ('Осколки', 'Astra', '4:07')]


def logo(x, y, size, radius, uid):
    mime, data = LOGO
    return (f'<clipPath id="{uid}"><rect x="{x}" y="{y}" width="{size}" height="{size}" rx="{radius}"/></clipPath>'
            f'<image x="{x}" y="{y}" width="{size}" height="{size}" preserveAspectRatio="xMidYMid slice" '
            f'clip-path="url(#{uid})" href="data:{mime};base64,{data}" xlink:href="data:{mime};base64,{data}"/>')


def desktop(x, y, w, h):
    side, step, top = 168, 24, y + 74
    cx = x + side
    css = ''
    frames = [f'{100 * i / len(MENU):.1f}%,{100 * i / len(MENU) + 12:.1f}%{{transform:translateY({i * step}px)}}' for i in range(len(MENU))]
    frames.append('100%{transform:translateY(0)}')
    css += f'@keyframes mpick{{{"".join(frames)}}}.mpick{{animation:mpick {DESK_CYCLE}s cubic-bezier(.77,0,.18,1) infinite}}'
    css += ('@keyframes fill{from{transform:scaleX(0)}to{transform:scaleX(1)}}'
            '.fill{transform-box:fill-box;transform-origin:left center;animation:fill 9s cubic-bezier(.45,0,.55,1) infinite}')
    icons, names = '', ''
    for index, name in enumerate(MENU):
        row = top + index * step
        icons += f'<rect x="{x + 16}" y="{row + 3}" width="10" height="10" rx="2" fill="{PAPER if index == 1 else DIM}"/>'
        names += text(x + 34, row + 12, name, 11.5, PAPER if index == 1 else GREY)
    track = TRACKS[-1]
    rows = ''.join(
        f'<g class="rise" style="{delay(.5 + i * .1)}">'
        f'<rect x="{cx + 16}" y="{y + 96 + i * 26}" width="18" height="18" rx="3" fill="{INK}" stroke="{LINE}"/>'
        f'<rect x="{cx + 19}" y="{y + 99 + i * 26}" width="12" height="12" rx="2" fill="{SIGNAL if i == 0 else DIM}" opacity="{0.85 if i == 0 else 0.4}"/>'
        f'{text(cx + 44, y + 108 + i * 26, name, 11.5, PAPER if i == 0 else GREY)}'
        f'{text(cx + 44, y + 118 + i * 26, artist, 9, DIM, mono=True)}'
        f'{text(x + w - 18, y + 111 + i * 26, length, 9, DIM, anchor="end", mono=True)}</g>'
        for i, (name, artist, length) in enumerate(TRACKS))
    chips = ''.join(
        f'<rect x="{cx + 18 + i * 74}" y="{y + 238}" width="66" height="18" rx="9" fill="none" stroke="{SIGNAL if i == 0 else LINE}"/>'
        + text(cx + 51 + i * 74, y + 250, name, 9, PAPER if i == 0 else DIM, 600, anchor='middle', mono=True)
        for i, name in enumerate(['ночь', 'lofi', 'спорт']))
    bars = ''.join(
        f'<rect class="fb eq" style="{delay(-(k * .23) % 1.5)};animation-duration:{1 + (k % 4) * .2:.1f}s" '
        f'x="{x + w - 156 + k * 6}" y="{y + h - 40 - (3 + k % 5 * 2)}" width="3" height="{8 + k % 5 * 4}" fill="{SIGNAL}"/>'
        for k in range(16))
    svg = f'''
<rect x="{x + 12}" y="{y + 30}" width="{side - 24}" height="38" rx="9" fill="{INK}" stroke="{LINE}"/>
{logo(x + 22, y + 39, 20, 6, 'sb-logo')}
{text(x + 48, y + 48, 'PlayLek', 12.5, PAPER, 800)}{text(x + 48, y + 60, 'Desktop · v1.2.18', 8, DIM, mono=True)}
<rect x="{x + 10}" y="{top - 9}" width="{side - 20}" height="21" rx="7" fill="{SIGNAL}" opacity=".16"/>
<g class="mpick"><rect x="{x + 10}" y="{top - 9}" width="{side - 20}" height="21" rx="7" fill="{SIGNAL}" opacity=".22"/></g>
{icons}{names}
<path d="M{x + 12} {y + h - 52}H{x + side - 12}" stroke="{LINE}"/>
<circle cx="{x + 30}" cy="{y + h - 32}" r="10" fill="{INK}" stroke="{GREY}"/>
{text(x + 46, y + h - 30, '@Oko_Kle', 9, DIM, mono=True)}
<path d="M{cx} {y + 34}V{y + h - 58}" stroke="{LINE}"/>
{label(cx + 18, y + 28, 'библиотека', PAPER, size=10.5)}
{label(x + w - 18, y + 28, 'офлайн · 128 треков', DIM, anchor='end', size=9.5)}
<rect x="{cx + 18}" y="{y + 46}" width="{w - side - 36}" height="22" rx="4" fill="{INK}" stroke="{GREY}"/>
{text(cx + 28, y + 61, 'поиск по трекам и плейлистам', 10, DIM, mono=True)}
{rows}
<path d="M{cx + 18} {y + 214}H{x + w - 18}" stroke="{LINE}"/>
{label(cx + 18, y + 230, 'коллекции', DIM, size=9.5)}
{chips}
<rect x="{cx}" y="{y + h - 58}" width="{w - side}" height="58" fill="{INK}"/>
<path d="M{cx} {y + h - 58}H{x + w}" stroke="{LINE}"/>
<rect x="{cx + 16}" y="{y + h - 48}" width="40" height="40" rx="8" fill="{INK}" stroke="{LINE}"/>
{logo(cx + 17, y + h - 47, 38, 7, 'pb-logo')}
{text(cx + 68, y + h - 34, track[0], 12, PAPER, 700)}
{text(cx + 68, y + h - 21, f'{track[1]} · плейлист «темнота»', 9, DIM, mono=True)}
<rect x="{cx + 68}" y="{y + h - 41}" width="{w - side - 150}" height="2" fill="{LINE}"/>
<rect class="fill" x="{cx + 68}" y="{y + h - 41}" width="{w - side - 150}" height="2" fill="{SIGNAL}"/>
{bars}
<path d="M{x + w - 14} {y + h - 30}V{y + h - 46}M{x + w - 20} {y + h - 30}V{y + h - 40}M{x + w - 8} {y + h - 30}V{y + h - 40}" stroke="{GREY}" stroke-width="1.4"/>'''
    return svg, css
