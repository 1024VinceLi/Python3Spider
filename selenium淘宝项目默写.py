from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from pyquery import PyQuery as pq
from urllib.parse import quote

# browser = webdriver.Chrome()
Chrome_options = webdriver.ChromeOptions()
Chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=Chrome_options)
wait = WebDriverWait(browser, 10)

KEYWORD = 'iPad'

def index_page(page):
    '''获取页码'''
    print('正在爬取第', page, '页')
    try:
        # url = 'https://s.taobao.com/search?q' + quote(KEYWORD) # q后面有一个等于号
        url = 'https://s.taobao.com/search?q=' + quote(KEYWORD)
        browser.get(url) # 先请求网页
        if page > 1: # 再判断当前页码是否为第一页
            input = wait.until( # 定义input,获取输入页码端口
                EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form > input')))
            submit = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager div.form > span.btn.J_Submit')))
            input.clear()
            input.send_keys(page)
            submit.click() # 页码跳转完成
        wait.until( # 从此步骤开始加载页面信息
                # text_to_be_present_in_element判断某段文字是否出现
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active > span'),str(page)))
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item')))
        get_products()
    except TimeoutException:
        print('爬取第', page, '页超时')
        index_page(page)



def get_products():
    '''获取商品参数'''
    html = browser.page_source  # 获取网页源码
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items() # 此方法返回一个元组对列表。
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


MAX_PAGE = 100

def main():
    '''遍历每一页'''
    for i in range(1, MAX_PAGE + 1):
        index_page(page=i)
    browser.close()




if __name__ == '__main__':
    main()

