import requests

url = 'https://httpbin.org/post' #grader url here
multiple_files = [
     ('first.txt', open('file1.txt', 'rb')),
     ('second.txt', open('file2.txt', 'rb')),
     ('lr6.pkt', open('lr6.pkt', 'rb'))]
r = requests.post(url, files=multiple_files)
print(r.text)