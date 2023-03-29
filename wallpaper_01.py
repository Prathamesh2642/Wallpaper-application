import ctypes
import time

for i in range(1,11):
    path=f"D:\Learning only\webscrapingproject\Page1\A{i}.jpg"  
    print(path)
    ctypes.windll.user32.SystemParametersInfoW(20,0,path,0)
    time.sleep(10)