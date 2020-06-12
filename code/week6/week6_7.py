from selenium_class import Driver
import time

# id = input("ID : ")
# pw = input("PW : ")

driver = Driver()

driver.get_url("https://www.instagram.com/explore/tags/ootd/")

lg_btn = driver.find_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div/div/div/div[3]/div[1]/a")
driver.click(lg_btn)

id_input = driver.find_by_name("username")
id_input.send_keys(id)

pw_input = driver.find_by_name("password")
pw_input.send_keys(pw)

next_btn = driver.find_by_css("button.L3NKy")
driver.click(next_btn)

driver.click(driver.find_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button"))

time.sleep(2)
driver.get_url("https://www.instagram.com/explore/tags/ootd/")

divs = driver.find_all_by_css("div._9AhH0")[:12]
driver.click(divs[0])

for i in divs:
    text = driver.find_by_css('div.C4VMK span').text
    print(text)
    print("=" * 20)
    btn = driver.find_by_css('a._65Bje')
    driver.click(btn)

driver.driver.close()

