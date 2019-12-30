import csv
import os
import json
import pandas as pd

#jf='C:\\Users\\bharathkumar.akki\\Desktop\\AB Personal\\Learning\\ipl_male\\1181768.json'

# folder for Converted json files
path = 'C:\\Users\\'

#output file name
op_file = 'C:\\Users\\All_balls.csv'

header = ['Match_id','Innings_no','Batting_team','Delivery_no','Batsman','Bowler','Non_striker','Batsman_runs','Extra_runs','Total_runs','Wides','Noballs','Legbyes','Byes','Penalty','Player_out','Kind','Fielders']
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

    Match_id=''.join([n for n in f if n.isdigit()])
    #print(Match_id)

    score_details =d["innings"]
    inn=0
    for a in score_details:

        for b in score_details[inn]:
            Batting_team = score_details[inn][b]["team"]
            inn_deliveries=score_details[inn][b]["deliveries"]
            seq = 0
            for i in inn_deliveries:
                #print(i)
                for j in inn_deliveries[seq]:
                    #print(inn_deliveries[0])
                    Innings_no =j
                    Delivery_no = str(inn_deliveries[seq].keys()).replace('dict_keys([\'','').replace('\'])','')
                    Batsman = inn_deliveries[seq][j]["batsman"]
                    Bowler = inn_deliveries[seq][j]["bowler"]
                    Non_striker = inn_deliveries[seq][j]["non_striker"]
                    Batsman_runs = inn_deliveries[seq][j]["runs"]["batsman"]
                    Extra_runs = inn_deliveries[seq][j]["runs"]["extras"]
                    Total_runs = inn_deliveries[seq][j]["runs"]["total"]
                    if "extras" in inn_deliveries[seq][j].keys():
                        if "wides" in inn_deliveries[seq][j]["extras"]:
                            Wides=inn_deliveries[seq][j]["extras"]["wides"]
                        else:
                            Wides = 0
                        if "noballs" in inn_deliveries[seq][j]["extras"]:
                            Noballs = inn_deliveries[seq][j]["extras"]["noballs"]
                        else:
                            Noballs = 0
                        if "legbyes" in inn_deliveries[seq][j]["extras"]:
                            Legbyes = inn_deliveries[seq][j]["extras"]["legbyes"]
                        else:
                            Legbyes = 0
                        if "byes" in inn_deliveries[seq][j]["extras"]:
                            Byes = inn_deliveries[seq][j]["extras"]["byes"]
                        else:
                            Byes = 0
                        if "penalty" in inn_deliveries[seq][j]["extras"]:
                            Penalty = inn_deliveries[seq][j]["extras"]["penalty"]
                        else:
                            Penalty = 0
                    else :
                        Wides = 0
                        Noballs = 0
                        Legbyes = 0
                        Byes = 0
                        Penalty = 0

                    if "wicket" in inn_deliveries[seq][j].keys():
                        Player_out = inn_deliveries[seq][j]["wicket"]["player_out"]
                        Kind = inn_deliveries[seq][j]["wicket"]["kind"]
                        if "fielders" in inn_deliveries[seq][j]["wicket"]:
                            Fielders = str(inn_deliveries[seq][j]["wicket"]["fielders"]).replace('[\'','').replace('\']','').replace('\'','')
                        else :
                            Fielders = 'NULL'
                    else :
                        Player_out = 'NULL'
                        Kind = 'NULL'
                        Fielders = 'NULL'

                    res = [Match_id,Innings_no,Batting_team,Delivery_no,Batsman, Bowler, Non_striker, Batsman_runs, Extra_runs, Total_runs, Wides, Noballs, Legbyes,Byes, Penalty, Player_out, Kind, Fielders]
                    op_list.append(res)

                    seq += 1
        inn+=1


with open(op_file, 'w', newline='') as f:
    csv_writer = csv.writer(f,quoting=csv.QUOTE_ALL)
    csv_writer.writerows(op_list)