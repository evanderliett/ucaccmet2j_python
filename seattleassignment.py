import json
with open("precipitation.json") as file:
    contents = json.load(file)
# print(type(data))

# the station code for seattle is GHCND:US1WAKG0038
# using this station code to select all the measurements belonging to it from the JSON data file

seattle_stations = [
    x
    for x in contents
        if x["station"] == "GHCND:US1WAKG0038"
]
print(seattle_stations)

# to get total monthly precipitation, need to "group" by month and then sum up everything
total_monthly_precipitation_seattle = 