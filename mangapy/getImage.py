import os
import requests
import shutil


root_dir = os.getcwd()


def get_image(gi_url: object, gi_download_path: str, gi_current_chapter: int, gi_current_image: int) -> bool:
    response = gi_url
    if response.status_code == 200:
        response.raw.decode_context = True
        download_path = fr"{gi_download_path}/{gi_current_image}.jpg"
        with open(download_path, "wb") as file:
            shutil.copyfileobj(response.raw, file)
        print(f"IMAGE {gi_current_image} FROM CHAPTER {gi_current_chapter} HAS BEEN DOWNLOADED!")
        return True
    else:
        print(f"ALL IMAGES FROM CHAPTER {gi_current_chapter} HAVE BEEN DOWNLOADED!\n")
        return False


def chapter_treatment(ct_url: str, ct_current_chapter: int) -> str:
    if ct_current_chapter <= 9:
        return f"{ct_url}/capitulo-0{ct_current_chapter}/"
    else:
        return f"{ct_url}/capitulo-{ct_current_chapter}/"


def image_treatment(it_url: str, it_current_chapter: int, it_current_image: int) -> str:
    if it_current_chapter <= 9 and it_current_image <= 9:
        return f"{it_url}/capitulo-0{it_current_chapter}/0{it_current_image}.jpg"
    elif it_current_chapter <= 9 and it_current_image > 9:
        return f"{it_url}/capitulo-0{it_current_chapter}/{it_current_image}.jpg"
    elif it_current_chapter > 9 and it_current_image <= 9:
        return f"{it_url}/capitulo-{it_current_chapter}/0{it_current_image}.jpg"
    else:
        return f"{it_url}/capitulo-{it_current_chapter}/{it_current_image}.jpg"


def download():
    # Defining the current chapter
    current_chapter = int(1)
    # User should type the url using the following pattern: https://cdn.mangayabu.top/mangas/naruto
    url = str(input("TYPE THE URL: ")).lower()
    # User should define the last chapter, it will be used to stop the downloading loop
    last_chapter = int(input("TYPE THE LAST CHAPTER: "))

    # While current chapter less than last chapter, we will download the images
    while current_chapter <= last_chapter:
        # Using the chapter_treatment function to organize our url
        url_chapter = chapter_treatment(url, current_chapter)
        # Verifying if the current chapter is available
        request_to_chapter = requests.get(url_chapter, stream=True)
        # If the current chapter doesn't exist
        if request_to_chapter.status_code == 404:
            print(f"THE CHAPTER DOESN'T EXIST!")
            # User should choose stop or continue the execution
            option = str(input("WOULD YOU LIKE TO TRY THE NEXT CHAPTER (Y/N): "))
            # Checking the next chapter
            if option.upper() == "Y":
                current_chapter += int(1)
            # Stopping the program
            else:
                break
        # If the current chapter exists
        else:
            # Defining the current image
            current_image = int(0)
            # Creating a new directory to store the current chapter
            os.mkdir(fr"{root_dir}/chapter {current_chapter}")
            while True:
                # Using the image_treatment function to organize our url
                url_image = image_treatment(url, current_chapter, current_image)
                # Verifying if the current chapter is available
                request_to_image = requests.get(url_image, stream=True)
                # Trying to get image based on treated url, directory, current chapter and current image
                try:
                    ret_get_image = get_image(request_to_image, fr"{root_dir}/chapter {current_chapter}",
                                              current_chapter, current_image)
                    # If get_image return is false, we should stop the program
                    if ret_get_image == False:
                        break
                # Treating exceptions
                except NameError:
                    print(NameError)
                current_image += 1
            current_chapter += 1


def how_to_use():
    print("====================================== WELCOME TO MANGAPY ======================================\n"
          "| 1 - ACCESS 'HTTPS://MANGAYABU.TOP/'                                                          |\n"
          "| 2 - CLICK ON YOUR FAVORITE MANGA'S NAME                                                      |\n"
          "| 3 - SELECT THE FIRST CHAPTER                                                                 |\n"
          "| 4 - RIGHT BUTTON ON THE FIRST IMAGE AND OPEN IMAGE IN A NEW TAB                              |\n"
          "| 5 - YOU WILL GOT A LINK LIKE 'HTTPS://CDN.MANGAYABU.TOP/MANGAS/NARUTO/CAPITULO-01/00.JPG'    |\n"
          "| 6 - CUT THE FIRST PART 'HTTPS://CDN.MANGAYABU.TOP/MANGAS/NARUTO/'                            |\n"
          "| 7 - PAST THE NEW ADDRESS ON OUR PROGRAM AND PRESS ENTER                                      |\n"
          "| 8 - SELECT HOW MANY CHAPTERS WOULD YOU LIKE TO DOWNLOAD AND PRESS ENTER                      |\n"
          "| 9 - ENJOY IT                                                                                 |\n"
          "============================ DEVELOPED BY: LEONARDO SANTOS DA ROCHA ============================\n")


def main():
    how_to_use()
    download()


main()
