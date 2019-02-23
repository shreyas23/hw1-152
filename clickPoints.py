import matplotlib.pyplot as plt
import numpy as np

def clickPoints(image, n, plot_status = 0, label_status = 0):
    plt.imshow(image, cmap = 'gray')
    font = {'color': 'green', 'size' : 12}
    points = np.zeros(shape = (n + 1, 2))
    for i in range(n + 1):
        points[i] = np.array(plt.ginput(1, show_clicks = False))
        
        if i == n:
            continue
        
        if plot_status == 1:
            plt.scatter(*points[i].T, c = 'r', marker = '+')
            plt.draw()
        
        if label_status == 1:
            plt.text(*points[i].T + 0.25, i + 1, font)
            plt.draw()
    
    plt.close()
    return points[:n, :]




