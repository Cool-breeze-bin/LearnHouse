import cv2

def cvcamera():
    cap = cv2.VideoCapture(0)
    cap.set(3,640)
    cap.set(4,480)
    cap.set(10,100)

    while True:
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    cvcamera()