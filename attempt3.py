import requests
import os
from bs4 import BeautifulSoup

srclist=[]



for run in range(1,10):
    srclist=[]

    response=requests.get(f"https://hdqwalls.com/latest-wallpapers/page/{run}")
    # print(response.content)
    soup = BeautifulSoup(response.text, "html.parser")
    div = soup.find_all("img")
    tempPage=run
    for i in div:
        srclist.append(i['src'])
    print(srclist)

    templist=["A"+str(i) for i in range(1,19)]
    print(templist)

    ifexist=os.path.exists(f"D:\\Learning only\\Wallpaper_application\\wallpaper1\\Page{tempPage}")
    if(ifexist):
            listofpics=os.listdir(f"D:\\Learning only\\Wallpaper_application\\wallpaper1\\Page{tempPage}")
            for i in listofpics:
                os.remove(f"D:\\Learning only\\Wallpaper_application\\wallpaper1\\Page{tempPage}\\{i}")
            os.rmdir(f"D:\\Learning only\\Wallpaper_application\\wallpaper1\\Page{tempPage}")

    os.mkdir(f"D:\\Learning only\\Wallpaper_application\\wallpaper1\\Page{tempPage}")
    for k in range(1,len(templist)+1):
        with open(f"D:\\Learning only\\Wallpaper_application\\wallpaper1\\Page{tempPage}\\"+templist[k-1]+".jpg", "wb") as f:
            # print(srclist[k])
            txt=srclist[k].replace("/thumb","")
            print(txt)

            response=requests.get(txt)
            f.write(response.content)
            # f.close()