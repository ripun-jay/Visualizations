import csv
import matplotlib.pyplot as plt
from datetime import datetime

# filename= "files/weather_small_dataset.csv"
filename= "files/weather_large_dataset.csv"

with open(filename) as f:
    reader = csv.reader(f)
    title = next(reader)
    for index, head in enumerate(title):
       # print(index, head)
        pass

    """
    0 AKDT
    1 Max TemperatureF
    2 Mean TemperatureF
    3 Min TemperatureF
    """

    
    highs, lows, means, dates = [],[],[],[]
    for row in reader:
        highs.append(int(row[1]))
        lows.append(int(row[3]))
        means.append(int(row[2]))
        dates.append(datetime.strptime(row[0], '%Y-%m-%d'))

# print(f"{highs}\n\n{lows}\n\n{dates}")

fig, ax = plt.subplots(figsize=(12,8))
ax.plot(dates, highs, c="red", alpha= 0.5, linewidth= 0.9)
ax.plot(dates, lows, c= "blue", alpha= 0.5, linewidth= 0.9)
ax.plot(dates, means, c="orange", alpha= 0.8, linewidth= 0.4, label= "orange")

ax.set_xlabel("DATE", fontsize=14)
ax.set_ylabel("TEMPRATURE", fontsize=14)
ax.set_title("WEATHER RECORDS", fontsize=24)
ax.tick_params(axis= "both", which= "major", labelsize=5)
plt.fill_between(dates, highs, lows, facecolor= "green", alpha=0.26)

fig.autofmt_xdate()
plt.show()