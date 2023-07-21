from bs4 import BeautifulSoup
import lxml
import requests

response = requests.get('https://news.ycombinator.com/news')

# print(response.text)

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, 'html.parser')
td_elements = soup.find_all(name='td', class_='title')

for td in td_elements:
    title_spans = td.find_all(name='span', class_='titleline')
    for span in title_spans:
        a_tags = span.find_all(name='a')
        for a_tag in a_tags:
            print(a_tag.getText())
            print(a_tag.get('href'))
            print('\n')

article_tag = soup.find(name='span', class_='titleline')


# all_anchor_tags = soup.find_all(name='a')
# print(all_anchor_tags)

# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get('href'))
#     pass

# class_is_heading = soup.find_all(name='h3', class_='heading')
# print(class_is_heading)

# h3_heading = soup.find(name='h3', class_='heading')
# print(h3_heading)

# name = soup.select_one(selector='#name')
# print(name)


# headings = soup.select(".heading")
# print(headings)
