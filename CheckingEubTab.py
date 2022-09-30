import time
# from telnetlib import EC
from pathlib import Path

from selenium.webdriver.support import expected_conditions as EC
import  selenium
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import os
import  os.path
from os import path


from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
# from tqdm import tqdm
from selenium.webdriver.support.wait import WebDriverWait

path = "D:\PDFDriveScrape\Chrome\chromedriver.exe"

service = Service(path)
option = webdriver.ChromeOptions()
# option.add_experimental_option("prefs",{
#   "download.default_directory": r"D:\InterestBasedDownload\Sports"
#   })
driver = webdriver.Chrome(service = service, options=option)
driver.maximize_window()
driver.get("http://www.pdfdrive.com/sports-nutrition-vitamins-and-trace-elements-2nd-ed-volume-of-nutrition-in-exercise-and-sport-series-crc-taylor-francis-e183891534.html")
time.sleep(10)

# driver.get('https://www.pdfdrive.com'+getting_download_pdf_button['href'])
        # wait = WebDriverWait(driver,10)
# while True:
#     if driver.find_elements(By.CLASS_NAME,"btn-user"):
#         WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CLASS_NAME, "btn-user")))
#         print('Abc = ')
#         break



# progressCondition = progress_bar.get_attribute('aria-valuenow')
# if progressCondition == 100 or progressCondition>100:
download_file_soup = BeautifulSoup(driver.page_source,'html.parser')
get_pdf_file_name = download_file_soup.find("div", {"id": "alternatives"})
print('get_pdf_file_name = ',get_pdf_file_name)
anchor = get_pdf_file_name.find('a',{"class":"btn-user"})
anchor_slice = anchor['href'][-3:]
print('get_pdf_file_name = ',anchor_slice)
if anchor_slice=='pdf':
    from requests import get

    file_path = 'D:/InterestBasedDownload/Sports/'
    reply = get('https://www.pdfdrive.com' + anchor['href'], stream=True)
    with open(file_path + 'make_file_name', 'wb') as file:
        for chunk in reply.iter_content(chunk_size=1024):
            print('make_file_name = ', 'make_file_name')
            if chunk:
                file.write(chunk)


time.sleep(20)
# get_download_Text = download_file_soup.find('a',{"class":"btn-user"})
# if ':' in get_pdf_file_name:
#     get_pdf_file_name = get_pdf_file_name.replace(':', '')
# make_file_name = get_pdf_file_name.replace('\n','') +'( PDFDrive ).pdf'
# print('get_download_Text = ',get_download_Text.text)
# if "Download ( PDF )" in get_download_Text.text :
#     from requests import get
#     file_path = 'D:/InterestBasedDownload/Sports/'
#     reply = get('https://www.pdfdrive.com'+get_download_Text['href'], stream=True)
#     with open(file_path + make_file_name, 'wb') as file:
#         for chunk in reply.iter_content(chunk_size=1024):
#             print('make_file_name = ', make_file_name)
#             if chunk:
#                 file.write(chunk)
#     parent = driver.window_handles[0]
#     chld = driver.window_handles[1]
#     driver.close()
#     driver.switch_to.window(parent)
# else:
#     parent = driver.window_handles[0]
#     chld = driver.window_handles[1]
#     driver.close()
#     driver.switch_to.window(parent)
            # driver.get('https://www.pdfdrive.com'+get_download_Text['href'])

        # else:
        #     parent = driver.window_handles[0]
        #     chld = driver.window_handles[1]
        #     driver.switch_to.window(chld)
        #     driver.close()
        #     driver.switch_to.window(parent)
        # if kwrg =="Sports":
        #     option.add_experimental_option("prefs", {
        #         "download.default_directory": r"D:\InterestBasedDownload\Sports"
        #     })
        # if kwrg =="Blockchain":
        #     option.add_experimental_option("prefs", {
        #         "download.default_directory": r"D:\InterestBasedDownload\Blockchain"
        #     })
        # if kwrg =="Food":
        #     option.add_experimental_option("prefs", {
        #         "download.default_directory": r"D:\InterestBasedDownload\Food"
        #     })
        # if kwrg =="Education":
        #     option.add_experimental_option("prefs", {
        #         "download.default_directory": r"D:\InterestBasedDownload\Education"
        #     })
        # if kwrg =="Animals":
        #     option.add_experimental_option("prefs", {
        #         "download.default_directory": r"D:\InterestBasedDownload\Animals"
        #     })

        # progress - bar - striped


    # search_result_div = driver.find_elements(By.CLASS_NAME,"file-right")
    # for srd in search_result_div:
    #     srd.find_element(By.TAG_NAME,'a').click()
















































driver.implicitly_wait(4000)
driver.quit()




























# https://www.pdfdrive.com/nutrition-for-sport-exercise-and-performance-a-practical-guide-for-students-sports-enthusiasts-and-professionals-d195265729.html