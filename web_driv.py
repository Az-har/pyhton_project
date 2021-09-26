# from bs4 import BeautifulSoup
# import requests
# url = "https://www.amazon.in/ASUS-15-6-inch-i5-10300H-SSDWindows-FX566LH-BQ275T/dp/B096VJ2J4P?ref_=Oct_DLandingS_D_1cf98edc_60&smid=A14CZOWI0VEHLG"

# # add header
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
# r = requests.get(url, headers=headers)
# r.raise_for_status()
# soup = BeautifulSoup(r.content, 'html.parser')
# elems=soup.find(class_= "a-size-medium a-color-price priceBlockDealPriceString")
# print(elems.text.strip())

from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://automatetheboringstuff.com/')
elem = browser.find_element_by_css_selector('body > div > main > div > ul:nth-child(16) > li:nth-child(13) > a')
elem.click()


