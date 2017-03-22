from bs4 import BeautifulSoup
import pprint
import pandas as pd

import requests

url = "www.delfi.lt/"

r  = requests.get("http://" +url)

data = r.text

soup = BeautifulSoup(data, "html.parser")
linklist = set()

for link in soup.find_all('a'):
    linklist.add(link.get('href'))

correct_list = []
print correct_list
for item in linklist:
    if item is not None and "http://www.delfi.lt" in item:
        print 'http' + item
        correct_list.append(item)
    elif item is not None and "https://www.delfi.lt" in item:
        print 'https' + item
        correct_list.append(item)
    elif item is not None:
        print 'reject ' + item

print correct_list

text_list = []

#while len(correct_list) < 50:
for item in correct_list:
    new_request = requests.get(item)
    text = new_request.text
    soup2 = BeautifulSoup(text, "html.parser")
    for link in soup2.find_all('a'):
        if link is not None and "http://www.delfi.lt" in link:
            correct_list.append(link)
        elif link is not None and "https://www.delfi.lt" in link:
            correct_list.append(link)
        elif link is not None:
            print link

print len(correct_list)


for item2 in correct_list:
    new_request2 = requests.get(item2)
    text2 = new_request2.text
    soup3 = BeautifulSoup(text2, "html.parser")
    tags = soup3.find_all("div", attrs={"data-post-id":True})
    for item in tags:
        text_list.append(item)


pprint.pprint(text_list)

print len(text_list)


data_frame = pd.DataFrame(
    {'string':text_list}
)
print data_frame

data_frame.to_csv('delfiOutput.csv', mode='a', sep='\t')