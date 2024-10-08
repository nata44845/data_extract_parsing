from lxml_test import etree

def print_tree(element, depth=0):
    print("-"*depth+element.tag)
    for child in element.iterchildren():
        print_tree(child, depth+1)

tree = etree.parse("src/web_page.html")

root = tree.getroot()
print_tree(root)

title_element = tree.find("head/title")
print(title_element.text)

p_element = tree.find("body/p")
print(p_element.text)

list_items = tree.findall("body/ul/li")
print(list_items)
for li in list_items:
    print(li.text)

for li in list_items:
   a = li.find("a")
   if a is not None:
       print(f"{li.text.strip()} {a.text}")
   else:
       print(li.text)

