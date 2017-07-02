'''
Reference:
http://www.pyimagesearch.com/2015/03/09/capturing-mouse-click-events-with-python-and-opencv/
'''
import cv2
BLUE = (255,0,0)
ref_pt = []
def click_and_crop(event, x, y, flags, image):
    global ref_pt
    if event == cv2.EVENT_LBUTTONDOWN:
        ref_pt = [(x,y)]
    elif event == cv2.EVENT_LBUTTONUP:
        ref_pt.append((x,y))
        cv2.rectangle(image, ref_pt[0], ref_pt[1], BLUE,2)
        cv2.imshow('image',image)

def pick_obj(img_path):
    image = cv2.imread(sys.argv[1])
    clone = image.copy()
    cv2.namedWindow('image')
    cv2.setMouseCallback('image', click_and_crop, image)

    while True:
        cv2.imshow('image', image)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('r'):
            image = clone.copy()
            cv2.setMouseCallback('image', click_and_crop, image)

        if key == ord('c'):
            break

    if len(ref_pt) == 2:
        print 'Reference point: ', ref_pt
        roi = clone[ref_pt[0][1]:ref_pt[1][1], ref_pt[0][0]:ref_pt[1][0]]
        cv2.imshow('ROI', roi)
        cv2.waitKey(0)

    cv2.destroyAllWindows()

if __name__ == '__main__':
    import sys
    pick_obj(sys.argv[1])
