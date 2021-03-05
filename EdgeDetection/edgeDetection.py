import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images.png',0)
edges = cv2.Canny(img,100,200)

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

# print(edges)
# for arr in edges:
#     print(arr)

f = open("gcode.txt","w")

f.write("G90\n")

for i in range(len(edges)):
    for j in range(len(edges[i])):
        if edges[i][j] == 0 or j == 0:
            f.write("T1\nM6\n")
            f.write(f"G0 X{i} Y{j}\n")

        elif edges[i][j] == 255:
            f.write("T0\nM6\n")
            f.write(f"G0 X{i} Y{j}\n")



f.close()

plt.show()