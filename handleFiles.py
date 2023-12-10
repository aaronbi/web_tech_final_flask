import os
import json

#returns a list of trip names of all saved trips in files
def getTripNames():
    trips = os.listdir('files')
    for i in range(len(trips)):
        trips[i] = trips[i].replace('_', ' ')[0:-5]
    return trips

#loads and returns json data for the given trip
def getTrip(name):
    trips = os.listdir('files')
    name = name.replace(' ', '_')

    for t in trips:
        if t.find(name) != -1:
            with open('files/'+t, 'r') as file:
                data = json.load(file)
            return data
    
    #trip not found? (shouldn't be possible)
    print('\nTRIP NOT FOUND\n', name)
    return None


if __name__ == '__main__':
    print(getTripNames())
