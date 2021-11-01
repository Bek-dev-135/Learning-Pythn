import requests
from bs4 import BeautifulSoup
import pprint

i=0
while i<4:
    i+=1

    res =requests.get('https://news.ycombinator.com/news?p='+str(i))
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

    def sorted_stories_by_votes(hnlist):
        return sorted( hnlist, key= lambda k: k['votes'], reverse=True)

    def create_custom_hn(links,subtexts):
        hn=[]

        for idx,item in enumerate(links):
            title= links[idx].getText()
            href=links[idx].get('href', None)
            vote=subtexts[idx].select(".score")

            if len(vote) :
                points=int(vote[0].getText().replace("points", ""))


                hn.append({'title': title, "link": href, "votes":points})
        return sorted_stories_by_votes(hn)
    pprint.pprint(create_custom_hn(links,subtexts))