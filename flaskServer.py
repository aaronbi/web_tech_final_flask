from flask import *
from handleFiles import *
import json

app = Flask(__name__)

#server logic for home page
@app.route("/",methods = ['POST','GET'])
def home():

    trip_names = getTripNames()
    print(trip_names)
    
    if request.method == 'POST':
        print(request.form['trip_name'])

    return render_template('home.html', trip_names=json.dumps(trip_names))



#code for starting dev server
if __name__ == '__main__':
    app.secret_key = 'secret key abc'
    app.config['SESSION_TYPE'] = 'filesystem'

    app.run(host='0.0.0.0',debug=True)
