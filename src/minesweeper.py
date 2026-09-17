#
#  SEMESTER:        EECS 581 Fall 2026
#  PROJECT:         Project 1 - Minesweeper
#  FILE:            minesweeper.py
#
#  DESCRIPTION:     Implements the Minesweeper game, including board setup, gameplay logic, mine 
#                   flagging, win/loss conditions, and the Tkinter graphical user interface.
#
#  INPUT:           Player mouse input for uncovering and flagging cells.
#  OUTPUT:          Displays the Minesweeper board, cell states, and game results through the 
#                   graphical user interface.
#
#  COLLABORATORS:   Liam Kinghouser, Gael Salazar-Morales, Joshua Fakunmoju
#  SOURCES:         TBD
#
#  AUTHOR:          Pruthviraj Sadhankar
#  CREATION DATE:   09/13/2026
#
#  AUTHOR'S NOTE:   This file contains the initial minimum viable product (MVP) for the Minesweeper 
#                   game and may be modified or refactored as development continues.
#

import tkinter as tk, random
from tkinter import simpledialog

root = tk.Tk()
root.title("Minesweeper")

N = 10
M = 15

a = [[0] * N for _ in range(N)]
r = [[False] * N for _ in range(N)]
f = [[False] * N for _ in range(N)]
done = False
first_move = True


def place_mines(exclude_x, exclude_y):
    global a
    safe = {(exclude_x, exclude_y)}
    for i in range(max(0, exclude_x - 1), min(N, exclude_x + 2)):
        for j in range(max(0, exclude_y - 1), min(N, exclude_y + 2)):
            safe.add((i, j))
    for i in range(N):
        for j in range(N):
            a[i][j] = 0
    for mine in random.sample([(i, j) for i in range(N) for j in range(N) if (i, j) not in safe], M):
        a[mine[0]][mine[1]] = -1
    for i in range(N):
        for j in range(N):
            if a[i][j] != -1:
                a[i][j] = sum(a[x][y] == -1 for x in range(max(0, i - 1), min(N, i + 2)) for y in range(max(0, j - 1), min(N, j + 2)))


def reveal(x, y):
    global done, first_move
    if not (0 <= x < N and 0 <= y < N and not r[x][y] and not f[x][y]):
        return
    if first_move:
        place_mines(x, y)
        first_move = False
    r[x][y] = True
    if a[x][y] == -1:
        for p in range(N):
            for q in range(N):
                if a[p][q] == -1:
                    btns[p][q].config(text="💥", bg="red")
        done = True
        if tk.messagebox.askyesno("Minesweeper", "Boom! You lost. Play again?"):
            reset()
        else:
            root.destroy()
        return
    btns[x][y].config(relief=tk.SUNKEN, text=str(a[x][y] or ""), bg="lightgray", fg=["blue", "green", "red", "navy", "brown", "teal", "black", "gray"][a[x][y]])
    if a[x][y] == 0:
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                reveal(x + i, y + j)
    if sum(sum(r, [])) == N * N - M:
        done = True
        tk.messagebox.showinfo("Minesweeper", "You win!")
        root.destroy()


def click(x, y):
    if not done:
        reveal(x, y)


def flag(x, y, e):
    if done or r[x][y]:
        return

    # If the cell is unflagged and user has no flags left
    if (not f[x][y]) and calculate_remaining_flags() == 0:
        return
    
    f[x][y] = not f[x][y]
    btns[x][y].config(text="🚩" if f[x][y] else "")
    update_remaining_flags_label() # update the flag count label after a flag toggle
    return "break"


def reset():
    global done, first_move, M
    while True:
        mine_count = simpledialog.askinteger("Minesweeper", "Number of mines (10-20):", initialvalue=M, minvalue=10, maxvalue=20)
        if mine_count is None:
            mine_count = M
        if 10 <= mine_count <= 20:
            break
    M = mine_count
    for i in range(N):
        for j in range(N):
            r[i][j] = f[i][j] = False
            a[i][j] = 0
            btns[i][j].config(text="", bg="SystemButtonFace", relief=tk.RAISED)
    done = False
    first_move = True

    update_remaining_flags_label()

# Calculate the number of remaining flags the player has
# (Total mines (M) - placed flags)
def calculate_remaining_flags():
    global M # Declare global M variable so we can access in this function

    if done: # If game is over
        return 0 # User cannot flag more cells

    flagged_mines = 0 # Tracked flagged mines

    for i in range(N): # Iterate through columns
        for j in range(N): # Iterate through rows
            if f[i][j]: # Check if mine at [i][j] in matrix is flagged
                flagged_mines += 1 # If flagged, increment flagged mines tracker

    remaining_flags = M - flagged_mines # Calculate remaining flags

    return remaining_flags # Return the calculated remaining flags


# Update the text label that shows user how many more flags they can place
def update_remaining_flags_label():
    remaining_flags = calculate_remaining_flags() # Get the number of remaining flags
    
    remaining_flags_label.config(text=f"Remaining flags: {remaining_flags}") # Update the label using f string


btns = [[tk.Button(root, width=2, height=1, font=("Arial", 12)) for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        btns[i][j].config(command=lambda i=i, j=j: click(i, j))
        btns[i][j].grid(row=i + 1, column=j + 1)
        btns[i][j].bind("<Button-3>", lambda e, i=i, j=j: flag(i, j, e))
for c in range(N):
    tk.Label(root, text=chr(65 + c), width=2).grid(row=0, column=c + 1)
for r_index in range(N):
    tk.Label(root, text=str(r_index + 1), width=2).grid(row=r_index + 1, column=0)

tk.Button(root, text="Reset", command=reset).grid(row=N + 1, column=0, columnspan=N + 1, sticky="ew")

remaining_flags_label = tk.Label(root, text=f"Remaining flags: {calculate_remaining_flags()}") # Create label to show remaining flag count
remaining_flags_label.grid(row=N + 2, column = 0, columnspan = N + 2) # Set label position

reset()
root.mainloop()
