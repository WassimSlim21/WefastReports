import pip

# Function to install packages using pip
def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])

# Install the required package 'fastf1'
install('fastf1')

import matplotlib.pyplot as plt
import pandas as pd
from timple.timedelta import strftimedelta  # Assuming there's a typo and the correct module is 'timple'
import fastf1
import fastf1.plotting
from fastf1.core import Laps

# Enable caching for FastF1 (replace the directory with your cache directory)
fastf1.Cache.enable_cache('C:\WPy64-39100\python-3.9.10.amd64\Lib\site-packages')

# Set up matplotlib for timedelta support and disable color scheme and miscellaneous modifications
fastf1.plotting.setup_mpl(mpl_timedelta_support=True, color_scheme=None, misc_mpl_mods=False)

# Load a session and its telemetry data
# Assuming 'dataset' contains race year, race name, and driver code information
session = fastf1.get_session(dataset['race_year'].values[0], dataset['name'].values[0], 'R')
session.load()

# Get unique drivers in the session
drivers = pd.unique(session.laps['Driver'])
print(drivers)

# Get the fastest lap for each driver
list_fastest_laps = list()
for drv in drivers:
    drvs_fastest_lap = session.laps.pick_driver(drv).pick_fastest()
    list_fastest_laps.append(drvs_fastest_lap)
fastest_laps = Laps(list_fastest_laps).sort_values(by='LapTime').reset_index(drop=True)

# Calculate the delta lap time compared to the pole lap
pole_lap = fastest_laps.pick_fastest()
fastest_laps['LapTimeDelta'] = fastest_laps['LapTime'] - pole_lap['LapTime']

print(fastest_laps[['Driver', 'LapTime', 'LapTimeDelta']])

# Get team colors for plotting
team_colors = list()
for index, lap in fastest_laps.iterlaps():
    color = fastf1.plotting.team_color(lap['Team'])
    team_colors.append(color)

# Plotting the delta lap times
fig, ax = plt.subplots()
ax.barh(fastest_laps.index, fastest_laps['LapTimeDelta'],
        color=team_colors, edgecolor='grey')
ax.set_yticks(fastest_laps.index)
ax.set_yticklabels(fastest_laps['Driver'])

# Show fastest lap at the top
ax.invert_yaxis()

# Draw vertical lines behind the bars
ax.set_axisbelow(True)
ax.xaxis.grid(True, which='major', linestyle='--', color='black', zorder=-1000)

# Convert pole lap time to string format
lap_time_string = strftimedelta(pole_lap['LapTime'], '%m:%s.%ms')

# Adding title
plt.suptitle(f"{session.event['EventName']} {session.event.year} Racing\n"
             f"Fastest Lap: {lap_time_string} ({pole_lap['Driver']})")

plt.show()