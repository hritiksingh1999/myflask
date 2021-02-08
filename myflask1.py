from flask import Flask,jsonify,request,redirect


app=Flask(__name__)

songs=[{'name':'e','writer':'s'},{'name': 'o',"writer":"e"},{'name':'r','writer':'q'}]
@app.route("/songs",methods=["GET","POST"])
def get_songs():
    if request.method=="GET":
        return (songs)
    else:
        song=request.get_json()
        songs.append(song)
        return {'index': len(songs)},200

@app.route("/songs/<int:index>",methods=["PUT","DELETE"])
def put_songs(index):
    if request.method=="PUT":
        song=request.get_json()
        songs[index]=song
        return (songs),200
    else:
        songs.pop(index)
        return "DELETED",200

app.run(ssl_context=('cert.pem', 'key.pem'))