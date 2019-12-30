import os
import yaml
import json

path = 'C:\\Users\\'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.yaml' in file:
            files.append(os.path.join(r, file))

for f in files:
    #print(f)
    json_f =f.replace(".yaml",".json")
    #print(json_f)
    with open(f, 'r') as yaml_in, open(json_f, "w") as json_out:
        yaml_object = yaml.safe_load(yaml_in) # yaml_object will be a list or a dict
        json.dump(yaml_object, json_out,default=str)
















#sf= 'C:\\Users\\bharathkumar.akki\\Desktop\\AB Personal\\Learning\\ipl_male\\1181768.yaml'
#tf= 'C:\\Users\\bharathkumar.akki\\Desktop\\AB Personal\\Learning\\ipl_male\\1181768.json'
'''with open('C:\\Users\\bharathkumar.akki\\Desktop\\AB Personal\\Learning\\ipl_male\\1181768.yaml') as f:
    #stream = file('C:\\Users\\bharathkumar.akki\\Desktop\\AB Personal\\Learning\\ipl_male\\1181768.yaml', 'r')
    yml_loaded = yaml.safe_load(f)

    with open('C:\\Users\\bharathkumar.akki\\Desktop\\AB Personal\\Learning\\ipl_male\\1181768.json','wb') as f:
        json.dump(yml_loaded, f)
'''
#with open(sf, 'r') as yaml_in, open(tf, "w") as json_out:
#    yaml_object = yaml.safe_load(yaml_in) # yaml_object will be a list or a dict
#    json.dump(yaml_object, json_out)