# intelligent_robot
This programm is about speech recoginzation of Japanese by accessing to IBM Watson API

Python version : python 2.7
in program  25 : RECORD_SECONDS = 5  ,which means it can record your speaking voice for 5seconds, you can replace it with any seconds 
                  u want. 
 line 57  : shutil.copy(r"D:\NLTK_py\record.wav", r"D:\NLTK_py\guest_record")
            D:\NLTK_py is where the program put,you should replace it with your own file path.
 line 91 : name = ["田中", "佐藤", "鈴木","查无此人"]  # 日文格式,  it includes several Japanese names which your speaking  is going 
            to  be compared with it.
 To run this program, make sure you are online.
