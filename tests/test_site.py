import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


BASE_URL = "https://andrey76-bit.github.io/it-beginner-site"


@pytest.fixture(scope="module")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")

    service = Service(executable_path="/usr/bin/chromedriver")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()


def test_01_main_page_opens(driver):
    """Главная страница открывается и загружается"""
    driver.get(BASE_URL)
    time.sleep(3)
    assert driver.title != "", "Заголовок страницы пустой"
    assert "IT Start" in driver.title, f"Неожиданный заголовок: {driver.title}"


def test_02_header_title(driver):
    """Заголовок h1 содержит 'IT Start'"""
    driver.get(BASE_URL)
    time.sleep(2)
    h1 = driver.find_element(By.TAG_NAME, "h1")
    assert "IT Start" in h1.text, f"Заголовок не найден, получено: {h1.text}"


def test_03_navigation_exists(driver):
    """Навигация .main-nav присутствует"""
    driver.get(BASE_URL)
    time.sleep(2)
    nav = driver.find_elements(By.CLASS_NAME, "main-nav")
    assert len(nav) > 0, "Навигация не найдена"


def test_04_nav_links(driver):
    """В навигации есть ссылки на разделы и контакты"""
    driver.get(BASE_URL)
    time.sleep(2)
    nav = driver.find_element(By.CLASS_NAME, "main-nav")
    links = nav.find_elements(By.TAG_NAME, "a")
    link_texts = [link.text for link in links]
    assert len(links) >= 5, f"Ожидалось минимум 5 ссылок, найдено: {len(links)}"
    assert any("Профессии" in text for text in link_texts), "Ссылка 'Профессии' не найдена"
    assert any("Контакты" in text for text in link_texts), "Ссылка 'Контакты' не найдена"


def test_05_language_buttons(driver):
    """Кнопки переключения языка есть"""
    driver.get(BASE_URL)
    time.sleep(2)
    buttons = driver.find_elements(By.TAG_NAME, "button")
    assert len(buttons) >= 2, f"Кнопки языка не найдены, всего кнопок: {len(buttons)}"


def test_06_sections_exist(driver):
    """Все 4 секции с id присутствуют"""
    driver.get(BASE_URL)
    time.sleep(2)
    for section_id in ["professions", "start", "history", "knowledge"]:
        section = driver.find_elements(By.ID, section_id)
        assert len(section) > 0, f"Секция #{section_id} не найдена"


def test_07_footer_exists(driver):
    """Футер присутствует"""
    driver.get(BASE_URL)
    time.sleep(2)
    footer = driver.find_elements(By.TAG_NAME, "footer")
    assert len(footer) > 0, "Футер не найден"


def test_08_contacts_page_opens(driver):
    """Страница контактов открывается"""
    driver.get(BASE_URL + "/contacts.html")
    time.sleep(3)
    h1 = driver.find_element(By.TAG_NAME, "h1")
    assert "Контакты" in h1.text, f"Заголовок контактов не найден: {h1.text}"


def test_09_contacts_list_present(driver):
    """Список контактов присутствует и содержит записи"""
    driver.get(BASE_URL + "/contacts.html")
    time.sleep(3)
    contacts = driver.find_elements(By.CLASS_NAME, "contacts-list")
    assert len(contacts) > 0, "Список контактов не найден"
    items = contacts[0].find_elements(By.TAG_NAME, "li")
    assert len(items) >= 4, f"Ожидалось минимум 4 контакта, найдено: {len(items)}"


def test_10_contacts_data_correct(driver):
    """На странице контактов есть телефон, email, Telegram, MAX"""
    driver.get(BASE_URL + "/contacts.html")
    time.sleep(3)
    page_text = driver.find_element(By.TAG_NAME, "body").text
    assert "+7 978 579-12-00" in page_text, "Телефон не найден"
    assert "nata37971@gmail.com" in page_text, "Email не найден"
    assert "@Andrey20Andre" in page_text, "Telegram не найден"
    assert "MAX" in page_text, "Блок MAX не найден"


def test_11_contacts_links_work(driver):
    """Ссылки на телефон и email корректны"""
    driver.get(BASE_URL + "/contacts.html")
    time.sleep(3)
    tel_link = driver.find_elements(By.XPATH, "//a[starts-with(@href, 'tel:')]")
    mail_link = driver.find_elements(By.XPATH, "//a[starts-with(@href, 'mailto:')]")
    tg_link = driver.find_elements(By.XPATH, "//a[contains(@href, 't.me')]")
    assert len(tel_link) >= 1, "Ссылка tel: не найдена"
    assert len(mail_link) >= 1, "Ссылка mailto: не найдена"
    assert len(tg_link) >= 1, "Ссылка t.me не найдена"


def test_12_no_js_errors_main(driver):
    """Консоль главной страницы без критических ошибок (кроме favicon)"""
    driver.get(BASE_URL)
    time.sleep(3)
    logs = driver.get_log('browser')
    severe = [
        log for log in logs
        if log['level'] == 'SEVERE' and 'favicon' not in log['message']
    ]
    for log in severe:
        print(f"JS ERROR: {log['message']}")
    assert len(severe) == 0, f"Найдено {len(severe)} критических JS-ошибок"
