import numpy as np
import matplotlib.pyplot as plt

def plotmatches(image1, image2, corr1, corr2):
    fig = plt.figure(figsize = (15, 15))
    image = np.hstack((image1, image2))

    plt.imshow(image, cmap = 'gray')

    for i in range(corr1.shape[1]):
        p1 = corr1[:, i]
        p2 = corr2[:, i]
        plt.scatter(p1[0], p1[1], s = 3, edgecolors = 'b')
        plt.scatter(p2[0] + image1.shape[1], p2[1], s = 3, edgecolors = 'b')
        plt.plot([p1[0], p2[0] + image1.shape[1]], [p1[1], p2[1]], linewidth = 0.35)
    fig.savefig('result.png')
#plt.show()

