import os
import matplotlib.pyplot as plt

#script to plot y d/t of sphere centers, t is based off sphere 1

#cur file location
__location__  = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

#returns list of ypoints for a sphere file
def yPoints(str):
    y = []
    t = []
    f = open(os.path.join(__location__, str), 'r')
    for row in f:
        row = row.split(', ')
        y.append(float(row[1]))
        t.append(float(row[3]))
    f.close()
    return y, t

#y coords
y1, t1 = yPoints('sphere1.txt')
y2, _ = yPoints('sphere2.txt')
y3, t3 = yPoints('sphere3.txt')
y4, _ = yPoints('sphere4.txt')
y5, t5 = yPoints('sphere5.txt')
y6, _ = yPoints('sphere6.txt')


plt.plot(t1,y1,'r', label='Sphere 1')
plt.plot(t1,y2,'r:', label='Sphere 2')
plt.plot(t3,y3,'b', label='Sphere 3')
plt.plot(t3,y4,'b:', label='Sphere 4')
plt.plot(t5,y5,'g', label='Sphere 5')
plt.plot(t5,y6,'g:', label='Sphere 6')

plt.xlabel("Time (sec)")
plt.ylabel("Y Coordinate (m)")
plt.legend()

plt.show()



