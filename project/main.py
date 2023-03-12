import requests

URL = 'http://raghuveereps.pythonanywhere.com/'

if __name__ == '__main__':
    
    response =  requests.get(URL)
    
    if response.status_code == 200:
        content = response.text 

        # with open('web.html', 'w+') as file:
        #     file.write(content)   #leo y creo el archivo


        regexa = '<h4>'
        regexb = '</h4>'

        for line in content.split('\n'):
            if regexa in line:
                start = line.find(regexa) + len(regexa)
                end = line.find(regexb)
                title = line[start:end]
                print(title)