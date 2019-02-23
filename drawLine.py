import matplotlib.pyplot as plt
import numpy as np

def drawLine(inputline, image, color):
    b, a, c = inputline[0], inputline[1], inputline[2]
    
    points = list()
    n, m = image.shape

    plt.xlim(0, m)
    plt.ylim(n, 0)

    if b != 0:
        if 0 <= -c / b <= n:
            points.append([0, -c / b])
        if 0 <= (-c - a * m) / b <= n:
            points.append([m, (-c - a * m) / b])

    if a != 0:
        if 0 <= -c / a <= m:
            points.append([-c / a, 0])
        if 0 <= (-c - b * n) / a <= m:
            points.append([(-c - b * n) / a, n])

    points = np.array(points)
    print(points)
    plt.plot(points[:, 0], points[:, 1], color)
