import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('test.jpg',0)
edges = cv2.Canny(img,100,200)

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

# print(edges[0])
# for arr in edges:
#     print(arr)


edges = list(edges)
# clear top
for _ in range(len(edges)):
    if np.all((edges[0] == 0)) == True:
        # print(np.all((edges[0] == 0)))
        edges.pop(0)
    else:
        break

# clear buttom 
for _ in range(len(edges)):
    if np.all((edges[len(edges)-1] == 0)) == True:
        edges.pop(len(edges)-1)
    else:
        break

# clear left
# for i in range(len(edges)):
#     total = 0
#     for j in range(len(edges)):
#         total += edges[j][0]
#     if total == 0:
#         for j in range(len(edges)):
#             edges[j].pop(0)
#     else:
#         break

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