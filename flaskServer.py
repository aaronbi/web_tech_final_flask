from flask import *
from handleFiles import *
import json

app = Flask(__name__)

#server logic for home page
@app.route("/",methods = ['POST','GET'])
def home():

    trip_names = getTripNames()
    #print(trip_names)
    
    if request.method == 'POST':
        print(request.form['trip_name'])
        return redirect(url_for('trip', trip_name=request.form['trip_name']))

    return render_template('home.html', trip_names=json.dumps(trip_names))


#server logic for trip info page
@app.route('/trip', methods = ['POST','GET'])
def trip():
    trip_name = request.args['trip_name']

    data = getTrip(trip_name)
    duration = data["duration"]
    location = data["location"]
    link = data["link"]
    climbers = json.dumps(data["climbers"])
    routes = json.dumps(data["routes"])
    images = json.dumps(data["images"])
    alts = json.dumps(data["image_alts"])
    return render_template('trip.html', trip_name=trip_name, duration=duration, location=location, link=link, climbers=climbers, routes=routes, images=images, alts=alts)


#about page
@app.route('/about', methods = ['POST', 'GET'])
def about():
    return render_template('about.html')

#code for starting dev server
if __name__ == '__main__':
    app.secret_key = 'secret key abc'
    app.config['SESSION_TYPE'] = 'filesystem'

    app.run(host='0.0.0.0',port=5000)
