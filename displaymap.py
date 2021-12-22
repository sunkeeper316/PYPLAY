import os
import cv2
# import pandas as pd 

class DisplayMap:
    # A5 Town
    A5_TOWN_START = "a5_town_start"
    A5_STASH = "a5_stash"
    A5_WP = "a5_wp"
    A5_QUAL_KEHK = "a5_qual_kehk"
    A5_MALAH = "a5_malah"
    A5_NIHLATHAK_PORTAL = "a5_nihlathak_portal"
    A5_LARZUK = "a5_larzuk"
    # Pindle
    A5_PINDLE_START = "a5_pindle_start"
    A5_PINDLE_SAVE_DIST = "a5_pindle_save_dist"
    A5_PINDLE_END = "a5_pindle_end"
    # Eldritch
    A5_ELDRITCH_START = "a5_eldritch_start"
    A5_ELDRITCH_SAVE_DIST = "a5_eldritch_save_dist"
    A5_ELDRITCH_END = "a5_eldritch_end"
    # Shenk
    A5_SHENK_START = "a5_shenk_start"
    A5_SHENK_SAVE_DIST = "a5_shenk_save_dist"
    A5_SHENK_END = "a5_shenk_end"
    # A4 Town
    A4_TOWN_START = "a4_town_start"
    A4_WP = "a4_town_wp"
    A4_TYRAEL_STASH = "a4_tyrael_stash"
    A4_VENDOR = "a4_vendor"
    # A3 Town
    A3_TOWN_START = "a3_town_start"
    A3_ORMUS = "a3_ormus"
    A3_STASH_WP = "a3_stash_wp"
    A3_ASHEARA = "a3_asheara"
    # Trav
    A3_TRAV_START = "a3_trav_start"
    A3_TRAV_CENTER_STAIRS = "a3_trav_center_stairs"
    # A2 Town
    A2_TOWN_START = "a2_town_start"
    A2_WP = "a2_wp"
    # A1 Town
    A1_TOWN_START = "a1_town_start"
    A1_WP = "a1_wp"

class ImgPath :
    #A1
    A1_TOWN_START = "assets/templates/a1_town/a1_town_0.png"
    #A2
    A2_TOWN_START = "assets/templates/a2_town/a2_town_0.png"
    #A3
    A3_TOWN_START = "assets/templates/a3_town/a3_town_0.png"
    #A4
    A4_TOWN_START = "assets/templates/a4_town/a4_town_0.png"
    #A5
    A5_TOWN_START = "assets/templates/a5_town/a5_town_0.png"




# 此函數用於讀取圖像，輸入為目錄名稱
def read_directory(directory_name):
    # 此循環用於讀取此文件夾中的每個圖像，目錄名稱是帶有圖像的文件夾名稱。
    array_of_img = []
    
    if directory_name.__contains__(".") :
        return
    else :
        for filename in os.listdir(r"./"+directory_name):
        #print(filename) #just for test
        #img 用於存儲圖像數據
        # img = cv2.imread(directory_name + "/" + filename) #抓取讀項
         # 這如果用於存儲所有圖像路徑
        # array_of_img.append(img) 如果要數據
        #print(img)
            print(f"{directory_name}{filename}") 
            array_of_img.append(f"{directory_name}{filename}")
        # print(array_of_img)   
    return array_of_img

def checkFilesImg(files) :
    imgs = []
    _files = []
    for f in files : 
        print(f"find {f}")
        if f.__contains__(".png") :
            imgs.append(f) 
        elif not f.__contains__(".") :
            _files.append(f)
                
    return imgs , _files

if __name__ == "__main__" :
    
    allImgs = []
    files = read_directory("assets/")

    imgs , _files = checkFilesImg(files)
    # print(_files)
    for img in imgs :
        allImgs.append(img)
    while len(_files) > 0 :
        
        for f in _files :    
            _imgs , __files = checkFilesImg(read_directory(f"{f}/"))
            _files.remove(f)
            for __img in _imgs :
                allImgs.append(__img)
            for _f in __files :
                _files.append(_f)
    print("allImgs-----")
    print(allImgs)

    with open("allImgs.txt" , 'w') as f :
        for img in allImgs :
            f.write(f"{img}\n")
        


    


    