import requests
from datetime import datetime
from bs4 import BeautifulSoup

URL = 'https://news.google.com/topics/CAAqLQgKIidDQkFTRndvSkwyMHZNR1ptZHpWbUVnWmxjeTAwTVRrYUFrRlNLQUFQAQ?hl=es-419&gl=AR&ceid=AR%3Aes-419'

if __name__ == '__main__':

    #Cron


    response = requests.get(URL)

    if response.status_code == 200:
        content = response.text

        soup = BeautifulSoup(content, 'html.parser')

        #fecha de cuando fue creado
        now = datetime.now().strftime('%d_%m_%Y %H_%M')
        print(now)
        #new_dia_mes_año.txt
        with open(f'news/news_{now}.txt', 'w+') as file:
            for element in soup.find_all('h3', class_='ipQwMb ekueJc gEATFF RD0gLb', limit= 10):
                title = element.a.text
                file.write(title + '\n')

    print('Archivo generado de forma exitosa')