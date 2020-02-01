import json
import xml

with open('news.json', encoding='utf-8') as f:
    data = json.load(f)

    news_list = data['rss']['channel']['items']

    description_list = []
    for news in news_list:
        description_list.append(news['description'])

    all_words = ' '.join(description_list).split()
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
