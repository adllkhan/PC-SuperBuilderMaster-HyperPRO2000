from flask import Flask, render_template, request, redirect
from src import database, RequestAPI

app = Flask(__name__)
datas = []
ids = []
names = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/builder/<string:name>/<string:id>")
def builder(name, id):
    if str(id).isdigit():
        names.append(name)
        ids.append(id)
        return render_template("builder.html")
    elif str(id) == "start":
        return render_template("builder.html")
    elif str(id) == "done":
        cpu, cooler, drive, videocard, motherboard, power, memory, case = 0
        for i in range(0, len(names)):
            if names[i] == "video-card":
                videocard = ids[i]
            elif names[i] == "cpu-cooler":
                cooler = ids[i]
            elif names[i] == "internal-hard-drive":
                drive = ids[i]
            elif names[i] == "power-supply":
                power = ids[i]
            elif names[i] == "cpu":
                cpu = ids[i]
            elif names[i] == "memory":
                memory = ids[i]
            elif names[i] == "case":
                case = ids[i]
            elif names[i] == "power-supply":
                power = ids[i]
        forprice = database.PCbuilds(database.generateID(), cpu, motherboard, cooler, memory, videocard, case, drive. power, "")
        build = RequestAPI.sumPrice(forprice)
        database.add(build)
        return

@app.route("/builder/partpicker/<string:name>", methods=["GET", "POST"])
def partPicker(name):
    if(request.method == "GET" or request.method == "POST"):
        for i in RequestAPI.getParts(str(name)):
            datas.append(str(i.brand).lower() + " " + str(i.model).lower())
        return render_template("PartPicker.html", name=name, datas=datas)

@app.route("/builder/partpicker/<string:name>/partinfo/<string:data>", methods=["GET", "POST"])
def partInfo(name, data):
    response = None
    id = datas.index(str(data))
    response = RequestAPI.getParts(name)[id]
    return render_template("PartInfo.html", response=response, name=name, id=id)

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port=8080)