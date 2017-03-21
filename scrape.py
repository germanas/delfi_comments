from bs4 import BeautifulSoup

import requests

url = "www.delfi.lt/news/daily/lithuania/r-karbauskis-siulo-vrk-formuoti-be-partiju-atstovu.d?id=74121020&com=1&reg=0&no=0&s=2"

r  = requests.get("http://" +url)

data = r.text

soup = BeautifulSoup(data, "html.parser")
linklist = set()

for link in soup.find_all('a'):
    linklist.add(link.get('href'))

correct_list = []
print correct_list
for item in linklist:
    if item is not None and "http://" in item:
        print 'http' + item
        correct_list.append(item)
    elif item is not None and "https://" in item:
        print 'https' + item
        correct_list.append(item)
    elif item is not None:
        print 'reject ' + item

print correct_list

comment_list = []

for item in correct_list:
    new_request = requests.get(item)
    text = new_request.text
    soup2 = BeautifulSoup(text, "html.parser")
    for link in soup2.find_all('a'):
        correct_list.append(link.get('href'))
    for item2 in soup2.find_all("div", { "class" : "comment-date" }):
        comment_list.append(item2)

print len(comment_list)
