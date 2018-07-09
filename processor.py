import re
import requests
import cv2 as cv

file = open("PATH TO YOUR HTML INPUT FILE HERE.txt","r")
text = file.readlines()

expression = re.compile('<img[^>]+src="([^">]+)"') #Pattern matching on the image src value.
imageURLS = []

#Go through each line of the HTML, find all the image srcs and add them to an accumulative array.
for line in text:
    urlsFound = expression.findall(line) 
      for url in urlsFound:
          imageURLS.append(url)

print("Got the URLs.")
numberOfImagesDownloaded = 0

for url in imageURLS:
    print(numberOfImagesDownloaded)                       #My equivalant of a loading bar. 
    filename = str(numberOfImagesDownloaded) + ".jpg"     #You can make this fancier if you want.
    #Make a request for that image file
    r = requests.get(url, allow_redirects=True) 
    #Write the image file data into an image file located beside your python code.
    open(filename, 'wb').write(r.content)
    
    #Load the same image file into an opencv image.
    img = cv.imread(filename)
    #Immedaitely rewrite the image file as a jpg, at maximum possible compression quality (100) 
    #For smaller files and greater loss, use a smaller value instead of 100.
    cv.imwrite(filename,img,[int(cv.IMWRITE_JPEG_QUALITY), 100])
    numberOfImagesDownloaded += 1
