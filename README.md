# IT Start — твой проводник в мир технологий

![Autotests](https://github.com/Andrey76-bit/it-beginner-site/actions/workflows/tests.yml/badge.svg)
![GitHub Pages](https://img.shields.io/badge/demo-online-success)

Мой первый сайт, созданный до обучения в Skillbox. Проект посвящён выбору IT-профессии и помогает новичкам понять, с чего начать.

## 🌐 Демо

Сайт доступен по ссылке:
🔗 https://andrey76-bit.github.io/it-beginner-site/

## 🛠️ Стек

- HTML5 — структура страниц
- CSS3 — стили, адаптивная вёрстка, тёмная тема
- JavaScript — переключатель языка (RU/EN), аккордеоны
- Python + Selenium + pytest — автотесты
- GitHub Actions — CI/CD

## ✨ Что внутри

- **Выбор профессии**: QA, разработчик, DevOps — с описанием каждой.
- **С чего начать**: пошаговый план для новичка.
- **Моя история**: личный путь в IT.
- **Локализация**: переключение языка без перезагрузки страницы.
- **Контакты**: телефон, email, Telegram, MAX.

## 📁 Структура проекта

- **index.html** — Главная страница
- **contacts.html** — Страница контактов
- **admin.html** — Генератор контактов
- **style.css** — Стили
- **script.js** — Логика (локализация, аккордеоны)
- **tests/test_site.py** — 14 автотестов
- **tests/requirements.txt** — Зависимости
- **.github/workflows/tests.yml** — CI/CD: автозапуск тестов
- **README.md** — Этот файл

## 🧪 Автотесты

Проект покрыт автотестами на Python + Selenium + pytest.

**Что проверяется:**

- Открытие главной и страницы контактов
- Заголовки, навигация, секции, футер
- Кнопки переключения языка
- Список контактов (телефон, email, Telegram, MAX)
- Рабочие ссылки tel:, mailto:, t.me
- Отсутствие критических JS-ошибок

**Запуск локально:**

cd tests
pip install -r requirements.txt
pytest test_site.py -v --html=report.html --self-contained-html

**Автозапуск:**
При каждом пуше в main GitHub Actions запускает тесты автоматически.
Статус: https://github.com/Andrey76-bit/it-beginner-site/actions

## 🚀 Как запустить локально

1. Клонируй репозиторий:
git clone https://github.com/Andrey76-bit/it-beginner-site.git

2. Открой файл index.html в браузере — готово.

## 👤 Автор

**Андрей**
GitHub: https://github.com/Andrey76-bit

## 📌 Планы по развитию

- [x] Добавить автотесты (Selenium + pytest)
- [x] Настроить CI/CD через GitHub Actions
- [x] Добавить страницу «Контакты»
- [ ] Добавить favicon
- [ ] Расширить покрытие тестами (переключение языка)
