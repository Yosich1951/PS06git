"""
На сайте
https://www.divan.ru/category/svet
найти наименования, цену и ссылки светильников.
Напиши альтернативный вариант кода на Python

"""
import requests
from bs4 import BeautifulSoup

# URL страницы с светильниками
url = "https://www.divan.ru/category/svet"

# Заголовки для запроса, чтобы имитировать браузер
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}
# Выполнение GET-запроса к странице
response = requests.get(url, headers=headers)
print(f"Статус {response.status_code}")
# Проверка успешности запроса
if response.status_code == 200:
    # Парсинг HTML-контента страницы
    soup = BeautifulSoup(response.content, 'html.parser')
    # Пример нахождения элементов светильников (зависит от структуры HTML)
    items = soup.find_all('div', class_='lsooF')
    # print(items)
    dict = {}
    for item in items:
        # Нахождение наименования светильника
        name = item.find('a', class_='ui-GPFV8 qUioe ProductName ActiveProduct').text.strip()

        # Нахождение цены светильника
        price = item.find('span', class_='ui-LD-ZU KIkOH').text.strip()
        # print(f"Price {price}")
        # Нахождение ссылки на светильник
        link = item.find('a', class_='ui-GPFV8 qUioe ProductName ActiveProduct')['href']
        # print(f"Ссылка {link}")
        full_link = f"https://www.divan.ru{link}"
        # Вывод информации
        print(f"Название: {name}")
        print(f"Цена: {price}")
        print(f"Ссылка: {full_link}")
        print()
    else:
        print("Не удалось получить данные с сайта")