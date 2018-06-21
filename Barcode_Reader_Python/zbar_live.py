from pyzbar import pyzbar
import cv2
import database_actions

dates = []
reps = 0
barcodes = None
prevcode = None
exp_date = []
cam = cv2.VideoCapture(0)
while (reps < 2):
    while (barcodes == None or barcodes == []):
        ret, image = cam.read()
        barcodes = pyzbar.decode(image)
        cv2.imshow("Image", image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    for barcode in barcodes:

        (x, y, w, h) = barcode.rect
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type
        if (barcodeData != prevcode):
            text = "{} ({})".format(barcodeData, barcodeType)
            cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (0, 0, 255), 2)

            print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))
            dates.append(database_actions.getDate(barcodeData))
            exp_date.append(int(barcodeData))
            reps += 1

        prevcode = barcodeData
        barcodes = None
        cv2.imshow("Image", image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

print dates
