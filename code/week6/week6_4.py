from selenium_class import Driver

driver = Driver()
driver.get_url('https://www.google.com/maps/')

search_box = driver.find_by_css("input.tactile-searchbox-input")
search_box.send_keys("카페")

search_btn = driver.find_by_id("searchbox-searchbutton")
driver.click(search_btn)

while True:

    results = driver.find_all_by_css("div.section-result")

    for i in results:
        name = driver.find_by_css_with_obj(i, "h3.section-result-title > span").text
        try:
            rate = driver.find_by_css_with_obj(i, "span.cards-rating-score").text
        except:
            rate = "-"
        address = driver.find_by_css_with_obj(i, "span.section-result-location").text

        print(name, rate, address)

    pagination = driver.find_all_by_css("div.gm2-caption button")[1]
    if pagination.get_attribute('disabled'):
        break
    else:
        driver.click(pagination)

print("수집 완료")



