"""Є вiдкритий API NASA який дозволяє за певними параметрами
отримати данi у виглядi JSON про фото зробленi ровером “Curiosity” на Марсi.
Серед цих даних є посилання на фото якi потрiбно розпарсити
i потiм за допомогою додаткових запитiв скачати i зберiгти цi фото як
локальнi файли mars_photo1.jpg , mars_photo2.jpg .
Завдання потрiбно зробити використовуючи модуль requests"""

import requests

url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}

response = requests.get(url, params=params)
if response.status_code == 200:
    data = response.json()
    photos = data.get('photos', [])

    for idx, photo in enumerate(photos):
        img_url = photo.get('img_src')
        if img_url:
            img_data = requests.get(img_url).content
            file_name = f'mars_photo{idx + 1}.jpg'
            with open(file_name, 'wb') as f:
                f.write(img_data)
            print(f'Збережено: {file_name}')
else:
    print('Помилка. Статус-код:', response.status_code)