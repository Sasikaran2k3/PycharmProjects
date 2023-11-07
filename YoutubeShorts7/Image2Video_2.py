from moviepy.editor import *

# Load the image with the filename "0.png"
image = ImageClip("0.png")

# Set the desired duration in seconds (e.g., 10 seconds)
duration = 5

# Calculate the canvas dimensions (9:16 aspect ratio)
canvas_width = 1080
canvas_height = 1920

# Resize the image to have a height of 1920 pixels and maintain its original aspect ratio
resized_image = image.resize(height=1920)

# Create a black background clip with the canvas dimensions
background = ColorClip(size=(canvas_width, canvas_height), color=(0, 0, 0))

# Calculate the horizontal position to start the image on the left side of the canvas
x_start_position = 0

# Calculate the horizontal position to end the image on the right side of the canvas
x_end_position = canvas_width - resized_image.size[0]

# Create a function to animate the image's horizontal position
def move_image_horizontal(t):
    x_position = int(x_start_position + (x_end_position - x_start_position) * t / duration)
    return x_position, 0

# Animate the image's horizontal position within the given duration
animated_image = resized_image.set_position(move_image_horizontal).set_duration(duration)

# Combine the background and animated image
final_video = CompositeVideoClip([background.set_duration(duration), animated_image]).set_fps(24)

# Export the video
final_video.write_videofile("output_video.mp4", codec="libx264")
