from tkinter import  *# ---------------------------- CONSTANTS ------------------------------- #
import math
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
my_timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(my_timer)
    label.config(text="TIMER",fg=GREEN,font=(FONT_NAME,45,"bold"),bg=YELLOW)
    canvas.itemconfig(timer_text,text="00:00")
    checkmark.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps +=1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60
    if reps % 8==0 :
        countdown(long_break_sec)
        label.config(text="Break",fg=RED,font=(FONT_NAME,45,"bold"),bg=YELLOW)
    elif reps % 2 ==0 :
        label.config(text="Break",fg=PINK,font=(FONT_NAME,45,"bold"),bg=YELLOW)

        countdown(short_break_sec)

    else:
        label.config(text="Work",fg=GREEN,font=(FONT_NAME,45,"bold"),bg=YELLOW)

        countdown(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

#timer works with milisecond 1000ms = 1s , fonksiyonadn sonraki parametreler fonksiyona atanıyor otomatikm
def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec <10:
        count_sec= f"0{count_sec}"


    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count >0:
        global my_timer
        my_timer=window.after(1000, countdown, count-1)

    else:
        start_timer()
        mark =""
        work_sessions = math.floor(reps/2)
        for a in range(work_sessions):
            mark +="✔"
        checkmark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title = ("Pomodoro")
window.config(padx=100, pady=50,bg=YELLOW,highlightthickness=0)

# canvas
canvas = Canvas(width=200,height=224,bg=YELLOW)
tomota_img = PhotoImage(file="tomato.png")
canvas.create_image(102, 112,image= tomota_img)
timer_text = canvas.create_text(103,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)


# label
label = Label(text="TIMER",fg=GREEN,font=(FONT_NAME,45,"bold"),bg=YELLOW)
label.grid(column=1,row=0)

# start button
start_button = Button(text="start",width=4,highlightthickness=0,command=start_timer)
start_button.grid(column=0,row=2)

#reset button
reset_button = Button(text="reset",width=4,highlightthickness=0,command=reset_timer)
reset_button.grid(column=2,row=2)

#checkmark
checkmark = Label(fg=GREEN,font=(FONT_NAME,20,"bold"),bg=YELLOW)
checkmark.grid(column=1,row=2)

# text="✔"

window.mainloop()