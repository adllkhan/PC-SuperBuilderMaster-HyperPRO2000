from pcpartpicker import API
from re import sub
from decimal import Decimal

api = API()
def sumPrice(build):
    cpu = api.retrieve("cpu").get("cpu")[build].price
    motherboard = api.retrieve("motherboard").get("motherboard")[build].price
    cooler = api.retrieve("cpu-cooler").get("cpu-cooler")[build].price
    memory = api.retrieve("memory").get("memory")[build].price
    videocard = api.retrieve("video-card").get("video-card")[build].price
    case = api.retrieve("case").get("case")[build].price
    drive = api.retrieve("internal-hard-drive").get("internal-hard-drive")[build].price
    power = api.retrieve("power-supply").get("power-supply")[build].price
    return Decimal(sub(r'[^\d.]', '', str(cpu + motherboard + cooler + memory + videocard + case + drive + power)))
print(float(sumPrice(0)))