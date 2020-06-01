from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions()
options.add_argument(
    "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get("https://papago.naver.com/")
time.sleep(2)
text_box = driver.find_element_by_id("txtSource")
text_box.send_keys("seize the day")
time.sleep(2)

trans_btn = driver.find_element_by_id("btnTranslate")
driver.execute_script("arguments[0].click();", trans_btn)

result_text = driver.find_element_by_id("txtTarget").text.strip()
print(result_text)

driver.quit()