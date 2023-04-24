from random import choice, randint
import matplotlib.pyplot as plt

class RandomWalk:

    def __init__(self, numwalk= 5000):
        self.x = [0]     # setting starting point at(0,0)
        self.y = [0]
        self.c = [0]     # setting color of starting point
        self.numwalk = numwalk

    def position(self):

        while len(self.x) < self.numwalk:
            x_direction= choice([-1,1])
            x_distance= choice([0,1,2,3,4])
            x_step = x_direction*x_distance

            y_direction= choice([-1,1])
            y_distance= choice([0,1,2,3,4])
            y_step = y_direction*y_distance

            # discart no movement
            if x_step== 0 and y_step== 0:
                continue
            
            c= choice([1,2,3,4,5,6])
            x = self.x[-1] + x_step
            y = self.y[-1] + y_step
            c = randint(1,6)

            self.x.append(x)
            self.y.append(y)
            self.c.append(c)

        return self.x, self.y, self.c

rw= RandomWalk(100)
x, y, c = rw.position()
print(x,y,c)   # analyzing result

# ploting the random walk in x,y cordinaate

fig, ax = plt.subplots(figsize= (15,9), dpi= 100)
#plt.style.use("seaborn")
ax.scatter(x,y, c=c)
ax.set_title("Random Walk", fontsize=24)
ax.set_xlabel("X", fontsize= 14)
ax.set_ylabel("Y", fontsize= 14)

ax.tick_params(axis= "both", labelsize= 10)




plt.show()
            
