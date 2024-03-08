import pip

# Function to install packages using pip
def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])

# Install the required package 'fastf1'
install('fastf1')

import fastf1
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib import cm
import numpy as np

# Enable caching for FastF1 (replace the directory with your cache directory)
fastf1.Cache.enable_cache('C:\WPy64-39100\python-3.9.10.amd64\Lib\site-packages')

# Load a session and its telemetry data
# Assuming 'dataset' contains race year, race name, and session type information
session = fastf1.get_session(dataset['race_year'].values[0], dataset['name'].values[0], 'R')
session.load()

# Get telemetry data for the fastest lap
lap = session.laps.pick_fastest()
tel = lap.get_telemetry()

# Extract X and Y coordinates from telemetry data
x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

# Create points and segments for plotting
points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)

# Extract gear information
gear = tel['nGear'].to_numpy().astype(float)

# Define colormap for gear visualization
cmap = cm.get_cmap('Paired')

# Create LineCollection for gear visualization
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

# Plotting
plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

# Adding title
title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lap['Driver']} - {session.event['EventName']} {session.event.year}"
)

# Adding colorbar for gear visualization
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))

plt.show()