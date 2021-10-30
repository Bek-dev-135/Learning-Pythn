import requests
from bs4 import BeautifulSoup

res =requests.get('https://news.ycombinator.com/news')
# print(res.text)
soup= BeautifulSoup(res.text, 'html.parser')
#print(soup)
#print(soup.body)

#finds all tags
#print(soup.find_all('a'))

#finds the first tag
#print(soup.find('a'))

links = (soup.select(".titlelink"))
subtexts= soup.select(".subtext")


def create_custom_hn(links,subtexts):
    hn=[]
    i=0
    for idx,item in enumerate(links):
        title= links[idx].getText()
        href=links[idx].get('href', None)
        vote=subtexts[idx].select(".score")

        if len(vote):
            points=int(vote[0].getText().replace("points", ""))


            hn.append({'title': title, "link": href, "votes":points})
    return hn,len(hn),i
print (create_custom_hn(links,subtexts))