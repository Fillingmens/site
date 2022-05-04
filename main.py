import json
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from attr import field
text = ''

with open('main.json', 'r', encoding='utf-8') as f:
    reader = json.load(f)
def click():
    name = form.name.text()
    form.text.setHtml("gg")
    print(name)
    if  name == '#' or name == '#Сам себе програмист':
        form.text.setHtml('''
        #Сам себе програмист

        260 страниц
        
        жанр иследовательский
        
        
        ''')
        
    

    

print(reader['res'])


Form, Window = uic.loadUiType("ui.ui")

app = QApplication([])
window = Window()
form = Form()

form.setupUi(window)
window.show()

form.search.clicked.connect(click)

app.exec()

