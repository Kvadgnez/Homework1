
import numpy as np
from matplotlib import pyplot as plt

f = open("Telegram Desktop\examp8.txt", 'r')
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

theta = np.radians(np.linspace(-120, 121, 681))

for i in range(n):
    for j in range(3,684):
        if 2.0 < data[i,j] < 5.6:
            plt.scatter(np.cos(angle[i]-theta[j])*(data[i,j])+x[i]+0.3*np.cos(angle[i]), np.sin(angle[i]-theta[j])*(data[i,j])+y[i]+0.3*np.sin(angle[i]))


plt.show()
