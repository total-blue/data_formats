import xml.etree.ElementTree as ET

tree = ET.parse('news.xml')
root = tree.getroot()

items = root.findall('channel/item')
descriptions = []
for item in items:
    descriptions.append(item.find('description').text)

all_words = ' '.join(descriptions).split()
all_words = [x.lower() for x in all_words]
set_words = set(all_words)

len_dict = {}
for word in set_words:
    if len(word) > 6:
        len_dict[word] = all_words.count(word)

pairs = list(len_dict.items())
pairs.sort(key=lambda i: i[1], reverse=True)
res = pairs[:10]
for i in res:
    print(i[0])
