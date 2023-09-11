import telnetlib
from ftplib import FTP
import time
import cv2
# from ultralytics import YOLO

# Set up the timer variables
interval = 2  # Time interval in seconds
prev_time = time.time()

# cognex's config
ip = "192.168.3.66"
user = 'admin'
password = '123456'

# model = YOLO("film_error_best.pt")
fileSavePath = "D:\Learning_Python\PythonProject\Image"
# out = cv2.VideoWriter('output.mp4', -1, 20.0, (640,480))



while True:
    try:
        start_time = time.time()
        tn = telnetlib.Telnet(ip)
        tn.read_until(b"User: ")
        tn.write(user.encode('ascii') + b"\r\n")
        # print("fill user")

        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\r\n")
        # print("fill password")

        response = tn.read_until(b"\r\n")
        # print(response)

        # time.sleep(0.1)
        tn.write(b"SE8\r\n")
        # response = tn.read_until(b"\n")

        # time.sleep(0.1)

        ftp = FTP(ip)
        ftp.login(user, password)

        # ftp.sendcmd('get image.bmp\r\n')
        # print("--- %s seconds ---" % (time.time() - start_time))

        filename = 'image.bmp'
        rename = 'image_get.bmp'
        lf = open(rename, "wb")
        ftp.retrbinary("RETR " + filename, lf.write)
        lf.close()

        image = cv2.imread(rename)
        cv2.imshow('Image', image)
        # try:
        #     results = model.predict(show=True, source=image)
        # except:
        #     print("Something wrong")

        # Calculate the elapsed time since the last save
        curr_time = time.time()
        elapsed_time = curr_time - prev_time

        # Check if the elapsed time has reached the desired interval
        # print(str(elapsed_time))
        # print(str(interval))
        # if elapsed_time >= interval:
        #     # Save the frame as an image
        #     cv2.imwrite(fileSavePath + "\image" + str(time.time())+".png", image)
        #
        #     # Update the previous time
        #     prev_time = curr_time
        # print("--- %s seconds ---" % (time.time() - start_time))
        # out.write(image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    except:
        print("Error")

cv2.destroyAllWindows()
