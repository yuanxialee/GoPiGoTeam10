from moviepy.editor import VideoFileClip
from moviepy.editor import ImageSequenceClip
import matplotlib.image as mpimg
import glob
import os
import cv2
import numpy as np
import re
import sys

# execute the script by
# $ python file start_time end_time delta_t
# start_time: the time when the robot start tracking
# end_time: the time when the robot finish tracking
# delta_t: sample frequency of robot
def sort_str(l):
    ''' sort filename by integers'''
    idx = []
    for string in l:
        idx.append(int(re.search(r'\d+', string).group()))
        #print idx[-1]
    return [x for (y,x) in sorted(zip(idx,l))]

path = sys.argv[1]
videoname = path + '/' + path +'.MOV'
if len(path) > 0:
    path = path + '/'
# Make sure image files are well-organized
if not os.path.exists(path+'robotcam'):
    raise Exception('Make sure you have robotcam images')
if not os.path.exists(path+'binary'):
    raise Exception('Make sure you have binary images')
if not os.path.exists(path+'centered'):
    raise Exception('Make sure you have centered images')

# glob and sort filenames
robocam_list = sort_str(glob.glob(path+'robotcam/*.jpg'))
centered_list = sort_str(glob.glob(path+'centered/*.jpg'))
binary_list = sort_str(glob.glob(path+'binary/*.jpg'))
print 'binary list: ',len(binary_list)
print 'robocam list: ',len(robocam_list)
print 'centered list', len(centered_list)
if not len(binary_list) == len(robocam_list) == len(centered_list):
    raise Exception('Different number of files')
if not os.path.exists('merged'):
    os.makedirs('merged')

for i in range(len(binary_list)):
    robotcam = cv2.imread(robocam_list[i])
    centered = cv2.imread(centered_list[i])
    binary = cv2.imread(binary_list[i])
    merged = np.concatenate((robotcam,binary, centered),axis = 0)
    cv2.imwrite('merged/merged'+str(i)+'.jpg', merged)

# uncomment if you wnat to make merged video
#clip = ImageSequenceClip('merged', fps=2)
#clip.write_videofile('merged.mp4', audio = False)


# In[3]:

robocam_num = len(robocam_list)
frame_num = 2602
# uncomment if you need to calculate number of frames in the video
#clip = VideoFileClip(videoname)
#frame_num = 0
#for frame in clip.iter_frames():
#    frame_num += 1

print 'Number of robot views: ', robocam_num
print 'Number of frame : ', frame_num

def process_frame(img):
    global count, script
    #print 'img ', img.shape
    i = script[count]
    img = rotateImage(img)
    resized = cv2.resize(img, (0,0), fx = 0.75, fy = 0.75)
    w, h, c = resized.shape
    output = np.zeros((w, h+720,3), np.uint8)
    output[0:w,0:h,:] = resized[:,:,:]

    robotcam = mpimg.imread(robocam_list[i])
    centered = mpimg.imread(centered_list[i])
    bw = mpimg.imread(binary_list[i])
    binary = np.zeros((bw.shape[0],bw.shape[1],3),np.uint8)
    binary[:,:,0] = binary[:,:,1] = binary[:,:,2] = bw
    #print 'robocam ', robotcam.shape
    #print 'centered ',centered.shape
    #print 'binary ', binary.shape
    output[:,h:,:] = np.concatenate((robotcam,binary, centered),axis = 0)
    count += 1
    return output

def rotateImage(image):
    ''' Rotate frame image by -90 degrees'''
    w, h , c = image.shape
    rotated = np.zeros((h,w,c),np.uint8)
    for i in xrange(3):
        rotated[:,:,i] = image[::-1,:,i].T
    return rotated

#start_sec = 17  # when robot start tracking
#end_sec = 98    # when robot finish tracking
#delta = 2.4
start_sec = int(sys.argv[2])
end_sec = int(sys.argv[3])
delta = float(sys.argv[4])
fps = 29

script = []
for i in xrange(start_sec * fps):
    script.append(1)

for i in xrange(robocam_num-3):
    # each run takes about 60 frames
    for j in xrange(int(delta*fps)):
        # robot start tracking after cam 3
        script.append(3+i)
for i in range(len(script), 2603):
    script.append(-1)
if max(script) != len(robocam_list)-1:
    raise Exception('Script and robot cam do not match. Check the number of pictures in robotcam')

count = 0

output = 'spyndra_lab4.mp4'
clip = VideoFileClip(videoname)
newclip = clip.fl_image(process_frame)
newclip.write_videofile(output, audio=False)
