import csv
import os
import json
import pandas as pd

# folder for Converted json files
path = 'C:\\Users\\'

#output file name
op_file = 'C:\\Users\\Matches_info.csv'

header = ['match_id','venue','city','dates','overs','team1','team2','toss_winner','toss_winner_descision','man_of_match','winner','win_margin','umpire1','umpire2']
op_list =[]
op_list.append(header)

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.json' in file:
            files.append(os.path.join(r, file))

for f in files:

    with open(f) as data_file:
        d= json.load(data_file)

    match_id=''.join([n for n in f if n.isdigit()])
    print(match_id)

    #print(d["info"])
    venue=str(d["info"]["venue"]).replace(',','-')
    if "city" in d["info"]:
        city=d["info"]["city"]
    else :
        str(d["info"]["venue"]).replace(',','-')
    dates=str(d["info"]["dates"]).replace('[','').replace(']','')
    overs=d["info"]["overs"]
    team1=d["info"]["teams"][0]
    team2=d["info"]["teams"][1]
    toss_winner = d["info"]["toss"]["winner"]
    toss_winner_descision = d["info"]["toss"]["decision"]
    if "player_of_match" in d["info"]:
        man_of_match = d["info"]["player_of_match"]
    else :
        man_of_match ='NULL'
    if "winner" in d["info"]["outcome"]:
        winner = d["info"]["outcome"]["winner"]
    else :
        winner =d["info"]["outcome"]["result"]
    if "winner" in d["info"]["outcome"]:
        if "runs" in d["info"]["outcome"]["by"]:
            win_margin = str(d["info"]["outcome"]["by"]["runs"]) + ' runs'
        if "wickets" in d["info"]["outcome"]["by"]:
            win_margin = str(d["info"]["outcome"]["by"]["wickets"]) + ' wickets'
    else :
        win_margin ='NULL'
    umpire1 = d["info"]["umpires"][0]
    umpire2 = d["info"]["umpires"][1]

    res = [match_id,venue,city,dates,overs,team1,team2,toss_winner,toss_winner_descision,man_of_match,winner,win_margin,umpire1,umpire2]
    op_list.append(res)

#print(len(op_list))

with open(op_file, 'w', newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerows(op_list)
