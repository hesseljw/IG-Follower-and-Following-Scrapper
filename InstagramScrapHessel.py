#Instagram Detail Scrapper
#Created by Hessel Juliust

from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests

import pandas as pd
df=pd.read_csv('contohuserig.csv', sep=',',header=None)
panjang = len(df)

print(panjang)
i = 0

while i<panjang:
    handle = df[0][i]
    url = "https://www.instagram.com/"
    

    import requests
    r = requests.get(url+handle)
    rstat = int(r.status_code)
    #print(rstat)
    if rstat == 404 :
        print("InstagramError InstagramError InstagramError")
        i = i+1
    else:
        page = urlopen(url+handle).read()
        soup = BeautifulSoup(page, features="html.parser")
        string = soup.find("meta",  property="og:description")['content']
        followers = string.split(" Followers, ")[0].replace(",","").replace("k", "000")
        if "." in followers:
           followers = followers.replace(".","")[:-1]
   
        following = string.split(" Followers, ")[1].split(" Following, ")[0].replace(",","").replace("k", "000")
        if "." in following:
           following = following.replace(".","")[:-1]
   
        posts = string.split(" Followers, ")[1].split(" Following, ")[1].split(" Posts")[0].replace(",","").replace("k", "000")
        if "." in posts:
           posts = posts.replace(".","")[:-1]
   
        print(posts, followers, following)
        i = i+1
