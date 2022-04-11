from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
SPEED = 10
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def rese_timer():
    global reps
    window. after_cancel(timer)
    label.config(text="Timer", font=(FONT_NAME, 35, "normal"), fg=GREEN, bg=YELLOW)
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0
    check.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps +=1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        label.config(text="Long_Break", highlightcolor=GREEN, fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        label.config(text="Short_Break", highlightcolor=GREEN, fg=PINK)
        count_down(short_break_sec)
    else:
        label.config(text="Work_Timer", highlightcolor=GREEN, fg=GREEN)
        count_down(work_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec< 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min} : {count_sec}")
    if count> 0:
        global timer
        timer= window.after(SPEED, count_down, count - 1)
    else:
        start_timer()
        check_marks = "✔"
        work_session = math.floor(reps / 2)
        check.config(text=check_marks*work_session)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("pomodoro")
window.config(padx=50, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

tomato_image = PhotoImage(file= "tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

label = Label(text="Timer", font=(FONT_NAME, 35, "normal"), fg=GREEN, bg=YELLOW)
label.config(highlightcolor=GREEN)
label.grid(column=2, row=1)


button = Button(text="Start", font=(FONT_NAME, 20, "normal"), highlightthickness=0, command=start_timer)
button.grid(column=1, row=4)

button1 = Button(text="Reset", font=(FONT_NAME, 20, "normal"), highlightthickness=0, command=rese_timer)
button1.grid(column=3, row=4)
check_mark = "✔"
check = Label()
check.grid(column=2, row=5)
check.config(fg=GREEN, bg=YELLOW)

window.mainloop()
