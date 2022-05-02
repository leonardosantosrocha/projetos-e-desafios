import os
import requests 
import shutil
import time

CURRENT_DIR = os.getcwd()

def download(url:str, downloadPath:str, image:str) -> bool:
    response = url
    # Checking if the url is valid - True
    if response.status_code == 200:
        response.raw.decode_context = True
        downloadPath = fr"{downloadPath}\{image}.jpg"
        with open(downloadPath, "wb") as file:
            shutil.copyfileobj(response.raw, file)
        print(f"Image has been downloaded!")
        return True
    # Checking if the url is valid - False
    else: 
        print(f"All images have been downloaded!\n")
        return False
    
def main():
    # Initial chapter
    chapter = 1
    while True:
        # Chapter treatment - adding 0 to chapter
        if chapter <= 9:
            requestToChapter = requests.get(f"https://mangayabu.top/mangas2/kimetsu-no-yaiba/capitulo-0{chapter}/", stream = True)
        # Chater treatment - pass
        else:
            requestToChapter = requests.get(f"https://mangayabu.top/mangas2/kimetsu-no-yaiba/capitulo-{chapter}/", stream = True)
        # If the chapter doesnt exist
        if requestToChapter.status_code == 404:
            print(f"The chapter doesn't exist!")
            break
        # If the chapter exists
        else:
            image = 1
            os.mkdir(fr"{CURRENT_DIR}\chapter {chapter}")
            while True:
                # Image treatment - adding 0 to chapter and image
                if chapter <= 9 and image <= 9:
                    requestToImage = requests.get(f"https://mangayabu.top/mangas2/kimetsu-no-yaiba/capitulo-0{chapter}/0{image}.jpg", stream = True)
                # Image treatment - adding 0 to chapter
                elif chapter <= 9 and image > 9:
                    requestToImage = requests.get(f"https://mangayabu.top/mangas2/kimetsu-no-yaiba/capitulo-0{chapter}/{image}.jpg", stream = True)
                # Image treatment - adding 0 to image
                elif chapter > 9 and image <= 9:
                    requestToImage = requests.get(f"https://mangayabu.top/mangas2/kimetsu-no-yaiba/capitulo-{chapter}/0{image}.jpg", stream = True)
                # Image treatment - pass
                else:
                    requestToImage = requests.get(f"https://mangayabu.top/mangas2/kimetsu-no-yaiba/capitulo-{chapter}/{image}.jpg", stream = True)
                # Applying the function download to capture the images
                try:
                    returnDownload = download(requestToImage, fr"{CURRENT_DIR}\chapter {chapter}", image)
                # Treatment unexpected errors
                except:
                    print("Error")
                if returnDownload == False:
                    break
                image += 1
            # Final chapter
            if chapter == 209:
                break
            chapter += 1
            
main()
