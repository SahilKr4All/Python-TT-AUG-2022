import urllib.request as url
import bs4

home_path = "https://www.imdb.com"
movie_name = input("Enter Movie Name :").replace(" ","+")
path = "https://www.imdb.com/find?q="+movie_name
response = url.urlopen(path)
data = bs4.BeautifulSoup(response,'lxml')
td = data.find("td",class_="result_text")
a = td.find("a")["href"]

path = home_path+a
response = url.urlopen(path)
data = bs4.BeautifulSoup(response,'lxml')
h1 = data.find("h1",class_="sc-b73cd867-0 eKrKux")
print(f"Movie Name => {h1.text}")
span = data.find("span",class_="sc-7ab21ed2-1 jGRxWM")
print(f"Movie Rating => {span.text}/10.0")
a = data.findAll("a",class_="ipc-title-link-wrapper")
for i in a:
    if i["href"].find("reviews?") != -1:
        a = i["href"]
path = home_path+a
response = url.urlopen(path)
data = bs4.BeautifulSoup(response,'lxml')
a_list=data.findAll("a",class_="title")
print("************** REVIEWS ******************")
for i in range(len(a_list)):
    print(f"{i+1}. {a_list[i].text}")




