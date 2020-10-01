# States needed
states_needed = {'mt', 'wa', 'or', 'id', 'nv', 'ut'}
# 
stations = {}
stations['kone'] = set(['id', 'nv', 'ut'])
stations['ktwo'] = set(['wa', 'id', 'mt'])
stations['ktree'] = set(['or', 'nv', 'ca'])
stations['kfour'] = set(['nv', 'ut'])
stations['kfive'] = set(['ca', 'az'])

# Solution
final_stations = set()

while states_needed:
    # Check the stations tha covers most uncovered satates
    best_station = None
    states_covered = set()
    for station, states in stations.items():
        # Check the states that the station covers and we need
        covered = states_needed & states
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
    # Append the best solution to final_stations and remove the now covered states
    states_needed -= states_covered
    final_stations.add(best_station)
print(final_stations)

