import json


#initializes and resets the test data
def initTrips():

    #some random climber data
    bob = {
            "name":"Bob",
            "level":"5.10c/V2",
            "skills":["lead climbing", "route cleaning", "top rope belayer", "lead belayer"],
            "gear": ["quickdraws", "slings", "60m rope", "ATC", "Grigri", "quad anchor", 'crash pads']
          }

    tom = {
            "name":"Tom",
            "level":"5.11b/V5",
            "skills":["lead climbing","trad climbing", "route cleaning", "top rope belayer", "lead belayer"],
            "gear": ["quickdraws","standard trad rack", "ascenders", "slings", "70m dry rope", "ATC", "Grigri"]
          }

    honnold = {
            "name":"Alex Honnold",
            "level":"5.14d/V12",
            "skills":["free soloing", "trad climbing", "lead climbing",'big walling' "route cleaning", "top rope belayer", "lead belayer"],
            "gear": ["chalk", "shoes", "snacks"]
          }
    
    tim = {
            "name":"Tim",
            "level":"5.0/VB",
            "skills":["has seen a rock before"],
            "gear": ["no"]
          }

    #some random routes from RRG
    eureka = {
            "name":"Eureka",
            "grade":"5.6",
            "type":"Sport, 70ft",
            "link":"https://www.mountainproject.com/route/105880926/eureka"
            }

    casual = {
            "name":"Casual Viewing",
            "grade":"5.7",
            "type":"Trad, 70ft",
            "link":"https://www.mountainproject.com/route/105878287/casual-viewing"
            }

    hazel = {
            "name":"Hazel Dormouse",
            "grade":"5.9+",
            "type":"Sport, 90ft",
            "link":"https://www.mountainproject.com/route/122728043/hazel-dormouse"
            }
    cave = {
            "name":"Caver's Route",
            "grade":"5.3 R",
            "type":"Trad, 200ft, 4 pitches",
            "link":"https://www.mountainproject.com/route/105882024/cavers-route"
            }
    
    #putting together the final .json object for this trip "The Red" 
    trip1 = {
            "trip_name":"The Red",
            "duration":"12/9/2023 - 12/16/2023",
            "location":"Red River Gorge",
            "link":"https://www.mountainproject.com/area/105841134/red-river-gorge",
            "climbers":[bob,tom,tim],
            "routes":[eureka, casual, hazel, cave],
            "images":["https://upload.wikimedia.org/wikipedia/commons/thumb/c/c0/View_of_Chimney_Top_Rock.JPG/1280px-View_of_Chimney_Top_Rock.JPG", "https://upload.wikimedia.org/wikipedia/commons/e/e6/Red_River_Gorge_-_Motherlode_-_Convicted_1.jpg"],
            "image_alts":["Chimney top rock", "Rock climbing in The Motherlode area of Red River Gorge"]
            }
    
    with open("files/The_Red.json","w") as out:
        json.dump(trip1, out)
    

    tommy = {
            "name":"Tommy Caldwell",
            'level':'5.15a/V13',
            'skills':["free soloing", "trad climbing", "lead climbing",'big walling' "route cleaning", "top rope belayer", "lead belayer"],
            'gear':["yes"]
            }

    #routes from yosemite
    nose = {
            'name':'The Nose',
            'grade':'5.9',
            'type':'Trad, Aid, 3000ft 31 pitches',
            'link':'https://www.mountainproject.com/route/105924807/the-nose'
            }

    #another trip .json
    trip2 = {
            'trip_name':'Speed Climbing The Nose',
            'duration':'2018/06/06',
            'location':'Yosemite NP',
            'link':'https://www.mountainproject.com/area/105833381/yosemite-national-park',
            'climbers':[honnold, tommy],
            'routes':[nose],
            'images':['https://mountainproject.com/assets/photos/climb/113207490_large_1498309301.jpg?cache=1702170121'],
            'image_alts':['Route Overlay for a 3-Day Ascent of the Nose']
            }
    with open('files/Speed_Climbing_The_Nose.json', 'w') as out:
        json.dump(trip2, out)

    #some data for trip 3
    ondra = {
            'name':'Adam Ondra',
            'level':'5.15d/V16',
            'skills':['extremely strong', 'world class sport climber', 'big walling', 'professional competition climber'],
            'gear':['a lot of shoes', 'all the essentials']
            }
    jakob = {
            'name':'Jakon Schubert',
            'level':'5.15d/V15',
            'skills':['extremely strong', 'olympic bronze medalist', 'professional competition climber'],
            'gear':['all the essentials']
            }
    silence = {
            'name':'Silence',
            'grade':'5.15d',
            'type': 'Sport, 150ft',
            'link':'https://www.mountainproject.com/route/120399023/silence'
            }
    trip3 = {
            'trip_name':'Flatanger',
            'duration':'12/11/23-12/14/23',
            'location':'Flatanger, Norway',
            'link':'https://www.mountainproject.com/area/110748026/flatanger',
            'climbers':[ondra, jakob],
            'routes':[silence],
            'images':['https://upload.wikimedia.org/wikipedia/commons/8/8e/Hanshelleren.JPG',
                'https://upload.wikimedia.org/wikipedia/commons/5/55/Adam_Ondra_climbing_Silence%2C_9c_by_PAVEL_BLAZEK_1.jpg', 'https://gripped.com/wp-content/uploads/2022/12/Jakob-Schubert-Project-Big.jpg'],
            'image_alts':['Hanshelleren cave in Flatanger','Adam Ondra on the second crux of Silence', 'Jakob Schubert resting with a double kneebar on B.I.G.']
            }
    with open('files/Flatanger.json','w') as out:
        json.dump(trip3, out)


    #random data for trip 4
    aaron = {
            'name':'Aaron Bi',
            'level':'5.10c/V3',
            'skills':['sport climbing', 'route cleaning', 'lead belaying'],
            'gear':['quickdraws', 'slings', 'ATC', '1 crash pad', 'quad anchor']
            }

    marie = {
            'name':'La Marie-Rose',
            'grade':'V3',
            'type':'Boulder',
            'link':'https://www.mountainproject.com/route/119450250/la-marie-rose'
            }
    toit = {
            'name':'Toit du Lepiney',
            'grade':'V4+',
            'type':'Boulder',
            'link':'https://www.mountainproject.com/route/113316863/toit-du-lepiney'
            }
    rainbow = {
            'name': 'Rainbow Rocket',
            'grade':'V11',
            'type':'Boulder',
            'link':'https://www.mountainproject.com/route/123838667/rainbow-rocket'
            }
    trip4 = {
            'trip_name':'Fontainebleau',
            'duration':'1/1/2024-1/30/24',
            'location':'Fontainebleau, France',
            'link':'https://www.mountainproject.com/area/106008886/fontainebleau',
            'climbers':[aaron, bob, ondra, honnold, tommy],
            'routes':[marie,toit,rainbow],
            'images':['https://goingupthecountry.net/wp-content/uploads/2023/08/IMG-20220917-WA0040-01.jpeg','https://bleau.info/images/bart.van.raaij/CarriersRainbowRocket.jpg'],
            'image_alts':['a bouldering area in fontainebleau', 'Rainbow Rocket V11']
            }
    with open('files/Fontainebleau.json','w') as out:
        json.dump(trip4, out)


#building and saving the .json files
if __name__ == '__main__':
    initTrips()




