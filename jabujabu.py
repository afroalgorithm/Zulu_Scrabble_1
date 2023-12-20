import tkinter as tk
import random
import time

def check_guess():
    global score
    guess = entry.get()
    if guess.lower() == word.lower():
        score += 1
        score_label.config(text=f"Score: {score}")
        shuffle_word()
        entry.delete(0, tk.END)
    else:
        info_label.config(text="Incorrect, try again!")

def shuffle_word():
    global word, jumbled_word, start_time
    if len(words) == 0:
        info_label.config(text="Game Over!")
        entry.config(state=tk.DISABLED)
        return
    word = random.choice(words)
    words.remove(word)
    letters = list(word)
    random.shuffle(letters)
    jumbled_word = "".join(letters)
    jumbled_label.config(text=jumbled_word)
    info_label.config(text="Unscramble...")
    start_time = time.time()

def update_timer():
    global start_time
    elapsed_time = int(60 - (time.time() - start_time))
    if elapsed_time >= 0:
        timer_label.config(text=f"Time left: {elapsed_time} s")
        timer_label.after(1000, update_timer)
    else:
        timer_label.config(text="Time's up!")
        entry.config(state=tk.DISABLED)

words = ["inyoka", "uphuthu", "cishe", "uhlelo", "ephuka", "thula",
         "khuluma", "ethuka", "ipapa", "ngemuva", "hlasela", "ithuba",
         "phuthuma", "esikoleni", "ebhasini", "ehhotela", "chitha", "ilala",
         "lala", "unyoko", "isicathulo", "umlenze", "ekushumayeleni", "ingoma",
         "umntwana", "iphaphu", "emaphashini", "gcwala", "qhuma", "lamba",
         "yidla", "gcoba", "ngoba", "futhi", "ukuze", "giya"]
score = 0
word = ""
jumbled_word = ""
start_time = 0

root = tk.Tk()
root.title("Mthuli Buthelezi")
root.configure(bg='sienna')

main_frame = tk.Frame(root, bg='sienna')
main_frame.pack(padx=20, pady=20)

jumbled_label = tk.Label(main_frame, text=jumbled_word, font=('Arial', 18), bg='sienna', fg='white')
jumbled_label.pack(pady=10)

entry = tk.Entry(main_frame, font=('Arial', 14))
entry.pack(pady=10)

check_button = tk.Button(main_frame, text="Hlola", command=check_guess, bg='white', fg='black')
check_button.pack(pady=5)

info_label = tk.Label(main_frame, text="Hlela amagama...", font=('Arial', 14), bg='sienna', fg='white')
info_label.pack(pady=10)

score_label = tk.Label(main_frame, text=f"Score: {score}", font=('Arial', 14), bg='sienna', fg='white')
score_label.pack(pady=5)

timer_label = tk.Label(main_frame, text="Isikhathi esisele: 60 s", font=('Arial', 14), bg='sienna', fg='white')
timer_label.pack(pady=5)

shuffle_word()
update_timer()

root.mainloop()
