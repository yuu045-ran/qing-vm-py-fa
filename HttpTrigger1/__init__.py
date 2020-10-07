import logging
import paramiko
from paramiko import AutoAddPolicy
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    ##added
    ##connecting to VM
    hostname = '10.3.1.4' # VIP = '10.3.1.4'
    port = 22
    username = 'yuran'
    password = 'Yuukochan!1979'

    
    s = paramiko.SSHClient()
    s.load_system_host_keys()
    s.set_missing_host_key_policy(AutoAddPolicy())
    s.connect(hostname, port, username, password)
    command = 'python3 hello.py'
    (stdin, stdout, stderr) = s.exec_command(command)
    print("below is the content of hello.py")
    for line in stdout.readlines():
        print(line)
    s.close()

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
