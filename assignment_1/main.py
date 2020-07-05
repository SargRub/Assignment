import requests


url = input()
website = requests.get(url)
text = website.text
with open("index.html", "w") as f:
    f.write(text)

# Variant 1
import re
lis = re.findall(r'<li><a href="/.+"><span>(.+)</span>(.+)</a></li>', text)
with open("links.txt", "w") as txt:
    for pair in lis:
        txt.write(f"{pair[0]} - {pair[1]} \n")


# Variant 2
# from bs4 import BeautifulSoup
# with open('index.html') as f:
#     soup = BeautifulSoup(f, 'html.parser')
#     uls = soup.find_all('ul')
#     for ul in uls:
#         for li in ul.findAll('li'):
#             for a in li.findAll('a'):
#                 print(a.contents[0].contents[0], "-", a.contents[1])


# Variant 3
# import re
#
#
# def code_and_content(link):
#     return re.findall('href="/(.+)"><span>', link)[0], re.findall('</span>(.+)</a>', link)[0]
#
#
# start = 0
# end = 0
# with open('links.txt', 'w') as txt:
#     while end != -1:
#         beginning = '<li><a'
#         ending = '</a></li>'
#         start = text.find(beginning, start + 1)
#         end = text.find(ending, end + 1)
#         if end != -1:Variant 1
#             code = code_and_content(text[start:end+len(ending)])[0]
#             content = code_and_content(text[start:end+len(ending)])[1]
#             txt.write(f'{code} - {content} \n')





