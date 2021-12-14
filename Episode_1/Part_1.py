import matplotlib.pyplot as plt

color = ['b', 'g', 'r', 'c', 'm', 'y', 'r']
for i in range(1, 6):
    with open("Love/00%d.dat" % i) as f:
        n = int(f.readline())
        x = []
        y = []
        for j in range(n):
            row = f.readline().split()
            x.append(float(row[0]))
            y.append(float(row[1]))

        plt.scatter(x, y, label='00%d.dat' % i, color=color[i])
        plt.title("Data of Santa Claus", fontsize=17)

    plt.legend()
    plt.gca().set_aspect('equal', adjustable='box')
    plt.savefig('../00%d.png' % i)
    plt.show()



