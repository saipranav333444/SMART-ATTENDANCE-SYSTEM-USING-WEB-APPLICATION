import cv2

cam_port = 0  # Use 0 for the default camera (you may need to change this value based on your system)
cam = cv2.VideoCapture(cam_port)

# Reading the input using the camera
inp = input('Enter person name: ')

# If the image is detected without any error, show the result
while True:
    result, image = cam.read()
    cv2.imshow(inp, image)

    key = cv2.waitKey(1) & 0xFF

    # Break the loop if 'q' is pressed
    if key == ord('q'):
        break
    # If the Enter key is pressed, save the image
    elif key == 13:  # 13 is the ASCII code for the Enter key
        cv2.imwrite("C:/Users/DELL/Desktop/qwert/images/" + inp + ".png", image)
        print("Image taken")

# Release the camera
cam.release()
cv2.destroyAllWindows()
