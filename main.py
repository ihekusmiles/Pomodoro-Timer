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
LONG_BREAK_MIN = 15
reps = 0
timer = ''

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    start_button.config(state="normal")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    reps += 1
    reset_button.config(state="normal") # Enable reset button after starting timer

    if reps == 8:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=GREEN)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=PINK)

# Disables the 'start' button after starting the program

    start_button.config(state="disabled")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    canvas.itemconfig(timer_text, text=f"{count_min:02}:{count_sec:02}") # canvas.itemconfig --> to configure in canvas
    '''Code below is Angela's, but we can simply use f-string, with 0 denoting 
    the fillers and 2 denoting number of 0's '''
    # if count_sec < 10:
    #     count_sec = f"0{count_sec}"
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)

    else:
        start_timer()
        bring_to_front()
        window.bell()
        marks = ""
        work_sessions = reps // 2
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)


# ---------------------------- FOCUS_WINDOW_TO_FRONT ------------------------------- #


def bring_to_front():
    # Restore if window is minimized
    window.state("normal")
    # Bring to top level above all windows
    window.attributes("-topmost", True)
    # Allows other windows to top level again
    window.attributes("-topmost", False)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=1, row=1)


title_label = Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)

check_marks = Label(font=(FONT_NAME, 16, "bold"), fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

'''command allows the button to start timer when user clicks it'''
start_button = Button(text="Start", bg="White", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", bg="White", command=reset_timer)
reset_button.grid(column=2, row=2)
reset_button.config(state="disabled") # Disabled before running timer

'''Main loop is listening all the time for inputs/buttons/etc'''


window.mainloop()

