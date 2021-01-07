import MinecraftStats, MinecraftFileHandler, json
from os import path, environ, getenv, system
import subprocess as cmd

RESOURCES_PATH = getenv('RESOURCES_PATH')
STATS_PATH = getenv('STATS_PATH')
WORLD_STATS = getenv('WORLD_STATS')
GIT_USERNAME = getenv('GIT_USERNAME')
GIT_PASSWORD = getenv('GIT_PASSWORD')

def push_to_git():
    cp = cmd.run(f"cd {RESOURCES_PATH} && git add {STATS_PATH} && git commit -m \"[stats-repo] Update\" && git push -u origin master -f", check=True, shell=True)
    
mF = MinecraftFileHandler.MinecraftFileHandler(WORLD_STATS)
stats =  mF.get_users_stats()


all_stats = list()
for stat in stats:
    data_to_export = MinecraftStats.MinecraftStats(stat['content'],stat['uuid']).export_data()
    all_stats.append(data_to_export)

json.dump(all_stats, open(RESOURCES_PATH + "/" + STATS_PATH,'w+'))
push_to_git()