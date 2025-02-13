import matplotlib.pyplot as plt
import numpy as np 
from random import choice

plt.scatter(2, 4, s=200)

plt.title("Sqrt number", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Sqrt of value", fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=14)
#######################
plt.show()

x_values = [1,2,3,4,5]
y_values = [1,4,9,16,25]

plt.scatter(x_values, y_values, s=100)
plt.show()
#######################

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values,c= y_values, cmap=plt.cm.Blues, edgecolors='none', s=40)
plt.axis([0, 1100, 0, 1100000])
plt.savefig('graph.png', bbox_inches='tight')
plt.show()
#############################

class RandomWalk():

    def __init__(self, num_points=5000):
        self.num_points = num_points

        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        while len(self.x_values)  < self.num_points:
            x_direction = choice([1, -1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0,1,2,3,4])
            y_step = y_direction * y_distance

            if x_step == 0 and y_step == 0:
                continue

            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

rw = RandomWalk()
rw.fill_walk()
plt.scatter(rw.x_values, rw.y_values, s=15)
plt.show()

####################################

while True:
    rw = RandomWalk()
    rw.fill_walk()

    pts_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=pts_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)
    plt.show()

    keep_running = input("Make another? (y/n)")
    if keep_running == "n":
        break