# web scraping

# import packages
import requests
from bs4 import BeautifulSoup
from conn import execute_query

url = r"http://localhost"
data = requests.get(url)


if data.status_code == 200:
    
    html = BeautifulSoup(data.text, "html.parser")
    titles_list = html.find_all("h3", attrs={"class": "title-post"})

    for contador, titles in enumerate(titles_list):

        post = titles.find("a", {"class": "post_url"})
        post_url = rf"http://localhost{post['href']}" 
        
        req_for_post = requests.get(post_url)
        dom = BeautifulSoup(req_for_post.text, "html.parser")

        data = {
            "title": dom.find("h3", attrs={"class": "post-title"}).getText(),
            "url": post_url,
            "views": int(dom.find("span", attrs={"class": "views"}).getText()),
            "author": dom.find("a", attrs={"class": "user-link"}).getText()
        }

        try:

            query = "INSERT INTO details(title, url, views, author) VALUES ('%s', '%s', '%i', '%s')" % (data["title"], data["url"], data["views"], data["author"])
            sql = execute_query(query)
            msg = "dato {0}, id [{1}] SUCCESS".format(contador, data['url'].split("/")[-1])
            print (msg)

        except:
            msg = "dato {0}, id [{1}] ERROR".format(contador, data['url'].split("/")[-1])
            print (msg)