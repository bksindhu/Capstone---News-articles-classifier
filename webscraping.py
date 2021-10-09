# # -*- coding: utf-8 -*-
# """RssFeed.ipynb

# Automatically generated by Colaboratory.

# Original file is located at
#     https://colab.research.google.com/drive/1n6gncZk7xvyC2oeN-FNEy5FF7B8_a_kx
# """

# import requests
# from bs4 import BeautifulSoup

# #enter URL
# url = "http://feeds.bbci.co.uk/news/world/us_and_canada/rss.xml"

# resp = requests.get(url)

# soup = BeautifulSoup(resp.content, features="xml")

# print(soup.prettify())

# items = soup.findAll('item')

# print(items)

# len(items)

# items[1]

# #declare empty var to append data
# news_items = []

# #scarring HTML tags such as Title, Description, Links and Publication date
# for item in items:
#     news_item = {}
#     news_item['title'] = item.title.text
#     news_item['description'] = item.description.text
#     news_item['link'] = item.link.text
#     news_item['pubDate'] = item.pubDate.text
#     news_items.append(news_item)

# news_items[0]

# #import pandas to create dataframe and CSV
# import pandas as pd
# df = pd.DataFrame(news_items,columns=['title','description','link','pubDate'])

# df.head()

# df.to_csv('BBCdata1.csv',index=False, encoding = 'utf-8')

