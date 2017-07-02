import cv2
import numpy as np 

def geodesic_dilation(mask, seed):
    ''' Geodesic dilation '''
    marker = np.zeros(mask.shape, np.uint8)
    marker[seed[0],seed[1]] = 255
    kernel = np.ones((15,15),np.uint8)
    x,y= np.nonzero(marker)
    prev = len(x)
    while True:
        marker = cv2.dilate(marker, kernel) & mask
        x, y = np.nonzero(marker)

        # uncomment if you want to see the process
        #cv2.imshow('marker', marker)
        #cv2.waitKey(0)

        # too noisy so the centroid/seed is not
        # in the ball region
        if len(x) == 0:
            return bw

        # if the area does not change anymore
        # return the geodesic dilation
        if len(x) == prev:
            break
        prev = len(x)
    return marker

def color_filter(filepath):
    img = cv2.imread(filepath)

    # calculate mean of h, s and v channels
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    avg = np.mean(np.mean(hsv,axis=0),axis=0, dtype = int)
    print '(H, S, V) = ({}, {}, {})'.format(avg[0],avg[1],avg[2])

    # color thresholding
    # manually designed for the softball
    lower = (20, 140, 0)
    upper = (60, 220,255)
    mask = cv2.inRange(hsv, lower, upper)

    # morphological processing
    kernel = np.ones((20,20),np.uint8)
    clean = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    kernel = np.ones((5,5),np.uint8)
    clean = cv2.morphologyEx(clean, cv2.MORPH_OPEN, kernel)

    # calculate the centroid of object
    x, y = np.nonzero( clean )
    center = (int(np.mean(x)), int(np.mean(y))) 
    area = len( x )

    filled = geodesic_dilation(clean,center)
    # update the centroid of object
    x, y = np.nonzero( filled )
    center = (int(np.mean(x)), int(np.mean(y))) 
    area = len( x )

    # mark the centroid on robot camera
    # notice that the x and y are reversed in cv2
    cv2.circle(img, (center[1], center[0]), 5, (0,0,255), thickness=-1)
    cv2.imwrite(filepath+'_centered.jpg', img)
    cv2.imwrite(filepath+'_binary.jpg', filled)

    return center, area

if __name__ == '__main__':
    '''
    for i in xrange(10):
        center, area = color_filter('img'+str(i)+'.jpg')
        print 'Centroid: ({}, {})'.format(center[0], center[1])
        print 'Area: {}'.format(area)
    '''
    import sys
    print color_filter(sys.argv[1])
