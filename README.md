# Download All The Images (from an insta account)
---
## Instructions
* Search for the account name here -> http://picbear.online/
* Proceed to load all of the users images by scrolling to the very bottom of the screen, where no more images load. 
* Open up developer tools for your browser and copy all of the relevant HTML into a text file. 
* Load up the python script in an IDE, ensure that you have all the libraries, rename in the input text file path and run it. 

## Warnings
- This program will also download preview stills of video posts.
- You should be using an adblocker or else you shall see advertisment images as well, which you probably don't want to download.
- The code is so simple it names the files without any leading zeros.
- If you want to delete the "pointless" opencv code, be warned that most of the instagram images don't have metadata which means most of your editor / viewing programs will hate them. Hacky fix is to compress them a tad, and resave to create valid metadata using opencv.

---
## Websites I referenced while creating this.

- https://www.meccanismocomplesso.org/en/opencv-python-load-display-save-images/ (How to open cv)
- https://stackoverflow.com/questions/30229231/python-save-image-from-url/30229298 (How to save images from urls)

## Extra!

- You could use this with any HTML file or website. I choose picbear because no thumbnails, just fullsize insta images and nothing else.

