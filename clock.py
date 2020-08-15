from tkinter import *
import time


window = Tk()
window.geometry('300x128')
window.title('Digital Clock')
window.resizable(0, 0)
window.config(bg='red')


Empty_label = Label(window, font=('Times', 25, 'bold'))
Empty_label.pack( pady=10)

myDate = time.strftime("%d : %m : %Y")
Label(window, text=myDate, font=('Times', 15, 'bold')).pack(pady=5)

def clock():
    current_time = time.strftime("%I : %M : %S")
    Empty_label.config(text=current_time)
    Empty_label.after(200, clock)
clock()

## getTime = Button(window, text='Get Time').pack(side='left')
exitButton = Button(window, text='Exit', fg='white', font=('Times', 12), bg='red',command=quit)
exitButton.pack(side='right', ipadx=15)

def quit(window):
    window.destroy()

window.mainloop()

