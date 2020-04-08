import MinecraftProfile, datetime

class MinecraftStats:
    def __init__(self, stats_content, stats_uuid):
        self.stats_content = stats_content
        self.stats_uuid = stats_uuid
    
    def export_data(self):
        out_json = {}

        profile = MinecraftProfile.MinecraftProfile(self.stats_uuid)
        profile.get_profile()

        out_json["profile"] = {}
        out_json["profile"]["name"] = profile.get_name()
        out_json["profile"]["head_link"] = profile.get_head_link()
        out_json["profile"]["body_link"] = profile.get_body_link()
        out_json["profile"]["uuid"] = self.stats_uuid

        stats = self.stats_content['stats']

        out_json["stats"] = {}
        out_json["stats"]["play_one_minute"] = stats["minecraft:custom"]["minecraft:play_one_minute"] if "minecraft:play_one_minute" in stats["minecraft:custom"] else "0"
        out_json["stats"]["deaths"] = stats["minecraft:custom"]["minecraft:deaths"] if "minecraft:deaths" in stats["minecraft:custom"] else "0"
        out_json["stats"]["jumps"] = stats["minecraft:custom"]["minecraft:jump"] if "minecraft:jump" in stats["minecraft:custom"] else "0"
        out_json["stats"]["mined"] = stats["minecraft:mined"] if "minecraft:mined" in stats else {}


        played_ticks = out_json["stats"]["play_one_minute"]
        played_seconds = played_ticks / 20
        out_json["stats"]["play_time_readable"] = str(datetime.timedelta(seconds=played_seconds)).split(".")[0]
    
        return out_json
        