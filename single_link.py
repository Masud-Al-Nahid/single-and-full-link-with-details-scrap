import requests
from bs4 import BeautifulSoup as bs
import csv

with open('all_link_data.txt', 'r') as file:
    urllist = file.readlines()

    for url in urllist:
        url = url.strip('\n')   
        s = requests.Session()
        res =s.get(url)
        soup = bs(res.text, 'html.parser')
        book_name = soup.find('div', {'class': 'col-sm-6 product_main'})
        head_line = book_name.find('h1').text
        book_price =book_name.find('p',{'class':'price_color'}).text
        book_des_h2 = soup.find('h2').text
        book_image = soup.find('div', {'class':'item active'}).find('img').get('src')
        image_link = 'https://books.toscrape.com/media/'+book_image
        book_description =soup.select_one('#content_inner > article > p').text #copy selector from eadge browser
        book = {'Book_Name': head_line,'Price': book_price,'Book_Photos': image_link,'Product_Description': book_des_h2,'Book_paragraph': book_description}
        with open('book_data.csv', 'a', newline='', encoding='utf-8') as file:
            writer= csv.DictWriter(file, fieldnames=book.keys())
            writer.writerow(book)
