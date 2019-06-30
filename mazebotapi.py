import urllib.request, json 

def read_mazebot_data():
    with urllib.request.urlopen("https://api.noopschallenge.com/mazebot/random?minSize=10&maxSize=10") as url:
        data = json.loads(url.read().decode())
        return data

initialdata = read_mazebot_data()

maze = initialdata['map']

