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
# the results are a dictionary: {1: 1690, 2: 730, 3: 870, 4: 749, 5: 911, 6: 568, 7: 54, 8: 51, 9: 902, 10: 908, 11: 1090, 12: 2249}
# in methods: we analyzed the data per month in seattle

# to make it into a list format
print(list(total_monthly_precipitation_seattle.values()))
# the results are now a list: [1690, 730, 870, 749, 911, 568, 54, 51, 902, 908, 1090, 2249]

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

# to calculate the total precipitation over seattle, add all precipitation values together
total_yearly_precipitation_seattle = sum(list(total_monthly_precipitation_seattle.values()))
print(total_yearly_precipitation_seattle)
# result is 10772 

with open ("results.json", "a", encoding="utf-8") as file:
    json.dump(total_yearly_precipitation_seattle, file, indent=4, ensure_ascii=False)

# to calculate relative_monthly_precipitation (proportion of the yearly rain) per month. value has to be 0.2 not 20%
# its important that total_monthly_precipitation_seattle is in a dictionary format, not list
relative_monthly_precipitation_seattle = {}
for month in total_monthly_precipitation_seattle:
    relative_monthly_precipitation_seattle[month] = (total_monthly_precipitation_seattle[month] / total_yearly_precipitation_seattle)
print(relative_monthly_precipitation_seattle)
# results are: {1: 0.15688822874118083, 2: 0.06776828815447457, 3: 0.08076494615670256, 4: 0.0695321203119198, 5: 0.08457111028592648, 6: 0.05272929818046788, 7: 0.005012996658002228, 8: 0.004734496843668771, 9: 0.0837356108429261, 10: 0.08429261047159302, 11: 0.10118826587448941, 12: 0.20878202747864835}

with open ("results.json", "a", encoding="utf-8") as file:
    json.dump(relative_monthly_precipitation_seattle, file, indent=4, ensure_ascii=False)
# note: change it to "a" so that it adds and doesnt override the previous json.dump command

# having python read the station codes for each 

other_stations = [
    x
    for x in contents
        if x["station"] == "GHCND:USW00093814" or "GHCND:USC00513317" or "GHCND:US1CASD0032"
]
# print(other_stations) this works!

month = 0
total_monthly_precipitation_other = {}
for entry in other_stations:
    date = entry["date"].split("-") # the data looks like this '2010-12-28' and i want to take out the month
    month = int(date[1])
    if month not in total_monthly_precipitation_other:
        total_monthly_precipitation_other[month] = 0
    else:
        total_monthly_precipitation_other[month] = total_monthly_precipitation_other[month] + entry["value"]
print(total_monthly_precipitation_other)
# {1: 3890, 2: 2372, 3: 2764, 4: 2277, 5: 2338, 6: 2512, 7: 978, 8: 653, 9: 1425, 10: 2334, 11: 4194, 12: 5527}

total_yearly_precipitation_other = sum(list(total_monthly_precipitation_other.values()))
print(total_yearly_precipitation_other)
# you get 31264

relative_monthly_precipitation_other = {}
for month in total_monthly_precipitation_other:
    relative_monthly_precipitation_other[month] = (total_monthly_precipitation_other[month] / total_yearly_precipitation_other)
print(relative_monthly_precipitation_other)
# you get {1: 0.12442425793244627, 2: 0.07587001023541454, 3: 0.08840839303991811, 4: 0.0728313715455476, 5: 0.07478249744114637, 6: 0.08034800409416581, 7: 0.03128198567041965, 8: 0.020886642784032752, 9: 0.04557958034800409, 10: 0.07465455475946776, 11: 0.13414790174002048, 12: 0.17678480040941658}

relative = total_yearly_precipitation_seattle / (total_yearly_precipitation_seattle + total_yearly_precipitation_other)
print(relative)
# you get 0.2562565420116091. so only 25.6% of all yearly rain falls in seattle






stations_csv = []
with open("stations.csv", encoding = "utf-8") as file:
    for line in file:
        stations_csv.append(line.strip())
    stations_csv.remove("Location,State,Station")
print(stations_csv)

for location_info in stations_csv:
    location, state, code = location_info.split(",")