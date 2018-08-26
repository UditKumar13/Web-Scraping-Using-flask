import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import requests
##to fetch the webpage

from bs4 import BeautifulSoup
##to parse the webpage
%matplotlib inline

url='https://www.imdb.com/chart/top'
## fetch the web page
r=requests.get(url)
soup=BeautifulSoup(r.text,'html.parser')
TITLES=[]
YEARS=[]
URLS=[]
RATINGS=[]
DIRECTORS=[]
ACTORS=[]
table_inf=soup.find_all('tbody',{'class':'lister-list'})
doc=table_inf[0]
rows=doc.find_all('tr')
title_column=test_row.find('td',{'class':'titleColumn'})

count=0
movie_root_url = 'https://www.imdb.com'
for row in rows:
    #if count>1:
        #break
    count+=1
    title_column=row.find('td',{'class':'titleColumn'})
    rating_column=row.find('td',{'class':'ratingColumn'})
    movie_title=title_column.a.text

    year=title_column.span.text.split('(')[-1].split(')')[0]
    movie_rel_url=title_column.a['href']
    movie_url= movie_root_url +  movie_rel_url


    imp_people = title_column.a['title']
    director=imp_people.split(',')[0].split('(')[0].strip()
    actors = ','.join(imp_people.split(',')[1:]).strip()
    rating=rating_column.strong.text



    directors=imp_people.split(',')[0].split('(')[0].strip()

    TITLES.append(movie_title)
    YEARS.append(year)
    URLS.append(movie_url)
    RATINGS.append(rating)

    ACTORS.append(actors)
    DIRECTORS.append(director)

print (count)

uk_df=pd.DataFrame({'Title': TITLES, 'Rating': RATINGS, 'Year': YEARS, 'URL': URLS, 'Director': DIRECTORS, 'Actors': ACTORS},
                     columns=['Title', 'Year', 'Rating', 'Director', 'Actors', 'URL'])
uk_df.to_csv('./imdb.csv', index=False)

def show(n):
    movie_data = pd.read_csv('imdb.csv')
    return movie_data.head(n)
