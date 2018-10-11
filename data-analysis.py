import pandas as pd
import matplotlib.pyplot as plt
import plotly.plotly as py

data = pd.read_csv("test.csv") 

# Speed controlled road
controled_access = data[data.controlledAccess != 'N']
py.iplot(controled_access, filename='controled_access')

# roads has no speed control
not_controled_access = data[data.controlledAccess != 'Y']
py.iplot(not_controled_access, filename='not_controled_access')

# Highway list
highway = data[data.isHighway != '0']
py.iplot(highway, filename='highway')

#Local roads
local_road = data[data.isHighway != '0']
py.iplot(local_road, filename='local_road')

#
max_speed = df[['latitude', 'longitude', 'speedlimit_mph', 'driver_id']]
vehicle_speed = df[['latitude', 'longitude', 'speed_mph', 'driver_id']]

vehicle_speed['speed'] = max_speed.speed[max_speed.speedlimit_mph < vehicle_speed.speed_mph]
vehicle_speed = vehicle_speed[vehicle_speed.speed != False]
# Best drivers data frame
vehicle_speed = vehicle_speed[vehicle_speed.speed_mph < 10]
py.iplot(vehicle_speed, filename='vehicle_speed')

