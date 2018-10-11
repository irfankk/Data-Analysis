#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import plotly.plotly as py

data = pd.read_csv("test.csv") 

# Speed controlled road
# select controlled road and plot ot table
#remove controlledAccess colom value is 'N'
controled_access = data[data.controlledAccess != 'N']
py.iplot(controled_access, filename='controled_access')

# roads has no speed control
# remove controlled access and plot to table
not_controled_access = data[data.controlledAccess != 'Y']
py.iplot(not_controled_access, filename='not_controled_access')

# Highway list
#select higways
highway = data[data.isHighway != '0']
py.iplot(highway, filename='highway')

#Local roads
# Remove non highways 
local_road = data[data.isHighway != '0']
py.iplot(local_road, filename='local_road')

# Findin best drivers
# remove overspeed vehicles
#remove very slow vehicles

max_speed = df[['latitude', 'longitude', 'speedlimit_mph', 'driver_id', 'state']]
vehicle_speed = df[['latitude', 'longitude', 'speed_mph', 'driver_id', 'state']]
worst_speed = vehicle_speed
vehicle_speed['speed'] = max_speed.speed[max_speed.speedlimit_mph < vehicle_speed.speed_mph]
vehicle_speed = vehicle_speed[vehicle_speed.speed != False]

# Best drivers data frame
#plot to table
vehicle_speed = vehicle_speed[vehicle_speed.speed_mph < 10]
py.iplot(vehicle_speed, filename='vehicle_speed')

# plot based on area
latitude = vehicle_speed['latitude']
longitude = vehicle_speed['longitude']
plt.plot(latitude, longitude)
plt.show()

# worst drivers
# select over speed vehicles
# select very slow vehicles
worst_speed['speed'] = max_speed.speed[max_speed.speedlimit_mph > worst_speed.speed_mph]
worst_speed = worst_speed[worst_speed.speed != False]
worst_speed = worst_speed[worst_speed.speed_mph > 10]

# plot to table
py.iplot(worst_speed, filename='worst_speed')

# plot based on longitude and latitude
latitude = worst_speed['latitude']
longitude = worst_speed['longitude']
plt.plot(latitude, longitude)
plt.show()


# states based of worst drivers 
state = worst_speed['state']
diver = worst_speed['driver_id']
plt.plot(state, driver)
plt.show()

# state based on best drives
state = vehicle_speed['state']
diver = vehicle_speed['driver_id']
plt.plot(state, driver)
plt.show()


# worst drivers driving time
time = vehicle_speed['timestamp']
diver = vehicle_speed['driver_id']
plt.plot(time, driver)
plt.show()


# Best drivers driving time

time = vehicle_speed['timestamp']
diver = vehicle_speed['driver_id']
plt.plot(time, driver)
plt.show()

