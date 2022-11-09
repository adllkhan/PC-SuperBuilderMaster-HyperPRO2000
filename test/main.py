import RequestAPI
from src import database


def chooseAct():
    return int(input("(type 1): Start build CPU. \n"
          "(type 0): Exit. \n"))

def engine(act):
    while act != 0:
        act = chooseAct()
        if act == 1:
            input("Press any Button to choose cpu.")
            for i in range (0, len(RequestAPI.getCPUs())):
                print(i, ": ", RequestAPI.getCPUs()[i].brand, RequestAPI.getCPUs()[i].model)
            cpu = int(input())
            input("Press any Button to choose motherboard.")
            for i in range (0, len(RequestAPI.getMotherboards())):
                print(i, ": ", RequestAPI.getMotherboards()[i].brand, RequestAPI.getMotherboards()[i].model)
            motherboard = int(input())
            input("Press any Button to choose cooler.")
            for i in range (0, len(RequestAPI.getCoolers())):
                print(i, ": ", RequestAPI.getCoolers()[i].brand, RequestAPI.getCoolers()[i].model)
            cooler = int(input())
            input("Press any Button to choose memory.")
            for i in range (0, len(RequestAPI.getMemories())):
                print(i, ": ", RequestAPI.getMemories()[i].brand, RequestAPI.getMemories()[i].model)
            memory = int(input())
            input("Press any Button to choose videocard.")
            for i in range (0, len(RequestAPI.getVideocards())):
                print(i, ": ", RequestAPI.getVideocards()[i].brand, RequestAPI.getVideocards()[i].model)
            videocard = int(input())
            input("Press any Button to choose case.")
            for i in range (0, len(RequestAPI.getCases())):
                print(i, ": ", RequestAPI.getCases()[i].brand, RequestAPI.getCases()[i].model)
            case = int(input())
            input("Press any Button to choose hard-drive.")
            for i in range(0, len(RequestAPI.getDrives())):
                print(i, ": ", RequestAPI.getDrives()[i].brand, RequestAPI.getDrives()[i].model)
            drive = int(input())
            input("Press any Button to choose power-supplies.")
            for i in range(0, len(RequestAPI.getPowers())):
                print(i, ": ", RequestAPI.getPowers()[i].brand, RequestAPI.getPowers()[i].model)
            power = int(input())

            forPrice = database.PCbuilds(database.generateID(), cpu, motherboard, cooler, memory, videocard, case, drive, power, "")
            build = database.PCbuilds(database.generateID(), cpu, motherboard, cooler, memory, videocard, case, drive, power, RequestAPI.sumPrice(forPrice))
            bool = save(build)
            if bool:
                act = 0

def save(build):
    clause = int(input("save build or build again? (1/2):\n"))
    if clause == 1:
        database.add(build)
        print("build saved!")
        clause = input("Exit? (Y/n):\n")
        if clause.lower() != "y":
            engine(-1)
            return False
        else:
            print("Good Bye!")
            return True
    elif clause == 2:
        engine(-1)
        return False
    else:
        save(build)

engine(-1)