import requests
import os
from bs4 import BeautifulSoup

def download(userCategory,numOfPages):
    for run in range(1,numOfPages+1):
        srclist=[]

        response=requests.get(f"https://hdqwalls.com/{userCategory}/page/{run}")
        # print(response.content)
        soup = BeautifulSoup(response.text, "html.parser")
        div = soup.find_all("img")
        tempPage=run
        for i in div:
            srclist.append(i['src'])
        print(srclist)

        templist=["A"+str(i) for i in range(1,19)]
        print(templist)

        ifMainDirecExists=os.path.exists(f"D:\\Learning only\\Wallpaper_application\\wallpaper1\\{userCategory}")
        if(ifMainDirecExists==False):
            os.mkdir(f"D:\\Learning only\\Wallpaper_application\\wallpaper1\\{userCategory}")
           

        ifInDireExist=os.path.exists(f"D:\\Learning only\\Wallpaper_application\\wallpaper1\\{userCategory}\\Page{tempPage}")
        if(ifInDireExist):
                listofpics=os.listdir(f"D:\\Learning only\\Wallpaper_application\\wallpaper1\\{userCategory}\\Page{tempPage}")
                for i in listofpics:
                    os.remove(f"D:\\Learning only\\Wallpaper_application\\wallpaper1\\{userCategory}\\Page{tempPage}\\{i}")
                os.rmdir(f"D:\\Learning only\\Wallpaper_application\\wallpaper1\\{userCategory}\\Page{tempPage}")

        os.mkdir(f"D:\\Learning only\\Wallpaper_application\\wallpaper1\\{userCategory}\\Page{tempPage}")
        for k in range(1,len(templist)+1):
            with open(f"D:\\Learning only\\Wallpaper_application\\wallpaper1\\{userCategory}\\Page{tempPage}\\"+templist[k-1]+".jpg", "wb") as f:
                # print(srclist[k])
                txt=srclist[k].replace("/thumb","")
                print(txt)

                response=requests.get(txt)
                f.write(response.content)
                # f.close()
    print("XXXXXXXX Thank you for using this system XXXXXXXX")



# if __name__=="__init__":

categories={1:'latest-wallpapers',
            2:'superheroes-wallpapers',
            3:'movies-wallpapers',
            4:'tv-shows-wallpapers',
            5:'cars-wallpapers',
            6:'games-wallpapers',
            7:'celebrities-wallpapers',
            8:'love-wallpapers',
            9:'sports-wallpapers',
            10:'abstract-wallpapers',
            11:'typography-wallpapers'}

while True:
    userInput=int(input("""Enter the category of wallpapers you want to download :
                        1]All latest wallpapers (mix)
                        2]Superhero
                        3]Movies
                        4]Tv Shows
                        5]Cars
                        6]Games
                        7]Celebrities
                        8]Love
                        9]Sports
                        10]Abstract
                        11]Typography
                        12]exit
                        \n"""))
    if userInput==12:
        break
    if userInput<1 or userInput>12:
        continue
    userPagesReq=int(input("Enter number of pages you want to download : (each page contains 18 wallpapers)"))
    userWants=categories[userInput]
    download(userWants,userPagesReq)
    break