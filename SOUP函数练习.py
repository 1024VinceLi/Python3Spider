html = '''<div class="bg-wkq js-settings-mask"></div>

            <dl class="js-as-select">
                <dt>搜索结果显示条数</dt>
                <dd>
                    <a href="javascript:void(0);" class="xz" data-value="10">每页显示10条</a>
                    <ul id="settings-number-list">
                        <li><a  href="javascript:void(0);" data-value="10">每页显示10条</a></li>
                        <li><a  href="javascript:void(0);" data-value="20">每页显示20条</a></li>
                        <li><a  href="javascript:void(0);" data-value="50">每页显示50条</a></li>
                        <li><a  href="javascript:void(0);" data-value="100">每页显示100条</a></li>
                    </ul>
                </dd>
                <input type="hidden" name="pageNum" id="settings-show-number" value="10">
            </dl>
            <p class="enter" style="padding-top: 20px;">
                <a href="javascript:void(0);"  class="a1">保存</a>
                <a href="javascript:void(0);"  class="a2">恢复默认</a>
            </p>
        </div>
'''
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
print(soup.find_all(name='a'))
print(soup.find_all(attrs={'class': 'a1'}))
print(soup.find_all(id='settings-show-number'))
print(soup.ul)
print(soup.a)
print(soup.ul.children)
for child in enumerate(soup.ul.children):
    print(child)
print(soup.select('ul li'))
print(soup.select('.enter'))
# 使用select选择属性时,属性名(ul li div)前不用加点,选择一个标签的class时,前面要加上点;
# 只能选择class属性,不能选择其他如id,name等属性
print(soup.select('.xz'))
lidata = soup.find_all(name='li')
for data in lidata:
    print(data.get_text())
    #get_text()函数获取文本内容,非常好用的函数