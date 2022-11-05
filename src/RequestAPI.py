from pcpartpicker import API
from re import sub
from decimal import Decimal
from src import database

supported_parts = {'cpu', 'motherboard', 'cooler', 'memory', 'video-card', 'case', 'internal-hard-drive',
                   'power-supply'}

api = API()


def getParts(name):
    try:
        return api.retrieve(str(name)).get(str(name))
    except:
        getParts(name)


"""
def getMotherboards():
    return api.retrieve("motherboard").get("motherboard")

def getCoolers():
    return api.retrieve("cpu-cooler").get("cpu-cooler")

def getMemories():
    return api.retrieve("memory").get("memory")

def getVideocards():
    return api.retrieve("video-card").get("video-card")

def getCases():
    return api.retrieve("case").get("case")

def getDrives():
    return api.retrieve("internal-hard-drive").get("internal-hard-drive")

def getPowers():
    return api.retrieve("power-supply").get("power-supply")

"""


def sumPrice(build):
    cpu = api.retrieve("cpu").get("cpu")[build.cpu].price
    motherboard = api.retrieve("motherboard").get("motherboard")[build.motherboard].price
    cooler = api.retrieve("cpu-cooler").get("cpu-cooler")[build.cooler].price
    memory = api.retrieve("memory").get("memory")[build.memory].price
    videocard = api.retrieve("video-card").get("video-card")[build.videocard].price
    case = api.retrieve("case").get("case")[build.case].price
    drive = api.retrieve("internal-hard-drive").get("internal-hard-drive")[build.drive].price
    power = api.retrieve("power-supply").get("power-supply")[build.power].price
    return str(cpu + motherboard + cooler + memory + videocard + case + drive + power)



print(api.retrieve("cpu").get("cpu")[0].price)
print(api.retrieve("motherboard").get("motherboard")[0].price)
print(api.retrieve("cpu-cooler").get("cpu-cooler")[0].price)
print(api.retrieve("memory").get("memory")[0].price)
print(api.retrieve("video-card").get("video-card")[0].price)
print(api.retrieve("case").get("case")[0].price)
print(api.retrieve("internal-hard-drive").get("internal-hard-drive")[0].price)
print(api.retrieve("power-supply").get("power-supply")[0].price)

