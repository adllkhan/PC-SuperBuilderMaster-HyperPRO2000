from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.app_context().push()
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://postgres://:postgres@localhost:5432/pc"
db.init_app(app)

sample = ["cpu", "motherboard", "cooler", "memory", "videocard", "case", "drive", "power", "price"]

class PCbuilds(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    cpu = db.Column(db.Integer)
    motherboard = db.Column(db.Integer)
    cooler = db.Column(db.Integer)
    memory = db.Column(db.Integer)
    videocard = db.Column(db.Integer)
    case = db.Column(db.Integer)
    drive = db.Column(db.Integer)
    power = db.Column(db.Integer)
    price = db.Column(db.String)

    def __init__(self, id, cpu, motherboard, cooler, memory, videocard, case, drive, power, price):
        self.id = id
        self.cpu = cpu
        self.motherboard = motherboard
        self.cooler = cooler
        self.memory = memory
        self.videocard = videocard
        self.case = case
        self.drive = drive
        self.power = power
        self.price = price

with app.app_context():
    db.create_all()

def genID():
    i = 0
    with app.app_context():
        while db.session.query(db.exists().where(PCbuilds.id == i)).scalar():
            i+=1
        return i

def add(build):
    with app.app_context():
        db.session.add(build)
        db.session.commit()

def data_exists(build):
    with app.app_context():
        exists = db.session.query(db.exists().where(PCbuilds.id == build.id)).scalar()
        return(exists)

def getData(id):
    with app.app_context():
        build = db.get_or_404(PCbuilds, id)
        return build
def genID():
    i = 0
    with app.app_context():
        while db.session.query(db.exists().where(PCbuilds.id == i)).scalar():
            i+=1
        return i