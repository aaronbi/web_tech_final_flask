import os

#returns a list of trip names of all saved trips in files
def getTripNames():
    trips = os.listdir('files')
    for i in range(len(trips)):
        trips[i] = trips[i].replace("_", " ")[0:-5]
    return trips

if __name__ == '__main__':
    print(getTripNames())
