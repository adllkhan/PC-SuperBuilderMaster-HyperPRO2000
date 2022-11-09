from flask import Flask, render_template, redirect, flash
from src import RequestAPI
from src import database as db

app = Flask(__name__)
ids = []
names = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/builder/<string:name>/<string:id>")
def builder(name, id):
    if str(id) == "start":
        return render_template("builder.html")
    elif str(id) == "done":
        cpu = 0
        cooler = 0
        drive = 0
        power = 0
        videocard = 0
        motherboard = 0
        memory = 0
        case = 0
        try:
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
                elif names[i] == "motherboard":
                    motherboard = ids[i]
            forprice = db.PCbuilds(int(db.genID()), int(cpu), int(motherboard), int(cooler), int(memory), int(videocard), int(case), int(drive), int(power), "")
            build = db.PCbuilds(int(db.genID()), int(cpu), int(motherboard), int(cooler), int(memory), int(videocard), int(case), int(drive), int(power), str(RequestAPI.sumPrice(forprice)))
            db.add(build)
        except:
            flash("Collect all parts!")
        return redirect("/builder/start/start")
    else:
        try:
            ids.remove(names.index(name))
            names.remove(names.index(name))
            names.append(name)
            ids.append(id)
        except:
            names.append(name)
            ids.append(id)
        flash('Chosen part added to the list, to change the part - just pick another and it would update automatically.')
        return redirect("/builder/start/start")

@app.route("/builder/partpicker/<string:name>")
def partPicker(name):
    datas = []
    list = RequestAPI.getParts(name)
    for i in list:
        if(int(i.price.amount) > 0.00):
            datas.append(str(i.brand).lower() + " " + str(i.model).lower())
    return render_template("PartPicker.html", name=name, datas=datas)

@app.route("/builder/partpicker/<string:name>/partinfo/<string:data>", methods=["GET", "POST"])
def partInfo(name, data):
    id = 0
    response = None
    list = RequestAPI.getParts(str(name))
    for i in range(0, len(list)):
        if (str(list[i].brand).lower() + " " + str(list[i].model).lower()) == str(data):
            id = i
            break
    response = list[id]
    print(name)
    name = str(name)
    print(name)
    print(id)
    return render_template("PartInfo.html", response=response, name=name, id=id)

@app.route("/mybuilds")
def myBuilds():
    ids = []
    for i in range(0, int(db.genID())):
        ids.append(int(db.getData(int(i)).id))
    return render_template("mybuilds.html", ids=ids)

@app.route("/mybuilds/<string:id>")
def build(id):
    id = int(id)
    ids = []
    data = []
    price = db.getData(id).price

    brand = RequestAPI.getParts(str(RequestAPI.supported_parts[0]))[int(db.getData(id).cpu)].brand
    model = RequestAPI.getParts(str(RequestAPI.supported_parts[0]))[int(db.getData(id).cpu)].model
    data.append(brand + " " + model)

    brand = RequestAPI.getParts(str(RequestAPI.supported_parts[1]))[int(db.getData(id).motherboard)].brand
    model = RequestAPI.getParts(str(RequestAPI.supported_parts[1]))[int(db.getData(id).motherboard)].model
    data.append(brand + " " + model)

    brand = RequestAPI.getParts(str(RequestAPI.supported_parts[2]))[int(db.getData(id).cooler)].brand
    model = RequestAPI.getParts(str(RequestAPI.supported_parts[2]))[int(db.getData(id).cooler)].model
    data.append(brand + " " + model)

    brand = RequestAPI.getParts(str(RequestAPI.supported_parts[3]))[int(db.getData(id).memory)].brand
    model = RequestAPI.getParts(str(RequestAPI.supported_parts[3]))[int(db.getData(id).memory)].model
    data.append(brand + " " + model)

    brand = RequestAPI.getParts(str(RequestAPI.supported_parts[4]))[int(db.getData(id).videocard)].brand
    model = RequestAPI.getParts(str(RequestAPI.supported_parts[4]))[int(db.getData(id).videocard)].model
    data.append(brand + " " + model)

    brand = RequestAPI.getParts(str(RequestAPI.supported_parts[5]))[int(db.getData(id).case)].brand
    model = RequestAPI.getParts(str(RequestAPI.supported_parts[5]))[int(db.getData(id).case)].model
    data.append(brand + " " + model)

    brand = RequestAPI.getParts(str(RequestAPI.supported_parts[6]))[int(db.getData(id).drive)].brand
    model = RequestAPI.getParts(str(RequestAPI.supported_parts[6]))[int(db.getData(id).drive)].model
    data.append(brand + " " + model)

    brand = RequestAPI.getParts(str(RequestAPI.supported_parts[7]))[int(db.getData(id).power)].brand
    model = RequestAPI.getParts(str(RequestAPI.supported_parts[7]))[int(db.getData(id).power)].model
    data.append(brand + " " + model)




    return render_template("build.html", id = id,  data = data, price = price)

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.run(debug = True, host = '0.0.0.0', port=8080)