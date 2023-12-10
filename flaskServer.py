from flask import *

app = Flask(__name__)

#server logic for home page
@app.route("/",methods = ['POST','GET'])
def home():
    return render_template('home.html')



#code for starting dev server
if __name__ == '__main__':
    app.secret_key = 'secret key abc'
    app.config['SESSION_TYPE'] = 'filesystem'

    app.run(host='0.0.0.0',debug=True)
