import cv2

def convertLength(length, img):

    # Load the video
    video = cv2.VideoCapture('background.mp4')
    image = cv2.imread(str(img)+".png")
    # Get the frames per second (fps) of the video
    fps = int(video.get(cv2.CAP_PROP_FPS))
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    # Get the dimensions of the image
    image_width = width
    image_height = 1000

    # Calculate the center coordinates of the video frame
    x = (width - image_width) // 2
    y = (height - image_height) // 2

    # Set the time limit in seconds
    time_limit = length

    # Calculate the number of frames to loop
    frames_to_loop = fps * time_limit

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('editedBackground.mp4', fourcc, fps, (int(video.get(3)), int(video.get(4))))
    cap_frame = 0
    print("processing....")
    while True:
        # Capture frame-by-frame
        ret, frame = video.read()

        if ret:
            # Resize the image to match the size of the video frame
            resized_image = cv2.resize(image, (image_width, image_height))

            # Add the image to the frame
            frame[y:y + image_height, x:x + image_width] = resized_image

            out.write(frame)
            cap_frame += 1
            # Check if we have reached the end of the video or time limit
            if cap_frame >= frames_to_loop:
                break

        else:
            # If we have reached the end of the video, start over from beginning
            video.set(cv2.CAP_PROP_POS_FRAMES, 0)

    # Release everything if job is finished
    video.release()
    out.release()
    cv2.destroyAllWindows()
