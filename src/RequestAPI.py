from pcpartpicker import API
from re import sub
from decimal import Decimal

supported_parts = {'cpu', 'motherboard', 'cooler', 'memory', 'video-card', 'case', 'internal-hard-drive', 'power-supply'}

api = API()

def getCPUs():
    return api.retrieve("cpu").get("cpu")

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

def sumPrice(build):
    cpu = api.retrieve("cpu").get("cpu")[build.cpu].price
    motherboard = api.retrieve("motherboard").get("motherboard")[build.motherboard].price
    cooler = api.retrieve("cpu-cooler").get("cpu-cooler")[build.cooler].price
    memory = api.retrieve("memory").get("memory")[build.memory].price
    videocard = api.retrieve("video-card").get("video-card")[build.videocard].price
    case = api.retrieve("case").get("case")[build.case].price
    drive = api.retrieve("internal-hard-drive").get("internal-hard-drive")[build.drive].price
    power = api.retrieve("power-supply").get("power-supply")[build.power].price
    money = '$6,150,593.22'
    value = Decimal(sub(r'[^\d.]', '', money))
    return str(cpu + motherboard + cooler + memory + videocard + case + drive + power)