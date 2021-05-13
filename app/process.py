import os
from flask import send_from_directory
from app.config import UPLOAD_DIRECTORY


if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)



def process(sender, other, message, copys):
    try:        
        content = [sender,copys,message]
        for i in other:
            with open(os.path.join(UPLOAD_DIRECTORY, i+".txt"), "w") as f:
                f.write(f'From: {content[0]} \n message: \n {message} \n copys: \n {copys}')
                # for item in content:
                #     f.write(f"{item}")
                #     f.write("\n")
    
    except:
        'a error has ocurred'

# sender = "qwe@main"
# other = ['qwemial', 'wert', 'sadf']
# message = "un bonito mensaje"
# copy = 3

# process(sender, other, message, copy)