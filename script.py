import geopandas
import pandas
import json
from pandas.io.json import json_normalize

gdf = geopandas.read_file("Statewide_Prec_2016_NoWater/Statewide_Prec_2016_NoWater.shp")
#print gdf.head()


with open('2016precinctdata.json') as json_data:
    d = json.load(json_data)

d = d['data']

precname = [] #8
response = [] #10
yes = [] #11
no = [] #11
first = False
for x in range(0, len(d)):
    if(d[x][10] == "Yes"):
        precname.append(d[x][8])
        yes.append(int(d[x][11]))
    elif(d[x][10] == "No"):
        no.append(int(d[x][11]))

resultsdf = pandas.DataFrame({"PRECNAME":precname, "yes":yes, "no":no})

merged = gdf.merge(resultsdf, on="PRECNAME")
print merged.head()
#print sum(no)
