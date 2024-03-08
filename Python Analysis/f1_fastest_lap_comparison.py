import matplotlib.pyplot as plt
import fastf1.plotting

# Enable caching for FastF1
fastf1.Cache.enable_cache('C:\WPy64-39100\python-3.9.10.amd64\Lib\site-packages')  # Cache directory

# Enable some matplotlib patches for plotting timedelta values and load FastF1's default color scheme
fastf1.plotting.setup_mpl()

# Load a session and its telemetry data
# Assuming 'dataset' contains race year, race name, and driver code information
session = fastf1.get_session(dataset['race_year'].values[0], dataset['name'].values[0], 'Q')
session.load()

# Pick the fastest laps for the selected drivers
ver_lap = session.laps.pick_driver(dataset['code'].values[0]).pick_fastest()
ham_lap = session.laps.pick_driver(dataset['code'].values[1]).pick_fastest()

# Get telemetry data for the fastest laps
ver_tel = ver_lap.get_car_data().add_distance()
ham_tel = ham_lap.get_car_data().add_distance()

# Get team colors for plotting
rbr_color = fastf1.plotting.team_color('RBR')
mer_color = fastf1.plotting.team_color('MER')

# Plotting the telemetry data for the fastest laps
fig, ax = plt.subplots()
ax.plot(ver_tel['Distance'], ver_tel['Speed'], color=rbr_color, label=dataset['code'].values[0])
ax.plot(ham_tel['Distance'], ham_tel['Speed'], color=mer_color, label=dataset['code'].values[1])

# Adding labels and legend
ax.set_xlabel('Distance in m')
ax.set_ylabel('Speed in km/h')
ax.legend()

# Adding title
plt.suptitle(f"Fastest Lap Comparison \n {session.event['EventName']} {session.event.year} Qualifying")

plt.show()