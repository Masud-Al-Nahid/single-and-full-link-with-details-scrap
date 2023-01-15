import requests
from bs4 import BeautifulSoup as bs

i = 1
while i<=50:

    url = f'https://books.toscrape.com/catalogue/page-{i}.html'

    s = requests.Session()
    res = s.get(url)
    data =res.text
    soup =bs(data, 'html.parser')
    page_div =soup.find('div', {'class': 'col-sm-8 col-md-9'})
    links = page_div.findAll('h3')
    for link in links:
        all_link = link.find('a').get('href')
        main_link ='https://books.toscrape.com/catalogue/'
        full_link= main_link+all_link
        with open('all_link_data.txt', 'a') as file:
            file.writelines(full_link+'\n')
    i+=1

        



