from lxml import etree

tree = etree.parse("src/web_page.html")

title_element = tree.xpath("//title")[0]
print(title_element.text)

title_element = tree.xpath("//title/text()")[0]
print(title_element)

title_element = tree.xpath("//p/text()")[1]
print(title_element)

list_items = tree.xpath("//li")
for li in list_items:
   print(etree.tostring(li))

list_items = tree.xpath("//ul/descendant::li")
for li in list_items:
   text = ''.join(map(str.strip, li.xpath(".//text()")))
   print(text)

