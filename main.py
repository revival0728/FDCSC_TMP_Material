import requests as rqs
from bs4 import BeautifulSoup as bsp

blocks = {  # texts // str
    'title': '', 
    'content': '', #0
    'input': '', #1
    'output': '', #2
    'sample_input': '', #3
    'sample_output': '', #4
    'hint': ''
}

def main():
    pid = 'a751'
    url = 'http://203.64.191.163/ShowProblem?problemid={}'
    
    response = rqs.get(url.format(pid))
    html = bsp(response.text, 'html.parser')
    content = html.find_all(name='div', attrs={'class', 'problembox'})
    
    print(content[5])

if __name__ == '__main__':
    main()