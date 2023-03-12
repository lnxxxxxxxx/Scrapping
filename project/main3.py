import requests
import re

URL = 'http://raghuveereps.pythonanywhere.com/'

if __name__ == '__main__':
    
    #trabajando de forma local, un archivo ya obtenido
    with open('web.html', 'r') as file:
        content = file.read()

        regex = '<h4>(.+?)</h4>'

        for title in re.findall(regex, content):
            print(title)