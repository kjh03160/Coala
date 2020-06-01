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

search_box.send_keys("치킨\n")
search_box.send_keys("\n")


time.sleep(1)
k = 1
while True:

    containers = WebDriverWait(driver, 5).until(
                        EC.presence_of_all_elements_located(
                            (By.CSS_SELECTOR, "div.link_search")))
    print(len(containers))


    for i in containers:
        name = WebDriverWait(i, 5).until(
                        EC.presence_of_element_located(
                            (By.CSS_SELECTOR, "span.search_title_text"))).text
        # name = i.find_element_by_css_selector("span.search_title_text").text

        address = WebDriverWait(i, 5).until(
                        EC.presence_of_element_located(
                            (By.CSS_SELECTOR, "span.address"))).text
        # address = i.find_element_by_css_selector("span.address").text

        try:
            tel = WebDriverWait(i, 5).until(
                        EC.presence_of_element_located(
                            (By.CSS_SELECTOR, "span.phone"))).text
        except:
            tel = "None"
        print(name, address, tel)
    pagination = driver.find_elements_by_css_selector('div.pagination_area > a')

    try:
        if k % 5:
            pagination[k % 5].click()
        else:
            next = driver.find_element_by_css_selector('button.btn_next')
            if next.get_attribute('disabled'):
                raise Exception
            next.click()
        k += 1
    except Exception as e:
        print(e)
        print('수집완료')
        break

driver.close()