import requests
import re

URL = 'http://raghuveereps.pythonanywhere.com/'

if __name__ == '__main__':
    
    response =  requests.get(URL)
    
    if response.status_code == 200:
        content = response.text 

        regex = '<h4>(.+?)</h4>'

        for title in re.findall(regex, content):
            print(title)