import requests
import os
from bs4 import BeautifulSoup

srclist=[]
altlist=[]


for run in range(1,2):
    response=requests.get(f"https://hdqwalls.com/movies-wallpapers/page/{run}")
    # print(response.content)
    soup = BeautifulSoup(response.text, "html.parser")
    div = soup.find_all("img")


    print(len(div))
    print(div)
    l=[]
    for i in div:
        print(str(i))
        k=str(i).split()
        len1=len(k)

        l.append(k[len1-1])

    #     print
        print(l)
    print(l)

    m=[]
    for i in l:
       m.append(i.split("="))
    print(m)
    v=[]
    for i in range(len(m)):
        v.append(m[i][1])
    print(v)

    z=[]
    for i in range(1,len(v)-1):
        z.append(v[i])
    print(z)

    x=[]
    for i in z:
        print(i)
        i = i.rstrip(i[-1])
        x.append(i)
        print(i)

    c=[]
    for i in x:
        print(i)
        i = i.rstrip(i[-1])
        c.append(i)
        print(i)
    a=[]
    for i in c:
        print(i)
        i = i.rstrip(i[-1])
        a.append(i)
        print(i)
    q=[]
    for i in a:
        print(i)
        i = i.lstrip(i[0])
        q.append(i)
        print(i)
    # impo
    # with open("abc.jpg","wb") as f:
    #     response=requests.get("https://images.hdqwalls.com/wallpapers/thumb/selena-gomez-rare-beauty-2023-sw.jpg")
    #     f.write(response.content)
    print("finally")
    os.mkdir(f"D:\\Learning only\\abc\\Page{run}")
    g=["A"+str(i) for i in range(1,27)]
    print(g)
    j=0
    for i in q:
        print(i)
        # print(response.content)
        with open(f"D:\\Learning only\\abc\\Page{run}\\"+g[j]+".jpg", "wb") as f:
            txt=i.replace("/thumb","")
            # print(txt)
            response=requests.get(txt)
            f.write(response.content)
            # f.close()
            j+=1

    #     Print the extracted tag
    # print(div.prettify())
    # soup1=BeautifulSoup(response.text,"html.parser")
    # div1=soup1.findall("div",class_="wall-resp col-lg-4 col-md-4 col-sm-4 col-xs-6 column_padding")

    # print(div1)

# text="https://images.hdqwalls.com/wallpapers/thumb/2023-a-plague-tale-requiem-5k-bp.jpg"
# import re 
# a=re.search("/thumb",text)
# print(a)

# # result=text.find("/thumb")
# # print(result)
# txt=text.replace("/thumb","")
# print(txt)
