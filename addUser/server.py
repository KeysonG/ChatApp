from bottle import route, run, template, static_file, request
import json

userlist = ["gideon"]

@route('/', method='GET')
def index():
    return template("index.html")


@route('/css/<filename:re:.*\.css>', method='GET')
def stylesheets(filename):
    return static_file(filename, root='css')

@route('/addUser', method='POST')
def adduser():
    global userlist
    username = request.POST.get('username')
    userlist.append(username)
    return json.dumps(userlist)

@route('/getUser', method='GET')
def getuser():
    global userlist
    return json.dumps(userlist)

def main():
    run(host='localhost', port=8000)

if __name__ == '__main__':
 main()
