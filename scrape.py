from bs4 import BeautifulSoup
import requests

onion_front_page_html = requests.get("https://www.theonion.com/").text
onion_front_page_soup = BeautifulSoup(onion_front_page_html, "html.parser")

#url of main article on the front page of the onion 
article_url = onion_front_page_soup.select("section+section a")[0]["href"]
article_html = requests.get(article_url).text
article_soup = BeautifulSoup(article_html, "html.parser")

article_title = article_soup.find("h1").get_text()
article_content = article_soup.find("p").get_text()
article_date = article_soup.select(".js_meta-time")[0].get_text()

print("%s\n\n%s\n\n%s" %  (article_date, article_title, article_content))
