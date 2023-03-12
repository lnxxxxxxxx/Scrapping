from bs4 import BeautifulSoup

if __name__ == '__main__':
    with open ('web.html', 'r') as file:
        content = file.read()

        soup = BeautifulSoup(content, 'html.parser')
        # print(soup.head)
        # print(type(soup.head))

        title = soup.find('title')
        if title: 
            print(title)

            print(type(title))
            print(title.name)

            print(title.text)
            print(title.get_text())