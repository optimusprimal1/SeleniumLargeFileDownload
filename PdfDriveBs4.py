import requests
from bs4 import BeautifulSoup




Urls_To_Download = ["https://www.pdfdrive.com/search?q=sports&pagecount=&pubyear=&searchin=&em=","https://www.pdfdrive.com/animal-books.html",
                    "https://www.pdfdrive.com/food-books.html","https://www.pdfdrive.com/education-books.html",
                    "https://www.pdfdrive.com/blockchain-books.html"]

# https://www.pdfdrive.com/search?q=sports&pagecount=&pubyear=&searchin=&em=&page=2
for utd in Urls_To_Download:
    request = requests.get(utd)
    soup = BeautifulSoup(request.content,'html.parser')
    get_all_pageList_Data = soup.findAll('a',{"class":"ai-search"})
    for anchor in get_all_pageList_Data:
        pdf_File = requests.get('https://www.pdfdrive.com' + anchor['href'])
        get_file_soup = BeautifulSoup(pdf_File.content,'html.parser')
        print('File Soup = ',get_file_soup)



















