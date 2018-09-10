from lxml import etree
text = etree.parse('./sogo.html', etree.HTMLParser())
result = text.xpath('//div/div/@class')
print(result)