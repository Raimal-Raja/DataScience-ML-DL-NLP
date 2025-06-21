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
    print(f"fetched {len(soup.text)} character from {url}")
    print(f"fetched {soup.text} content from {url}")
    
threads = []
urls =[
    
    'https://www.python.org/community/diversity/',
    'https://www.python.org/community/lists/',
    'https://www.python.org/community/irc/'
]

for url in urls:
    thread = threading.Thread(target=fetch_web_content, args=(url,))
    threads.append(thread)
    thread.start()
    
    
for thread in threads:
    thread.join()
    
print("All web pages fetched")