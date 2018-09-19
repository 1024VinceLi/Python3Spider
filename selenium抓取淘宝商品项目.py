from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC # index_page()中的主要判断模块
                                         # 传入的参数都是元组类型的locator，如(By.ID, 'kw')
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote
from pyquery import PyQuery as pq

# browser = webdriver.Chrome()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)
wait = WebDriverWait(browser, 10)

KEYWORD = 'iPad'


def index_page(page):
    """
    抓取索引页
    :param page: 页码
    加载url中的页面,通过if语句判断当前页面是否为1,如果是1,则进行函数最下面两个wait.until判断所需的
    元素是否加载完成;如果页面大于一,进入if循环通过传入page页数参数,input.send_keys(page)和
    submit.click()方法模拟页面跳转操作实现跳转到第page页.之后再进行wait.until判断页面加载是否完成.
    autor:Justin
    """
    print('正在爬取第', page, '页')
    try:
        url = 'https://s.taobao.com/search?q=' + quote(KEYWORD)
        browser.get(url)
        if page > 1:
            # presence_of_element_located 只要一个符合条件的元素加载出来就通过
            # presence_of_all_elements_located 必须所有符合条件的元素都加载出来才行
            input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form > input')))
            submit = wait.until(
                # element_to_be_clickable 这个条件判断元素是否可点击，传入locator
                EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager div.form > span.btn.J_Submit')))
            input.clear()
            input.send_keys(page)
            submit.click()
        wait.until( # wait.until 判断该元素是否被加载在DOM中，并不代表该元素一定可见
            # text_to_be_present_in_element 判断某段文本是否出现在某元素中
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active > span'), str(page)))
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item')))
        get_products()
    except TimeoutException:
        index_page(page)



def get_products():
    '''
    :return: 提取商品参数
    '''
    html = browser.page_source # 获取源码
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items() # 此方法返回一个元组对列表。
    for item in items:
        product = {
            # item.find()查找此标签.text()获取标签中的文本
            'title': item.find('.title').text(),
            'price': item.find('.price').text(),
            'shop': item.find('.shop').text(),
            'deal': item.find('.deal-cnt').text(),
            'image': item.find('.pic .img').attr('data-src'),
            'location': item.find('.location').text()
        }
        print(product)
        # save_to_mongo(product)


MAX_PAGE = 100


def main():
    '''遍历每一页'''
    for i in range(1, MAX_PAGE + 1):
        index_page(i)
    browser.close()


if __name__ == '__main__':
    main()
