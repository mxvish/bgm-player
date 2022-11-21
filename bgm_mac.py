from tkinter import *
import threading, tkinter
import subprocess as sp

def play_bgm(file_name):
    #sp.call('mpg123 --loop -1 ' + file_name,shell=True)
    sp.call('mpg321 -l 0 ' + file_name,shell=True)

def next_bgm(file_name):
    stop_bgm()
    sp.call('osascript -e "set volume without output muted"',shell=True)
    play_bgm(file_name)

def stop_bgm():
    sp.call('killall mpg321',shell=True)

def first_button_clicked():
    first_BGM.start()

def stop_button_clicked():
    sp.call('osascript -e "set volume with output muted"',shell=True)

def second_button_clicked():
    second_BGM.start()

def third_button_clicked():
    third_BGM.start()

def finish_button_clicked():
    stop_BGM.start()

root = Tk()
root.title("Python Music Player")
root.geometry("500x400")

compliment = Label(root, text="")
compliment.grid(row=0, column=0)

first_button = tkinter.Button(root, text="1st BGM", command=first_button_clicked)
first_button.place(x=150,y=50)
stop_button = tkinter.Button(root, text="Stop BGM", command=stop_button_clicked)
stop_button.place(x=150,y=100)
second_button = tkinter.Button(root, text="2nd BGM", command=second_button_clicked)
second_button.place(x=150,y=150)
stop_button = tkinter.Button(root, text="Stop BGM", command=stop_button_clicked)
stop_button.place(x=150,y=200)
third_button = tkinter.Button(root, text="3rd BGM", command=third_button_clicked)
third_button.place(x=150,y=250)
finish_button = tkinter.Button(root, text="Finish BGM", command=finish_button_clicked)
finish_button.place(x=150,y=300)

first_BGM = threading.Thread(target=play_bgm, args=('BGM_1_金庫解錠まで.mp3',))
second_BGM = threading.Thread(target=next_bgm, args=('BGM_2_爆弾解除.mp3',))
third_BGM = threading.Thread(target=next_bgm, args=('BGM_3_ゲームクリア.mp3',))
stop_BGM = threading.Thread(target=stop_bgm)

root.mainloop()
#requirements
#
##mpg123
##python
##tkinter
