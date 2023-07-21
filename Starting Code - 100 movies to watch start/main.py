import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇


response = requests.get(URL)
one_hundred_movies_web_page = response.text
soup = BeautifulSoup(one_hundred_movies_web_page, 'html.parser')

movie_title = soup.select('h3.title')


title_list = [movie.getText() for movie in movie_title]
in_order = title_list[::-1]
print(in_order)
file_path = "movie_list.txt"
file = open(file_path, 'w')
for movie in in_order:
    file.write(f"{movie}\n")
file.close()
