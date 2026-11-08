from .canvas import document, frame, text, label, delay, arrow
from .theme import FULL_WIDTH, PAPER, GREY, SIGNAL, INK

HEIGHT = 196


def build(title, numbers, button):
    body = frame(FULL_WIDTH, HEIGHT, strip=False)
    body += label(28, 38, 'проект', SIGNAL)
    body += f'<g class="rise" style="{delay(.1)}">{text(28, 84, title, 32, PAPER, 800)}</g>'
    for i, (big, small) in enumerate(numbers):
        x = 28 + i * 205
        body += f'<g class="rise" style="{delay(.25 + i * .12)}">{text(x, 148, big, 46, PAPER, 800, spacing=3)}</g>'
        body += label(x + 2, 172, small, GREY, size=10.5)
        if i:
            body += f'<path d="M{x - 18} 112V176" stroke="#26262b"/>'
    bx = FULL_WIDTH - 28 - 150
    body += (f'<rect x="{bx}" y="112" width="150" height="48" rx="6" fill="{SIGNAL}"/>'
             + text(bx + 28, 143, button, 19, INK, 800)
             + f'<g transform="translate({bx + 122} 136)">{arrow(0, 0, 8, INK, 2)}</g>')
    return document(FULL_WIDTH, HEIGHT, body, f'{title}: ' + ', '.join(f'{b} {s}' for b, s in numbers))
