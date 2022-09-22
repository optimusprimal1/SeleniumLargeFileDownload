import time
# from telnetlib import EC
from selenium.webdriver.support import expected_conditions as EC
import  selenium
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
# from tqdm import tqdm
from selenium.webdriver.support.wait import WebDriverWait

path = "D:\PDFDriveScrape\Chrome\chromedriver.exe"

service = Service(path)
option = webdriver.ChromeOptions()
option.add_experimental_option("prefs",{
  "download.default_directory": r"D:\InterestBasedDownload"
  })
driver = webdriver.Chrome(service = service, options=option)
driver.maximize_window()
driver.get("https://www.pdfdrive.com/")
time.sleep(3)
keywords_list = ["Sports","Blockchain","Food","Education","Animals"]

for kwrg in keywords_list:
    driver.find_element(By.ID, 'q').clear()
    driver.find_element(By.ID,'q').send_keys(kwrg)
    driver.find_element(By.ID, 'q').send_keys(Keys.RETURN)
    time.sleep(3)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source,'html.parser')
    # print('Soup = ', soup.prettify())
    pdf_anchor = soup.findAll('a',class_="ai-search")
    for pa in pdf_anchor:
        print('pa = ',pa['href'])
        complete_url = 'https://www.pdfdrive.com'+pa['href']
        # print('complete_url = ',complete_url)
        request  = requests.get('https://www.pdfdrive.com'+pa['href'])
        request_soup = BeautifulSoup(request.content,'html.parser')
        # print('Request_Soup = ', request_soup.prettify())
        getting_download_pdf_button = request_soup.find('a',{"id":"download-button-link"})
        driver.execute_script("window.open('');")

        # Switch to the new window and open new URL
        driver.switch_to.window(driver.window_handles[1])

        driver.get('https://www.pdfdrive.com'+getting_download_pdf_button['href'])
        wait = WebDriverWait(driver,10)
        progress_bar = wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"btn-user")))
        # progressCondition = progress_bar.get_attribute('aria-valuenow')
        # if progressCondition == 100 or progressCondition>100:
        download_file_soup = BeautifulSoup(driver.page_source,'html.parser')
        get_download_Text = download_file_soup.find('a',{"class":"btn-user"})
        print('get_download_Text = ',get_download_Text.text)
        if get_download_Text.text =="Download ( PDF )":
            # get_download_Text

        # Closing new_url tab
        driver.close()

        # progress - bar - striped


    # search_result_div = driver.find_elements(By.CLASS_NAME,"file-right")
    # for srd in search_result_div:
    #     srd.find_element(By.TAG_NAME,'a').click()

















































driver.implicitly_wait(4000)
driver.quit()