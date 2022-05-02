import os
from PIL import Image

def gen_file(path:str, chapter:int) -> bool:
    id = list()
    images = list()
    try:
        i = 1
        begin = 1
        os.chdir(path)
        for file in os.listdir(path):
            begin += 1
        for file in os.listdir(path):
            image = Image.open(fr"{path}\{i}.jpg")
            image = image.convert("RGB")
            images.append(image)
            i += 1
        if chapter >= 0 and chapter <= 9:
            fileName = f"KNY_00{chapter}.pdf"
        if chapter >= 10 and chapter <= 99:
            fileName = f"KNY_0{chapter}.pdf"
        if chapter >= 100 and chapter <= 999:
            fileName = f"KNY_{chapter}.pdf"
        image.save(fileName, save_all=True, append_images=images) 
    except:
        print("All pdf have been generated!")

def main():
    chapter = 1
    while True:
        path = fr"{os.getcwd()}+\chapter {chapter}"
        gen_file(path, chapter)
        chapter += 1
        if chapter == 209:
            break

main()  
