from moviepy.editor import *


f = open(os.path.dirname(__file__) + "\\Data\\" + "audioLength.txt", "r")
time_range = f.readlines()
video = VideoFileClip(os.path.dirname(__file__) + "\\Data\\" + "Top20NewsWithBackground.mp4")
for i in range(len(time_range)):
    start, stop = time_range[i].split(",")
    clip = video.subclip(start, stop)
    clip.write_videofile(os.path.dirname(__file__) + "\\Data\\" + "%d.mp4" % i)
