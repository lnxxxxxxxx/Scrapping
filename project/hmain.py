from bs4 import BeautifulSoup

if __name__ == '__main__':
    with open ('web.html', 'r') as file:
        content = file.read()

        soup = BeautifulSoup(content, 'html.parser')
        
    div = soup.find('div', {'title': 'hola'})
    #div = soup.find('div', string='Download Template')
    print(div.text) #list

    #next_sibling #previous_sibling
    #next_siblings #previous_siblings
     # .parent.parent al elemento padre de nuestra etiqueta
    span = soup.find('span')
    #parents
    for parent in span.parents:
        print(parent.name)
    
#   Atributo	Descripción
# parent	Elemento padre
# parents	Listado de elementos padres hasta el nível top
# next_sibling	Siguiente elemento después del elemento actual
# next_siblings	Listado de elementos después del elemento actual
# previous_sibling	Elemento anteriot al elemento actual
# previous_siblings	Listado de elemento anteriores al elemento actual
# contents	Listado de todos los elementos hijos
# children	Generador de todos los elementos hijos
# descendants	Generador de todos los elementos hijos de forma recursiva""