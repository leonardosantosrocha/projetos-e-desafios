import os
from PIL import Image


root_dir = os.getcwd()


def chapter_treatment(ct_chapter: int, ct_name: str) -> str:
    ct_name = ct_name[0:3].upper()
    if ct_chapter >= 0 and ct_chapter <= 9:
        return f"{ct_name}_00{ct_chapter}.pdf"
    elif ct_chapter >= 10 and ct_chapter <= 99:
        return f"{ct_name}_0{ct_chapter}.pdf"
    elif ct_chapter >= 100 and ct_chapter <= 999:
        return f"{ct_name}_{ct_chapter}.pdf"
    else:
        return f"ERRO DURING CHAPTER TREATMENT!"
        

def mounting_pdf(gf_path: str, gf_chapter: int, gf_name: str) -> bool:
    images = list()
    try:
        i = 0
        os.chdir(gf_path)
        for file in os.listdir(gf_path):
            image = Image.open(fr"{gf_path}/{i}.jpg")
            image = image.convert("RGB")
            images.append(image)
            i += 1
        fileName = chapter_treatment(gf_chapter, gf_name)
        image.save(fileName, save_all = True, append_images = images) 
        print(f"MANGA NUMBER {gf_chapter} IS READY TO BE READ!")
        return True
    except:
        print("ALL PDFS HAVE BEEN GENERATED!")
        return False


def generate_mangas():
    # Defining the current chapter
    current_chapter = int(1)
    # User should define the last chapter, it will be used to stop the downloading loop
    last_chapter = int(input("TYPE THE LAST CHAPTER: "))
    # User should define the manga's name
    manga_name = str(input("TYPE THE MANGA'S NAME: "))

    # While current chapter less than last chapter, we will mount the mangas using the chapters
    while current_chapter <= last_chapter:
        path = f"{os.getcwd()}/chapter {current_chapter}"
        mounting_pdf(path, current_chapter, manga_name)
        current_chapter += 1
        os.chdir(root_dir)


def how_to_use():
    print("====================================== WELCOME TO MANGAPY ======================================\n"
          "| 1 - HOW MANY CHAPTER WOULD YOU LIKE TO CREATE?                                               |\n"
          "| 2 - TYPE THE MANGA'S NAME:                                                                   |\n"
          "| 3 - ENJOY IT                                                                                 |\n"
          "============================ DEVELOPED BY: LEONARDO SANTOS DA ROCHA ============================\n")


def main():
    how_to_use()
    generate_mangas()


main()  
