from selenium import webdriver
from bs4 import BeautifulSoup

driver=webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
driver.implicitly_wait(20)
group_name = driver.find_element_by_css_selector("#pane-side > div:nth-child(1) > div > div > div:nth-child(11) > div > div > div._3OvU8 > div._3vPI2 > div.zoWT4 > span")
group_name.click()

lnks =driver.find_elements_by_tag_name("a")
for lnk in lnks:
    print(lnk.get_attribute(href))
driver.quit()







# group_column =driver.find_elements_by_class_name("i0jNr")
# print(type(group_column))
# text_1= ''.join(group_column)
# print(text_1.text)
# print(text_1.get_attribute("css=a@href"))












# group_column_text =group_column.text
# group_column_attribute_value = group_column.get_attribute('value')

# print('group_column.text: {0}'.format(group_column_text))
# print('group_column.get_attribute(\'value\'):{0}'.format(group_column_attribute_value))



# <a href="https://zoom.us/j/98770148761?pwd=aVVOTXFUMTROd2JCKzNrSjNwTmhHQT09" title="https://zoom.us/j/98770148761?pwd=aVVOTXFUMTROd2JCKzNrSjNwTmhHQT09" target="_blank" rel="noopener noreferrer" class="i0jNr selectable-text copyable-text">https://zoom.us/j/98770148761?pwd=aVVOTXFUMTROd2JCKzNrSjNwTmhHQT09</a>
# <a href="https://us02web.zoom.us/j/81600754535?pwd=dzZ6ZEJ6Sko2M05lb3RidWk1SHRIUT09" title="https://us02web.zoom.us/j/81600754535?pwd=dzZ6ZEJ6Sko2M05lb3RidWk1SHRIUT09" target="_blank" rel="noopener noreferrer" class="i0jNr selectable-text copyable-text">https://us02web.zoom.us/j/81600754535?pwd=dzZ6ZEJ6Sko2M05lb3RidWk1SHRIUT09</a>
# <selenium.webdriver.remote.webelement.WebElement (session="", element="")>]