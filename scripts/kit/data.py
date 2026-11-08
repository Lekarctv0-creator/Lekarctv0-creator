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
    ('link-telegram', 'Telegram', '@Oko_Kleima', 'https://t.me/Oko_Kleima'),
    ('link-github', 'GitHub', 'github.com/Lekarctv0-creator', 'https://github.com/Lekarctv0-creator'),
    ('link-playlek', 'PlayLek', 'релизы для Android и ПК', 'https://github.com/Lekarctv0-creator/PlayLek/releases'),
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
        alt='PlayLek Desktop — плеер для Windows на Kotlin и Compose: библиотека, очередь, текст песни, трей, мини-плеер, звук через VLC, треки из Telegram.'),
    'playlek': dict(
        kind='PLAYLEK · KOTLIN', title='PlayLek', art='telegram',
        lines=['Музыка из Telegram на телефоне: поиск,', 'плейлисты, обложки и управление с трея.', 'Избранное, статистика и скорость — общие с ПК.'],
        chips=['Kotlin', 'Compose', 'Telegram'],
        cta='', url_label='28 релизов · v0.2.19',
        url=None,
        alt='PlayLek — музыка из Telegram на Android: поиск, плейлисты, обложки, управление с трея, общие с ПК избранное и статистика. Kotlin, Compose.'),
    'support': dict(
        kind='TELEGRAM BOT · CLOUDFLARE', title='PlayLek Support', art='telegram',
        lines=['Бот поддержки PlayLek: обращения из приложения', 'и из Telegram идут в один чат.', 'Без своего сервера — Cloudflare Worker.'],
        chips=['JavaScript', 'Workers', 'Telegram'],
        cta='', url=None, url_label='@PlayLek_Support_bot',
        alt='PlayLek Support — бот поддержки PlayLek на Cloudflare Worker: обращения из приложения и из Telegram в одном чате.'),
    'miniapp': dict(
        kind='TELEGRAM MINI APP · JS', title='Mini App', art='portfolio',
        lines=['AI Generator Pro: мини-приложение', 'с генерациями, статусами и оплатой.'],
        chips=['JavaScript', 'HTML', 'Telegram'],
        cta='', url=None, url_label='v2.0 · mini app',
        alt='Mini App — AI Generator Pro: Telegram-мини-приложение с генерациями, статусами и оплатой.'),
    'batinok': dict(
        kind='TELEGRAM BOT · PYTHON', title='Temnica Morali', art='router',
        lines=['Telegram-бот на Python: база данных,', 'сценарии и модерация.'],
        chips=['Python', 'aiogram', 'SQLite'],
        cta='', url=None, url_label='бот · python',
        alt='Temnica Morali — Telegram-бот на Python: база данных, сценарии и модерация.'),
}

LAYOUT = [
    ('hero',),
    ('links',),
    ('stats',),
    ('section', 'desktop'),
    ('wide', 'playlek-desktop'),
    ('wide', 'playlek'),
    ('section', 'public'),
    ('wide', 'support'),
    ('wide', 'miniapp'),
    ('wide', 'batinok'),
    ('footer',),
]
