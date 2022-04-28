# Developed by 
#   -> Leonardo Rocha

# Target
#   -> Access different urls, downloading the jpg files and save on my pc automatically 

import os
import requests 
import shutil
import time

CURRENT_DIR = os.getcwd()

def download(url:str, downloadPath:str, image:str) -> bool:
    response = url

    if response.status_code == 200:
        response.raw.decode_context = True
        downloadPath = fr"{downloadPath}\{image}.jpg"
        with open(downloadPath, "wb") as file:
            shutil.copyfileobj(response.raw, file)
        print(f"Image has been downloaded!")
        return True
    else: 
        print(f"All images have been downloaded!\n")
        return False

def main():
    chapter = 1
    while True:
        # Chapter treatment
        if chapter <= 9:
            requestToChapter = requests.get(f"https://cdn.mangayabu.top/mangas/boruto-naruto-next-generations/capitulo-0{chapter}/", stream = True)
        else:
            requestToChapter = requests.get(f"https://cdn.mangayabu.top/mangas/boruto-naruto-next-generations/capitulo-{chapter}/", stream = True)
        # Checking if chapter exists - False
        if requestToChapter.status_code == 404:
            print(f"The chapter doesn't exist!")
            break
        # Checking if chapter exists - True
        else:
            image = 1
            os.mkdir(fr"{CURRENT_DIR}\chapter {chapter}")
            while True:
                # Image treatment
                if chapter <= 9 and image <= 9:
                    requestToImage = requests.get(f"https://cdn.mangayabu.top/mangas/boruto-naruto-next-generations/capitulo-0{chapter}/0{image}.jpg", stream = True)
                elif chapter <= 9 and image > 9:
                    requestToImage = requests.get(f"https://cdn.mangayabu.top/mangas/boruto-naruto-next-generations/capitulo-0{chapter}/{image}.jpg", stream = True)
                elif chapter > 9 and image <= 9:
                    requestToImage = requests.get(f"https://cdn.mangayabu.top/mangas/boruto-naruto-next-generations/capitulo-{chapter}/0{image}.jpg", stream = True)
                else:
                    requestToImage = requests.get(f"https://cdn.mangayabu.top/mangas/boruto-naruto-next-generations/capitulo-{chapter}/{image}.jpg", stream = True)
                
                # Applying the function download to capture the images
                try:
                    returnDownload = download(requestToImage, fr"{CURRENT_DIR}\chapter {chapter}", image)
                except:
                    print("Error")
                if returnDownload == False:
                    break
                image += 1
            chapter += 1
                    
main()
