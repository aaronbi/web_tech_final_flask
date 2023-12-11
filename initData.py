import json


#resets the test data in files
def initTrips():

    #some random climber data
    bob = {
            "name":"Bob",
            "level":"5.10c/V2",
            "skills":["lead climbing", "route cleaning", "top rope belayer", "lead belayer"],
            "gear": ["quickdraws", "slings", "60m rope", "ATC", "Grigri", "quad anchor"]
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
            "skills":["free soloing", "trad climbing", "lead climbing", "route cleaning", "top rope belayer", "lead belayer"],
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
    


    

if __name__ == '__main__':
    initTrips()




