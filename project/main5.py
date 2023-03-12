from bs4 import BeautifulSoup

if __name__ == '__main__':
    with open ('web.html', 'r') as file:
        content = file.read()

        soup = BeautifulSoup(content, 'html.parser')
        
        #find
        # for element in soup.find_all('div'): #solo ubusca div
        #busca div con clase que se llame modal 
        for element in soup.find_all('div', {'class': 'modal'}):
           # print(element, '\n') #\n para separarlos por un renglon
            #  div = element.find('div')
            #  span = element.find('span')

            div = element.div
            span = element.span
            print(div.text, span.text) #el .text es para ver el contenido de la etiqueta
