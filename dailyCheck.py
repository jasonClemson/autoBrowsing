from selenium import webdriver
from selenium.webdriver.common.keys import Keys

daily =["Jadeveon Clowney", "Logan Ryan", "Everson Griffen", "Cam Newton", "Presidential Polls", "Joe Biden VP", "Coronavirus stats"]

driver = webdriver.Chrome('./chromedriver')

for query in daily:
    driver.execute_script('''window.open("https://google.com","_blank");''')
    driver.switch_to.window(driver.window_handles[-1])
    driver.implicitly_wait(3)
    search=driver.find_element_by_name("q")
    search.clear()
    search.send_keys(query)
    search.send_keys(Keys.RETURN)
#driver.close()