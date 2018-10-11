import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("test.csv") 

# Speed controlled road
controled_access = data[data.controlledAccess != 'N']

+

# roads has no speed control
not_controled_access = data[data.controlledAccess != 'Y']

# Highway list
highway = data[data.isHighway != '0']

#Local roads
local_road = data[data.isHighway != '0']


#
max_speed = df[['latitude', 'longitude', 'speedlimit_mph', 'driver_id']]
vehicle_speed = df[['latitude', 'longitude', 'speed_mph', 'driver_id']]

vehicle_speed['speed'] = max_speed.speed[max_speed.speedlimit_mph < vehicle_speed.speed_mph]
vehicle_speed = vehicle_speed[vehicle_speed.speed != False]
# Best drivers data frame
vehicle_speed = vehicle_speed[vehicle_speed.speed_mph < 10]

