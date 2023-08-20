from pypresence import Presence
import json, time


def updateRPC():
    with open("config.json") as config_file:
        config = config_file.read()
        config = json.loads(config)
    RPC = Presence(config.get("ClientID"))
    RPC.connect()
    print("[INFO] Discord Rich Presence активировано")
    print("[WARNING] Не закрывайте эту консоль, так как она завершит работу RPC.")
    RPC.update(state=config.get("State"), details=config.get("Details"),
               start=time.time(), large_image=config.get("LargeImage"),
                large_text=config.get("LargeImageText"), small_image=config.get("SmallImage"),
                small_text=config.get("SmallImageText"), buttons = [
                    {"label": config.get("Button1"), "url": config.get("Url1")},
                    {"label": config.get("Button2"), "url": config.get("Url2")}
                ]
    )


if __name__ == "__main__":
    updateRPC()
    while True:
        time.sleep(30)



