import MinecraftStats, MinecraftFileHandler, json
from os import path
import subprocess as cmd

GIT_PATH = ""
STATS_PATH = ""
LATEST_PATH = ""

def push_to_git():
    cp = cmd.run(f"cd {GIT_PATH} && git add stats-repo\\latest.json && git commit -m \"[stats-repo] Update\" && git push -u origin master -f", check=True, shell=True)
    
mF = MinecraftFileHandler.MinecraftFileHandler("stats")
stats =  mF.get_users_stats()


all_stats = list()
for stat in stats:
    data_to_export = MinecraftStats.MinecraftStats(stat['content'],stat['uuid']).export_data()
    all_stats.append(data_to_export)

json.dump(all_stats, open(LATEST_PATH,'w+'))
push_to_git()