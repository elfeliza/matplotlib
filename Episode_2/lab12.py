import matplotlib.pyplot as plt
color = ['orchid', 'magenta', 'm', 'hotpink', 'mediumvioletred', 'purple']
with open('frames.dat') as f:
    lines = f.readlines()
    for j in range(0, 12, 2):
        l1 = lines[j]
        l2 = lines[j+1]
        x = [float(i) for i in l1.split()]
        y = [float(i) for i in l2.split()]
        img = plt.imread("gr2.jpg")
        fig, ax = plt.subplots()
        ax.imshow(img, extent=[0, 16, -10, 13])
        plt.plot(x, y, color=color[j // 2])
        plt.grid(which='major')
        fig.set_figwidth(12)
        if j == 10:
            plt.title("I've grown up! (%d)"%(j//2), fontsize=13)
        else:
            plt.title("My values are growing (%d)...."%(j//2), fontsize=13)
        plt.savefig('00%d.png' % j)
        plt.show()
        x, y = 0, 0
