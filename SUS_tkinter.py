##
import tkinter as tk
from tkinter import messagebox, ttk
from DataClass import DataClass

# Load SUS questions (replace with actual file or list)
with open('SUS_EN_DK.csv', 'r') as SUSfile:
    lines = SUSfile.readlines()
    SUS= [ln.split(";")[1][0:-1] for ln in lines]
SUS = SUS[1:]
#Initialize data storage
SUSresults = DataClass('MyResp.csv')
responses = []

# Create main application window
root = tk.Tk()
root.title("Likert Scale SUS Questionnaire")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky="nsew")


selected_value = tk.IntVar(value=0)
scale_steps = 7
question_index = tk.IntVar(value=0)

## Functions
def update_question():
    if question_index.get() < len(SUS):
        question_label.config(text=SUS[question_index.get()])
        selected_value.set(0)
    else:
        calculate_score()


def next_question():
    val = selected_value.get()
    if question_label.cget("text") == 'Press Go to start':
        question_index.set(0)
        nav_button.config(text="Next Question")
        update_question()
        toggle_scale_state()
    else:
        if val == 0:
            messagebox.showwarning("Warning", "Please select a response before proceeding.")
            return
        responses.append(val)
        SUSresults.dataupdate(f"{question_index.get()+1}:{val}", val)
        question_index.set(question_index.get() + 1)
        update_question()

def calculate_score():
    odd_q = sum(responses[i] - 1 for i in range(0, len(responses), 2))
    even_q = sum(scale_steps - responses[i] for i in range(1, len(responses), 2))
    score = (odd_q + even_q) / ((scale_steps - 1) * len(SUS)) * 100
    SUSresults.dataupdate(f"SUSscore = {score}")
    messagebox.showinfo("SUS Score", f"Your SUS score is: {score:.2f}")

    #prepare for new answers
    question_label.config(text="Press Go to start")
    nav_button.config(text="Go")
    selected_value.set(0)
    question_index.set(0)
    responses.clear()
    toggle_scale_state()

def toggle_scale_state():
    for child in scale_frame.winfo_children():
        if isinstance(child, ttk.Radiobutton):
            if child.state() == "active":
                child.config(state="disabled")
            else:
                child.config(state="active")

## UI Elements
question_label = tk.Label(mainframe, text="Press Go to start", wraplength=400, justify="center", font=("Arial", 14))
question_label.grid(column=1, row=1, sticky=(tk.NSEW))

# radio buttons
scale_frame = tk.Frame(mainframe)
scale_frame.grid(column=1, row=2, sticky=(tk.NSEW))

scale_LeftLabel = tk.Label(scale_frame, text="Disagree")
scale_LeftLabel.grid(column=1, row=1, sticky="nsew")
for i in range(1, scale_steps + 2):
    rb = tk.Radiobutton(scale_frame, text=str(i),
                        variable=selected_value, value=i)
    rb.grid(column=i+1, row=1, sticky="nsew")
scale_RightLabel = tk.Label(scale_frame, text="Agree")
scale_RightLabel.grid(column=scale_steps+2, row=1, sticky="nsew")


# navigation button
nav_button = tk.Button(mainframe, text="Go", command=next_question)
nav_button.grid(column=1, row=3, sticky="nsew")


##
# Start the GUI loop
root.mainloop()
