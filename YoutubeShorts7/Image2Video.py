from moviepy.editor import *

# Load the image
image = ImageClip("0.png")

# Set the desired duration in seconds (e.g., 10 seconds)
duration = 10

# Calculate the canvas dimensions (9:16 aspect ratio)
canvas_width = 1080
canvas_height = 1920

# Resize the image to have a height of 1920 pixels and maintain its original aspect ratio
resized_image = image.resize(height=1920)

# Create a black background clip with the canvas dimensions
background = ColorClip(size=(canvas_width, canvas_height), color=(0, 0, 0))

# Calculate the horizontal position to center the image on the canvas
x_position = (canvas_width - resized_image.size[0]) // 2

# Position the resized image on the canvas
final_video = CompositeVideoClip([background.set_duration(duration), resized_image.set_position((x_position, 0)).set_duration(duration)]).set_fps(1)

# Export the video
final_video.write_videofile("output_video.mp4", codec="libx264")
