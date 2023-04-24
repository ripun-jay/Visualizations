import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


filename = "files/earthquake_30days.json"

# loading JSON file
with open(filename, encoding= "utf8") as f:
    eq_data = json.load(f)

# eyeballing the file
readable_file = "files/earthquake_readable.json"
with open(readable_file, "w") as f:
    json.dump(eq_data, f, indent=4)

# structure of File
"""
{
"type": "xxx",
"metadata": "xxx"
"Feature": [
            {
               "type": "xxx",
               "properties": {
                                "mag": 232,
                                "title": "xx cc cc",
                                .
                                .
                                .many more
                             },
                "geomatry":  {
                                "type": "xx",
                                "coordinate" : [lat, lon, other]
                             },
                "ID": ususu
            },
            
            .
            .
            REPETING SAME FORMAT
            .
            .
            ],
"bbox": [
            5.2,
            3.4.
            .
            .
        ]

}

"""

# mags = eq_data[feature][property][mag]
# titles = eq_data[feature][property][title]
# lons = eq_data[feature][geomatry][cordinate][0]
# lats = eq_data[feature][geomatry][cordinate][1]


earthquakes = eq_data["features"]

mags, titles, lons, lats = [],[],[],[]
for earthquake in earthquakes:
    mags.append(earthquake["properties"]["mag"])
    titles.append(earthquake["properties"]["title"])
    lats.append(earthquake["geometry"]["coordinates"][1])
    lons.append(earthquake["geometry"]["coordinates"][0])

# viewing required data
# print(mags[:5] , titles[:5])

# ploting the earthquake on world map

data = [{
    "type": "scattergeo",
    "lon": lons,
    "lat": lats,
    "text": titles,
    "marker": {
              "size": [3*abs(mag) for mag in mags],
              "color": mags,
              "colorscale": "viridis",
              "reversescale": True,
              "colorbar": {"title": "Magnitude"}
    
              }
}]

mylayout= Layout(title= "Earthquake")

# open the plot offline in browzer
offline.plot({"data": data, "layout": mylayout}, filename="earthquakes.html")

