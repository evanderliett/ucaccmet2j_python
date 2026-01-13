import json
with open("precipitation.json") as file:
    contents = json.load(file)

# the station code for seattle is GHCND:US1WAKG0038

# to select all the seattle stations from the precipitation data:
seattle_stations = [
    x
    for x in contents
        if x["station"] == "GHCND:US1WAKG0038"
]

month = 0
total_monthly_precipitation_seattle = {}
for entry in seattle_stations:
    date = entry["date"].split("-") # the data looks like this '2010-12-28' and i want to take out the month
    month = int(date[1])
    if month not in total_monthly_precipitation_seattle:
        total_monthly_precipitation_seattle[month] = 0
    else:
        total_monthly_precipitation_seattle[month] = total_monthly_precipitation_seattle[month] + entry["value"]
print(total_monthly_precipitation_seattle)
# the results: [1690, 730, 870, 749, 911, 568, 54, 51, 902, 908, 1090, 2249]
# in methods: we analyzed the data per month in seattle

# to make it into a list format
print(list(total_monthly_precipitation_seattle.values()))

# to output as json file
import json
with open ("results.json", "w", encoding="utf-8") as file:
    json.dump(total_monthly_precipitation_seattle, file, indent=4, ensure_ascii=False)
# results: {
#     "1": 1690,
#     "2": 730,
#     "3": 870,
#     "4": 749,
#     "5": 911,
#     "6": 568,
#     "7": 54,
#     "8": 51,
#     "9": 902,
#     "10": 908,
#     "11": 1090,
#     "12": 2249
# }