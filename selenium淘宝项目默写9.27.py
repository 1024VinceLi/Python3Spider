from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# index_page()中的主要判断模块 # 传入的参数都是元组类型的locator，如(By.ID, 'kw')
from urllib.parse import quote
from pyquery import PyQuery as pq

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)
wait = WebDriverWait(browser, 10)
KEYWORD = 'iPad'

def index_page(page):
    print('正在爬取第', page, '页')
    try:
        url = 'https://s.taobao.com/search?q=' + quote(KEYWORD)
        browser.get(url)
        if page > 1:
            input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form > input')))
            submit = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager div.form > span.btn.J_Submit')))
            input.clear()
            input.send_keys(page)
            #input.send_keys(KEYWORD)页面跳转输入关键词应该是页码page
            submit.click()
        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active > span'), str(page)))
        wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item')))
        get_products()
    except TimeoutException:
        index_page(page)

# def index_page(page):
#     """
#     抓取索引页
#     :param page: 页码
#     加载url中的页面,通过if语句判断当前页面是否为1,如果是1,则进行函数最下面两个wait.until判断所需的
#     元素是否加载完成;如果页面大于一,进入if循环通过传入page页数参数,input.send_keys(page)和
#     submit.click()方法模拟页面跳转操作实现跳转到第page页.之后再进行wait.until判断页面加载是否完成.
#     autor:Justin
#     """
#     print('正在爬取第', page, '页')
#     try:
#         url = 'https://s.taobao.com/search?q=' + quote(KEYWORD)
#         browser.get(url)
#         if page > 1:
#             input = wait.until(
#                 EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form > input')))
#             submit = wait.until(
#                 EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager div.form > span.btn.J_Submit')))
#             input.clear()
#             input.send_keys(page)
#             submit.click()
#         wait.until(
#             EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active > span'), str(page)))
#         wait.until(
#             EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item')))
#         get_products()
#     except TimeoutException:
#         index_page(page)



def get_products():
    html = browser.page_source
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        product = {
            'title': item.find('.title').text(),
            'price': item.find('.price').text(),
            'shop': item.find('.shop').text(),
            'deal': item.find('.deal-cnt').text(),
            'image': item.find('.pic .img').attr('data-src'),
            'location': item.find('.location').text()
        }
        print(product)


MAX_PAGE = 20


def main():
    for i in range(1, MAX_PAGE+1):
        index_page(i)
    browser.close()


if __name__ == '__main__':
    main()