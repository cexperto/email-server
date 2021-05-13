# from flask import send_from_directory
# remender = "qwe@main wer@tyyt"
# affair = "un mensaje"
# message = "un bonito mensaje"
# number_copy = 3


def process(remender, affair, message, number_copy):
    try:
        copy = int(number_copy)
        my_email = [remender,affair,message]
        for i in range(1,copy+1):
            # print(i)
            with open(f"./files/{i}.txt", "w", encoding="utf-8") as f:
                for item in my_email:
                    f.write(f"{i} {item}")
                    f.write("\n")
    
    except:
        'execp'

