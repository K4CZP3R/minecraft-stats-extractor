import requests, uuid, json


class MinecraftProfile:
    def __init__(self, player_uuid):
        try:
            uuid.UUID(player_uuid,version=4)
        except:
            raise ValueError("Invalid uuid!")

        self.p_uuid = player_uuid
    
    def get_profile(self):
        resp = json.loads(requests.get(f"https://api.minetools.eu/profile/{self.p_uuid}").text)
        if resp["raw"]["status"] == "ERR":
            raise ValueError(f"This profile does not exist! {resp['raw']['errorMessage']} ({self.p_uuid})")


        self.p_name = resp["decoded"]["profileName"]
        self.head_link = f"https://crafatar.com/renders/head/{self.p_uuid}"
        self.body_link = f"https://crafatar.com/renders/body/{self.p_uuid}"
    
    def get_name(self):
        return self.p_name
    def get_head_link(self):
        return self.head_link
    def get_body_link(self):
        return self.body_link
