from selenium_class import Driver

driver = Driver()

driver.get_url("https://www.facebook.com/")

id_input = driver.find_by_id("email")
id_input.send_keys(input("ID : "))

pw_input = driver.find_by_id("pass")
pw_input.send_keys(input("PW : "))

lg_btn = driver.find_by_css("label#loginbutton > input")
driver.click(lg_btn)

driver.driver.close()