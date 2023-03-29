import ctypes
import time
import random

pageran=random.randint(1,10)
imgran=random.randint(1,10)

path=f"D:\Learning only\webscrapingproject\Page{pageran}\A{imgran}.jpg"  
print(path)
ctypes.windll.user32.SystemParametersInfoW(20,0,path,0)
