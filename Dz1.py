
import numpy as np
from matplotlib import pyplot as plt

f = open("E:\Голубов 7сем\\examp8.txt", 'r')
data_raw = f.readlines()
f.close()
n = len(data_raw)
data = np.zeros((n, 684))
for i in range(n):
    line = data_raw[i]
# for line in data_raw:
    a = line.replace(',', '')
    a = a.replace(';', '')
    a = a.split()
    new_line = list(map(float,a))
    # data.append(new_line)
    data[i,:] = new_line

x, y, angle = data[:,0], data[:,1], data[:,2]

beta = 240.0/681

plt.figure(1)
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')

for i in range(n):
    for j in range(3,684):
        if 2.0 < data[i,j] < 5.6:
            theta = (beta*(j-2) - 120)*np.pi/180 - angle[i]
            plt.plot(np.cos(theta)*(data[i,j]+0.3)+x[i], np.sin(theta)*(data[i,j]+0.3)+y[i], '.r', markersize=0.4)

plt.show()

figure.canvas.draw()
plotimage = np.frombuffer.(figure.canvas.tostring_rgb(), dtype=np.uint8)
ris = cv.cvtColor(plotimage.reshape(figure.canvas.get_wifth_height(_)[::-1]+(3,)), cv.COLOR_RGBA2BGR)
ris = ris[60:420, 82:650, :]
im1 = np.zeors(ris.shape)+255
im2 = im1.copy)()

plt.show()
