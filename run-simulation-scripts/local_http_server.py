from http.server import BaseHTTPRequestHandler, HTTPServer
import subprocess
import json


PORT_NUMBER = 8081

# This class will handles any incoming request from
# the browser 
class myHandler(BaseHTTPRequestHandler):
        def do_POST(self):
                content_len = int(self.headers.get('content-length'))
                post_body = self.rfile.read(content_len)
                self.send_response(200)
                self.end_headers()
                data = json.loads(post_body)

                with open('/home/ec2-user/data.json', 'a') as out:
                    json.dump(data, out)
                    out.write('\n')
                    
                # Use the post data
                #cmd = ["ls", "-rtl", "$HOME"]
                cmd = ["$HOME/aws-parallelcluster-monitoring/run-simulation-scripts/batch_run.sh", data['system']]
                p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
                p_status = p.wait()
                (output, err) = p.communicate()
                print("Command output : ", output)
                print("Command exit status/return code : ", p_status)

                self.wfile.write(output)
                return
try:
        # Create a web server and define the handler to manage the
        # incoming request
        server = HTTPServer(('', PORT_NUMBER), myHandler)
        print('Started httpserver on port ' , PORT_NUMBER)

        # Wait forever for incoming http requests
        server.serve_forever()

except KeyboardInterrupt:
        print('^C received, shutting down the web server')
        server.socket.close()
