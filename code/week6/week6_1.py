from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
# options.add_argument('headless')
options.add_argument(
    "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get('https://map.naver.com/')
driver.execute_script("arguments[0].click();", driver.find_element_by_css_selector("span.span_search"))

time.sleep(3)
search_box = driver.find_element_by_xpath('/html/body/app/layout/div[2]/div[2]/div[1]/shrinkable-layout/search-layout/search-box/div/div[1]/div/input')

search_box.send_keys("치킨")
time.sleep(1)
search_box.send_keys('\n')

time.sleep(1)

containers = driver.find_elements_by_css_selector("div.link_search")

for i in containers:
    name = i.find_element_by_css_selector("span.search_title_text").text
    address = i.find_element_by_css_selector("span.address").text
    tel = i.find_element_by_css_selector("span.phone").text
    print(name, address, tel)


driver.close()