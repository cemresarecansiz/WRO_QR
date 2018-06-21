# import the necessary packages
from imutils.video import VideoStream
from pyzbar import pyzbar
import imutils
import time
import cv2
import database_actions


# initialize the video stream and allow the camera sensor to warm up
print("[INFO] starting video stream...")
# vs = VideoStream(src=0).start()
vs = VideoStream().start()
time.sleep(2.0)
dates = []
reps = 0
barcodes = None
prevcode = None
exp_date = []


# loop over the frames from the video stream
while reps<1:
    # grab the frame from the threaded video stream and resize it to
    try:
        while (barcodes == None or barcodes == []):
            frame = vs.read()
            frame = imutils.resize(frame, width=400)
            barcodes = pyzbar.decode(frame)
            cv2.imshow("Image", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        barcodes = pyzbar.decode(frame)
        # loop over the detected barcodes
        for barcode in barcodes:
            (x, y, w, h) = barcode.rect
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

            barcodeData = barcode.data.decode("utf-8")
            barcodeType = barcode.type

            if (barcodeData != prevcode):
                text = "{} ({})".format(barcodeData, barcodeType)
                cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                            0.5, (0, 0, 255), 2)

                print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))
                dates.append(database_actions.getDate(barcodeData))
                reps += 1

            prevcode = barcodeData
            barcodes = None
            cv2.imshow("Image", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    except KeyboardInterrupt:
        break
# close the output CSV file do a bit of cleanup
print("[INFO] cleaning up...")
print dates
cv2.destroyAllWindows()
vs.stop()