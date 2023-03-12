from bs4 import BeautifulSoup

if __name__ == '__main__':
    with open ('web.html', 'r') as file:
        content = file.read()

        soup = BeautifulSoup(content, 'html.parser')
        
    #1
    # for element in soup.find_all(attrs={'class': 'col-sm-4'}):
    #         #if element.name == 'span':
    #             print(element.text)

    #2
    for element in soup.find_all(class_='col-sm-4'):
        #if element.name == 'span':
            print(element.text)