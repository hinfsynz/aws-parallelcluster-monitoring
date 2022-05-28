from flask import Flask, Blueprint, request, jsonify
from flask_cors import CORS
import random
import requests
import subprocess
import json

app = Flask(__name__)
CORS(app)
api = Blueprint('api', __name__)
random.seed(10)

def get_host_ip():
    cmd = "ip route show | grep 'default' | awk '{print $3}'"
    p = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True, universal_newlines=True)
    return p.stdout.strip()

@api.route('/submit', methods=['POST'])
def handle_submit():
    if request.method == "POST":
        #first_name = request.form['firstName']
        #last_name = request.form['lastName']
        #job = request.form['job']
        #print(f'first name : {first_name}')
        #print(f'last name : {last_name}')
        #print(f'job : {job}')
        system_index = request.form['systemIndex']
        print(f'system index: {system_index}')
        #host_ip = get_host_ip()
        #print(host_ip)
        f = open('/tmp/out.txt', 'w')
        #f.write('system index:{0}, host_ip:{1}'.format(system_index, host_ip))
        f.write('system index:{0}'.format(system_index))
        f.close()
        port = 8081
        r = requests.post('http://localhost:{0}'.format(port), json.dumps({'system': system_index}),
             headers = {'content-type':'application/json'})
        print(r.status_code, r.reason)

        # do your processing logic here.

        return jsonify({
            #"firstName": first_name,
            #"lastName": last_name,
            #"job": job,
            "systemIndex": system_index,
            "greeting": "a random integer number: {0}".format(random.randint(1,100))
        })


app.register_blueprint(api, url_prefix='/api')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5050)
