import os
import cv2

path = "Images/"

images = []

for file in os.listdir(path):
    name, extension = os.path.splitext(file)
    if extension in ['.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+'/'+file
        print("File Name: {file_name}")
        images.append(file_name)

count = len(images)

frame = cv2.imread(images[0])
height, width, channels = frame.shape
size = (width, height)

print(f"Size: {size}")

out = cv2.VideoWriter('Project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)

for i in range(count):
    img = cv2.imread(images[i])
    out.write(img)

out.release()
print("Done")
