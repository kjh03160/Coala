from selenium_class import Driver
import time
driver = Driver()

driver.get_url("https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com")

time.sleep(5)

id_input = driver.find_by_id("id")
id_input.clear()
id_input.send_keys(input("ID : "))

pw_input = driver.find_by_id("pw")
pw_input.clear()
pw_input.send_keys(input("PW : "))

lg_btn = driver.find_by_css("input.btn_global")
driver.click(lg_btn)