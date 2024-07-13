import tkinter as tk                                                               
from tkinter import messagebox

root = tk.Tk()
root.title("Tic-Tac-Toe")

buttons = [[None, None, None], [None, None, None], [None, None, None]]
current_player = "X"

def button_click(row, col):
    global current_player

    if buttons[row][col]["text"] == "" and current_player == "X":
        buttons[row][col]["text"] = "X"
        buttons[row][col]["fg"] = "blue"
        current_player = "O"
    elif buttons[row][col]["text"] == "" and current_player == "O":
        buttons[row][col]["text"] = "O"
        buttons[row][col]["fg"] = "red"
        current_player = "X"

    buttons[row][col]["state"] = "disabled"
    
    check_winner()
    
def check_winner():
    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[row][0]['text']} wins!")
            reset_board()
            return
        
    for col in range(3):
        if buttons[0][col]["text"] == buttons[1][col]["text"] == buttons[2][col]["text"] != "":
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[0][col]['text']} wins!")
            reset_board()
            return
        
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[0][0]['text']} wins!")
        reset_board()
        return
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[0][2]['text']} wins!")
        reset_board()
        return
    
    is_tie = all(buttons[i][j]["text"] != "" for i in range(3) for j in range(3))
    if is_tie:
        messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
        reset_board()

def reset_board():
    global current_player
    for i in range(3):
        for j in range(3):
            buttons[i][j]["text"] = ""
            buttons[i][j]["state"] = "active"
    current_player = "X"

for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text="", font=("Arial", 40), width=4, height=2,
                                  command=lambda row=i, col=j: button_click(row, col))
        buttons[i][j].grid(row=i, column=j)

root.mainloop()
