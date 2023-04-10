from gtts import gTTS
from moviepy.editor import *


def StartProcess():
    f = open(os.path.dirname(__file__) + "\\Data\\" + "newsLinks.txt", "r")
    total_no_of_news = len(f.readlines())
    f.close()

    for i in range(total_no_of_news):
        f = open(os.path.dirname(__file__) + "\\Data\\" + "%s.txt" % i, "r")
        content = "".join(f.readlines())
        TurnOnTheSound(content, i)
        EditProcess(i)
    for i in range(0, len(final), 5):
        end = concatenate_videoclips(final[i:i + 5], method="compose")
        end.write_videofile(os.path.dirname(__file__) + "\\Data\\" + "Top20News%d.mp4" % i)


def TurnOnTheSound(break_news, i):
    obj = gTTS(text=break_news, lang="en", slow=False)
    path = os.path.dirname(__file__) + "\\Data\\%i.mp3" % i
    print(path)
    obj.save(path)


def EditProcess(i):
    global start_time
    audio = AudioFileClip(os.path.dirname(__file__) + "\\Data\\%d.mp3" % i)
    image = ImageClip(os.path.dirname(__file__) + "\\Data\\%d.png" % i)
    video = image.set_audio(audio)
    audio_duration = audio.duration + 1
    f = open(os.path.dirname(__file__) + "\\Data\\" + "audioLength.txt", "a")
    print(start_time, start_time + audio_duration)
    f.write(str(start_time) + ',' + str(start_time + audio_duration) + '\n')
    start_time += audio_duration
    video.duration = audio_duration
    video.fps = 1
    video.write_videofile(os.path.dirname(__file__) + "\\Data\\%d.mp4" % i)
    final.append(video)


final = []
start_time = 00.00
