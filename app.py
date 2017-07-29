from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from bson import ObjectId
app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'tech4'
mongo = PyMongo(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        
        audits = mongo.db.audit.find()
        return render_template('index.html', audits=audits)
    elif request.method == 'POST':
        data = request.form
        audit_name = data['audit_name'] 
        audit_ref = data['ref_num'] 

        
        mongo.db.audit.insert({
           "Recordings": data["Recordings"],
            "Occurrence": data["Occurrence"],
            "Duration": data["Duration"],
            "Service": data["Service"],
            "daytime": data["daytime"],
            "Frequency": data["Frequency"],
            "Callsign": data["Callsign"],
            "RTF": data["RTF"],
            "Name": data["Name"],
            "Organization": data["Organization"],
            "Start": data["Start"],
            "CATEGORIES": data["CATEGORIES"],
            "Defects": data["Defects"],
            "Categories": data["Categories"],
            "Facility": data["Facility"],
            "Nameof": data["Nameof"],
            "Position": data["Position"],
            "Recordings": data["Recordings"],
            "Fault": data["Fault"],
            "START": data["START"],
            "Address": data["Address"],
            "Email": data["Email"],
            "Telephone": data["Telephone"],
        })
        return redirect(url_for('index'))








if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)
