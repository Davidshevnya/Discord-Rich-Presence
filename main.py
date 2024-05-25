import json

from pypresence import Presence



def updateRPC():
    try:
        with open("config.json") as config_file:
            config = config_file.read()
            config = json.loads(config)
        RPC = Presence(config.get("ClientID"))
        config.pop("ClientID")
        RPC.connect()
        
        RPC.update(**config)
    except Exception as _ex:
        return print(f"[ERROR] {_ex}")
    
    print("[INFO] Discord Rich Presence активировано")
    print("[WARNING] Не закрывайте эту консоль, так как она завершит работу RPC.")

if __name__ == "__main__":
    updateRPC()
    input("Чтобы выйти, нажмите [ENTER]")



