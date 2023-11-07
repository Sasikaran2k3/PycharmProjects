import datetime
import time
from moviepy.editor import *
from selenium.webdriver import Chrome, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

import StartBrowser


def KapwingEdit():
    browser.get("https://www.kapwing.com/folder/")

    # Create Workspace and make new project
    browser.find_element(By.XPATH, '//div[@data-cy="workspace-new-project-button"]').click()
    create = browser.find_elements(By.XPATH, '//div[text() = "Create a New Project"]')

    # if no of workspace is less than 3
    if create: create[0].click()

    # Upload video
    browser.find_element(By.XPATH, '//input[@data-cy="upload-input"]').send_keys(
        os.path.dirname(__file__) + "\\Data\\" + "%s.mp4" % date)
    print("Video Sent")
    time.sleep(10)

    wait = WebDriverWait(browser, 1000)
    ActionChains(browser).send_keys(Keys.ESCAPE).perform()

    # Pressing Subtitle Buttons
    browser.find_element(By.XPATH, '//div[text() = "Subtitles"]').click()
    browser.find_element(By.XPATH, '//span[text() = "Auto subtitles"]').click()
    while browser.find_elements(By.XPATH, '//span[text() = "Auto Subtitle"]'):
        browser.find_element(By.XPATH, '//span[text() = "Auto Subtitle"]').click()
    print("Waiting in Subtitle")

    # Wait till subtitle appears
    wait.until(expected_conditions.invisibility_of_element((By.XPATH, "//span[text()='Generating Subtitles...']")))
    wait.until(expected_conditions.presence_of_element_located((By.XPATH, '//textarea[@data-cy="magic-textarea"]')))
    print("Sub Ready")

    # Select Subtitle
    browser.find_element(By.XPATH, '//textarea[@data-cy="magic-textarea"]').click()
    act = ActionChains(browser)
    transform = browser.find_elements(By.XPATH, '//div[@data-cy="drag-handler"]')

    # Move the subtitle to Center by slowly changing y axis and stop when grid/Snap line is approched twice
    y_axis = 200
    grid_line = '//div[@class="SnapLines-module_line_Iuyzq"]'
    count_of_snap = 0
    while True:
        act.click_and_hold(transform[1]).move_to_element_with_offset(transform[0], 85, y_axis).perform()
        if len(browser.find_elements(By.XPATH, grid_line)) == 2:
            count_of_snap += 1
        act.release().perform()
        if count_of_snap == 2:
            break
        print("Y Axis: " + str(y_axis))
        y_axis -= 5
    print("Placed Center")

    # Selects the subtitle style
    parent = browser.find_elements(By.XPATH, '//div[@class="PresetPreview-module_container_034hO"]')
    for i in parent:
        if i.find_element(By.TAG_NAME, 'input').get_attribute("value") == "My":
            i.click()
            break
    browser.find_element(By.CSS_SELECTOR, 'div[data-cy="create-button"]').click()

    # Export Panel
    browser.find_element(By.CSS_SELECTOR, 'div[data-cy="export-panel-create-button"]').click()
    time.sleep(5)
    browser.find_element(By.CSS_SELECTOR,
                         'div[class = "common-module_smallControlButton_66vuT ExportRow-module_buttonStyle_L6WYa '
                         'ExportRow-module_studioColor_ltubC "]').click()
    time.sleep(7)
    print("Download Page")

    # Waits till the size of the file appears and then dowload button is clicked
    wait = WebDriverWait(browser, 1000)
    wait.until(expected_conditions.visibility_of_element_located(
        (By.XPATH, '//div[@class="VideoContainer-module_commentsMetaDataFileSize_E7zW4"]')))
    browser.find_element(By.XPATH, '//button[@data-cy="download-final-video-button"]').click()


def ImageAnimation(ImageClip, duration, flag):
    # Load the image
    image = ImageClip

    # Set the desired duration in seconds (e.g., 10 seconds)
    duration = duration

    # Calculate the canvas dimensions (9:16 aspect ratio)
    canvas_width = 1080
    canvas_height = 1920

    # Resize the image to have a height of 1920 pixels and maintain its original aspect ratio
    resized_image = image.resize(height=1920)

    # Create a black background clip with the canvas dimensions
    background = ColorClip(size=(canvas_width, canvas_height), color=(0, 0, 0))

    # Calculate the horizontal position to start the image on the left side of the canvas
    x_start_position_left = 0

    # Calculate the horizontal position to end the image on the right side of the canvas
    x_end_position_left = canvas_width - resized_image.size[0]

    # Create a function to animate the image's horizontal position to move left
    def move_image_left(t):
        x_position = int(x_start_position_left + (x_end_position_left - x_start_position_left) * t / duration)
        return x_position, 0

    # Calculate the horizontal position to start the image on the right side of the canvas
    x_start_position_right = x_end_position_left

    # Calculate the horizontal position to end the image on the left side of the canvas
    x_end_position_right = x_start_position_left

    # Create a function to animate the image's horizontal position to move right
    def move_image_right(t):
        x_position = int(x_start_position_right + (x_end_position_right - x_start_position_right) * t / duration)
        return x_position, 0

    if flag == "L":
        # Animate the image's horizontal position to move left within the given duration
        animated_image_left = resized_image.set_position(move_image_left).set_duration(duration)
        final = CompositeVideoClip([background.set_duration(duration), animated_image_left]).set_fps(24)
    else:
        # Animate the image's horizontal position to move right within the given duration
        animated_image_right = resized_image.set_position(move_image_right).set_duration(duration)
        final = CompositeVideoClip([background.set_duration(duration), animated_image_right]).set_fps(24)
    return final


date = "".join(str(datetime.date.today()).split("-"))
audio = AudioFileClip(os.path.dirname(__file__) + "\\Data\\%s.mp3" % date)
back = AudioFileClip(os.path.dirname(__file__) + "\\Background.mp3")
final = []

# No of image Shifts
shift_count = 4
divider = audio.duration / shift_count

for i in range(shift_count):
    pic_num = i % 4
    print(pic_num)
    img = ImageClip(os.path.dirname(__file__) + "\\Data\\%s_%d.png" % (date, pic_num))
    img = ImageAnimation(img, divider, flag="L" if i % 2 == 0 else "R")
    final.append(img)

# Combine all the small video to full video
out = concatenate(final,method="compose")
out = out.set_audio(CompositeAudioClip([audio, back]))
out.duration = divider * shift_count + 0.5
print(out.duration)
out_len = divider * shift_count + 0.5
out = out.subclip(0, out_len)
out.write_videofile(os.path.dirname(__file__) + "\\Data\\%s.mp4" % date, fps=24)

browser = StartBrowser.Start_Lap("UpgradeBuddy")

# Delete Old final video
l = os.listdir(os.path.dirname(__file__))
for i in l:
    if ".mp4" in i:
        os.remove(os.path.dirname(__file__) + "\\" + i)

count = 0
while True:
    try:
        KapwingEdit()
        time.sleep(20)
        l = os.listdir(os.path.dirname(__file__) + "\\Data")
        details = {}
        for i in l:
            if ".mp4" in i:
                details[time.ctime(os.path.getmtime(os.path.dirname(__file__) + "/Data/" + i))] = i
        os.rename(os.path.dirname(__file__) + "/Data/" + details[max(details)],
                  os.path.dirname(__file__) + "/%s.mp4" % date)
        print(details[max(details)])
    except Exception as e:
        print(e)
        count += 1
        if count > 10:
            print("Kapwing Error")
            break
    else:
        browser.quit()
        break
