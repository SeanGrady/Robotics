from random import random
import operator as op
import matplotlib.pyplot as plt

class NoisyAccelerometer():

    def random_walk(self, nsteps):
        pos = (0,0)
        pos_list = []
        for i in range(nsteps):
            x = random()*2 - 1
            y = random()*2 - 1
            delta_pos = (x, y)
            pos = tuple(map(op.add, delta_pos, pos))
            pos_list.append(pos)
        return pos_list

class Plotter():

    def _format_points(self, point_list):
        x, y = zip(*point_list)
        x = list(x)
        y = list(y)
        return x, y

    def plot_lists(self, point_lists, color='blue'):
        for point_list in point_lists:
            x, y = self._format_points(point_list)
            plt.plot(x, y, color=color)

    def average_lists(self, point_lists):
        alist = []
        for i in range(len(point_lists[0])):
            x_tot = 0.0
            y_tot = 0.0
            for plist in point_lists:
                x_tot += plist[i][0]
                y_tot += plist[i][1]
            x_avg = x_tot/len(point_lists)
            y_avg = y_tot/len(point_lists)
            alist.append((x_avg, y_avg))
        return alist

if __name__ == '__main__':
    NA = NoisyAccelerometer()
    point_lists = []
    for _ in range(100):
        pos_list = NA.random_walk(1000)
        point_lists.append(pos_list)
    pltr = Plotter()
    pltr.plot_lists(point_lists, color='grey')
    avg_list = pltr.average_lists(point_lists)
    pltr.plot_lists([avg_list], color='red')
    print "Plotting..."
    plt.show()
