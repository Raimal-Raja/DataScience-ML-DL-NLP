'''
Real-world example: Multi-threading for I/O-bound task
Scenario: Web Scrapping
web scrapping often involves making numerous network requests to
fetch web pages. These tasks are I/O-bound because they spend a lot of
time waiting for responses from servers. Multi-threading can significantly
improve the performance by allowing multiple web-apges to be fetch concurrently

'''
import requests
from bs4 import BeautifulSoup as bs
import threading

def fetch_web_content(url):
    response = requests.get(url)
    soup = bs(response.content, 'html.parser')
    print(f"fetche {len(soup.text)} character from {url}")
    
threads = []

for url in urls:
    thread = threading.Thread(target=fetch_web_content, args=(url))
    threads.append(thread)
    thread.start()
    
    
for thread in threads:
    thread.join()
    
print("All web pages fetched")