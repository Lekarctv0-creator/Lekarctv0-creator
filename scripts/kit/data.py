from .theme import SIGNAL, PAPER, GREY, DIM

REPO_TOTAL = 3
LANGUAGE_COUNT = 4
LANGUAGES = [
    ('Kotlin', 3, SIGNAL),
    ('Rust', 3, PAPER),
    ('Python', 2, GREY),
    ('HTML', 1, DIM),
]
HIGHLIGHTS = [
    (LANGUAGE_COUNT, '', 'языка', 'Kotlin · Rust · Python · HTML'),
    (28, '', 'релизов PlayLek', 'android 0.2.19 + pc 1.3.1'),
    (3, '', 'публичных проекта', 'PlayLek · Mini App · бот'),
]
STATS_META = 'github · ноябрь 2026'

LINKS = [
    ('link-ideas', 'Готов к идеям', 'напиши в Telegram', 'https://t.me/Oko_Kleima'),
    ('link-code', 'Чистый код', 'Rust · Kotlin · Python', 'https://github.com/Lekarctv0-creator'),
    ('link-ui', 'Красивый UI/UX', 'тёмные темы и анимации', 'https://lekarctv0-creator.github.io/PlayLek/'),
    ('link-playlek', 'Создал PlayLek', 'релизы для Android и ПК', 'https://github.com/Lekarctv0-creator/PlayLek/releases/latest'),
]

SECTIONS = {
    'desktop': ('01', 'Десктоп и музыка', 'Плееры для Windows и Android: тёмный UI, трей, текст песни, «слушать вместе».', '02 ПРОЕКТА'),
    'public': ('02', 'Публичные проекты', 'Мини-приложения и боты: то, что можно открыть и потрогать.', '03 ПРОЕКТА'),
}

PROJECTS = {
    'playlek-desktop': dict(
        kind='DESKTOP · RUST', title='PlayLek Desktop', title_size=56, art='desktop',
        lines=['Плеер для Windows на Rust: библиотека, очередь,', 'текст песни, трей, мини-плеер и «слушать вместе».', 'Треки — из Telegram, обновления — сами.'],
        chips=['Rust', 'Slint', 'TDLib'],
        cta='открыть релизы', url_label='PC 1.3.1 · Android 0.2.19',
        url='https://github.com/Lekarctv0-creator/PlayLek/releases',
        alt='PlayLek Desktop — плеер для Windows на Rust: библиотека, очередь, текст песни, трей, мини-плеер, «слушать вместе», треки из Telegram.'),
    'playlek': dict(
        kind='PLAYLEK · KOTLIN', title='PlayLek', art='telegram',
        lines=['Музыка из Telegram на телефоне: поиск,', 'плейлисты, обложки и управление с трея.', 'Избранное, статистика и скорость — общие с ПК.'],
        chips=['Kotlin', 'Compose', 'Telegram'],
        cta='', url_label='28 релизов · v0.2.19',
        url=None,
        alt='PlayLek — музыка из Telegram на Android: поиск, плейлисты, обложки, общие с ПК избранное и статистика. Kotlin, Compose.'),
    'support': dict(
        kind='TELEGRAM BOT · CLOUDFLARE', title='PlayLek Support', art='telegram',
        lines=['Бот поддержки PlayLek: обращения из приложения', 'и из Telegram идут в один чат.', 'Без своего сервера — Cloudflare Worker.'],
        chips=['JavaScript', 'Workers', 'Telegram'],
        cta='', url=None, url_label='@PlayLek_Support_bot',
        alt='PlayLek Support — бот поддержки PlayLek на Cloudflare Worker: обращения из приложения и из Telegram в одном чате.'),
}

LAYOUT = [
    ('hero',),
    ('links',),
    ('wide', 'playlek-desktop'),
    ('wide', 'playlek'),
    ('footer',),
]
