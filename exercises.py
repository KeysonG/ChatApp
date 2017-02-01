from bottle import route, run
import json
dict1= {
    "amount of times visited" : 0
}



@route('/')
def index():
    dict1["amount of times visited"] = dict1["amount of times visited"] +1
    return json.dumps(dict1)

def main():
    global counter
    run(host='localhost', port=7000)

if __name__ == '__main__':
 main()
