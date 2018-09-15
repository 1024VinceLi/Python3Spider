from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
import time
browser = webdriver.Chrome()

browser.get('https://taobao.com')
# input.send_keys(Keys.ENTER)
#     wait = WebDriverWait(browser, 10)
#     wait.until(EC.presence_of_element_located(By.ID, 'content_left'))
#     print(browser.current_url)
#     print(browser.get_cookies())
input_first = browser.find_element_by_id('q')  # 找到搜索框的id为q
# input_second = browser.find_element_by_css_selector('#q')
# input_third = browser.find_element_by_name('q')
input_first.send_keys('iPhone')  # 作用是在搜索框中输入 此处代码有问题，暂时未解决
time.sleep(1)
input_first.clear()
input_first.send_keys('iPad')
button = browser.find_element_by_class_name('btn-search')
button.click()

# print(input_first, '\n', input_second, '\n', input_third)

# browser.close()

