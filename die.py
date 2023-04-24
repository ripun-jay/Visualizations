from plotly.graph_objs import Bar, Layout
from plotly import offline
from random import randint, choice

class Die:

    def __init__(self, numside= 6, no_of_roll= 1000):
        self.numside= numside
        self.no_of_roll= no_of_roll

    def result(self):
        x_values= list(range(1,self.numside+1))
        y_values = [randint(1, self.numside) for i in range(self.no_of_roll)]
        x_frequency = []
        for i in range(1, self.numside+1):
            x_frequency.append(y_values.count(i))
        return x_values, x_frequency
    
die = Die()
x_values, x_frequency = die.result()

"""# analysing Result
print(sum(x_frequency), x_values)"""

# ploting result
data = [Bar(x= x_values, y= x_frequency)]
my_layout = Layout(xaxis= {"title": "values"}, yaxis={"title": "frequency of values"}, title = f"D{die.numside}Result",)
offline.plot({"data": data, "layout": my_layout}, filename=f"D{die.numside}.html")
