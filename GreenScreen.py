import cv2 as cv # import the library as CV 

cv.namedWindow("Result", cv.WINDOW_NORMAL) # Creating a window with a proper name and size to display my image  

image, background = cv.imread("IronMan.jpg"), cv.imread("Avengers.jpg") # Reading the image and background 

for h in range(697): # looping over the height 
    for w in range(1240): # looping over the width 
        if image[h][w][0] < 150 and image[h][w][1] > 180 and image[h][w][2] < 300:  # Checking the pixel where the green color occur, set it to image[h][w][1] > 180 
               image[h][w][0] = background[h][w][0] # Blue 
               image[h][w][1] = background[h][w][1] # Green
               image[h][w][2] = background[h][w][2] # Red 

cv.imshow("Result", image) # Displaying the image 
cv.waitKey(0) # Wait for the image to be displayed before continuing
cv.destroyAllWindows() # Destroy all windows

