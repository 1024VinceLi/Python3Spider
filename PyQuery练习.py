html = '''<div class="bg-wkq js-settings-mask"></div>

            <dl class="js-as-select">
                <dt>搜索结果显示条数</dt>
                <dd>
                    <a href="javascript:void(-2);" class="xz" data-value="10">每页显示10条</a>
                    <ul id="settings-number-list">
                        <li class="myname"><a  href="javascript:void(-1);" data-value="10">每页显示10条</a></li>
                        <li><a  href="javascript:void(0);" data-value="20">每页显示20条</a></li>
                        <li><a  href="javascript:void(1);" data-value="50">每页显示50条</a></li>
                        <li><a  href="javascript:void(2);" data-value="100">每页显示100条</a></li>
                    </ul>
                </dd>
                <input type="hidden" name="pageNum" id="settings-show-number" value="10">
            </dl>
            <p class="enter" style="padding-top: 20px;">
                <a href="javascript:void(3);"  class="a1">保存</a>
                <a href="javascript:void(4);"  class="a2">恢复默认</a>
            </p>
        </div>
'''
from pyquery import PyQuery as pq
data = pq(html)
print(data)
#doc = pq(url='https://cuiqingcai.com')
#print(doc('title'))
dd = pq(filename='sogo.html')
print(dd('a'))
print(data('.js-as-select #settings-number-list li'))
tt = data('ul')
ti = tt.children('.myname')
print(ti)
a =data('a')
for item in a.items():
    print(item.attr('href'))
    print(item.text())
b = tt('a')
for item1 in b.items():
    print(item1.attr('href'))
    print(item1.text())
print(tt.html())