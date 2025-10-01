from langchain.tools import tool
from bs4 import BeautifulSoup
from newspaper import Article
import requests
from time import sleep


@tool
def SearchWeb(query:str,max_results:int = 5,rate_limit:int=1.0):
    header = {"User-agent":"Mozzila/5.0"}
    url = f"https://duckduckgo.com/html/q=?{query}"
    res = requests.get(url=url,headers=header)
    if res.status_code != 200:
        return []
    soup = BeautifulSoup(res.text,"html.parser")
    results = []
    for a in soup.find_all("a",{"class":"result__a"},limit=max_results):
        title = a.get_text()
        link = a['href']
        snippet_tag = a.find_next("a").find_next_sibling("div")
        snippet = snippet_tag.get_text() if snippet_tag else ""
        
        
        article = Article(url=url)
        article.download()
        article.parse()
        
        results.append({
            "title":title,
            "link":link,
            "snippet":snippet,
            "article":article.text
        })
        sleep(rate_limit)
        return results
        
    