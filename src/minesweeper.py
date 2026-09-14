import tkinter as tk, random # Imports tkinter
root = tk.Tk(); # Create main window
root.title("Minesweeper") # Sets the title of the window to "Minesweeper"

N, M = 10, 15 # Sets the size of the grid to 10x10 and the number of mines to 15

b = [[0]*N for _ in range(N)]; # Creates a 2D array of zeros for the board
r = [[False]*N for _ in range(N)]; # Creates a 2D array of False values for revealed cells
f = [[False]*N for _ in range(N)]  # Creates a 2D array of False values for flags

done = False # Create a variable for game state

def reveal(x, y): # Create a function for when the user clicks on a cell when not done
    if not (0 <= x < N and 0 <= y < N and not r[x][y] and not f[x][y]): return # Checks if the cell is out of bounds, revealed, or flagged
    r[x][y] = True # Reveal cell
    if b[x][y] == -1: # Check if the cell is a mine, then reveal all mines and end the game
        for p in range(N): # Iterate through the rows
            for q in range(N): # Iterate through the columns
                if b[p][q] == -1: # Check if the cell is a mine
                    btns[p][q].config(text="💥", bg="red") # Sets the cells to be the boom text and red background
        done = True # Sets the game state to done
        if tk.messagebox.askyesno("Minesweeper", "Boom! You lost. Play again?"): reset() # Prompt player to play again
        else: root.destroy() # If not, close the window
        return # Return from function
    btns[x][y].config(relief=tk.SUNKEN, text=str(b[x][y] or ""), bg="lightgray", fg=["blue","green","red","navy","brown","teal","black","gray"][b[x][y]]) # Set the cell to be clicked with the color corresponding to the number of mines
    if b[x][y] == 0: # Check if cell is empty
        for i in (-1,0,1): # Iterate through the rows by -1, 0, and 1 which represents the adjacent cells
            for j in (-1,0,1): reveal(x+i, y+j) # Reveal adjacent cells
    if sum(sum(r,[])) == N*N-M: done = True; tk.messagebox.showinfo("Minesweeper", "You win!"); root.destroy() # Check if revealed cells = total cells - mines, then end the game and show win message

def click(x, y): # Create a function for when the user clicks on a cell
    if not done: reveal(x, y) # If the game is not done, reveal the cell

def flag(x, y, e): # Create a function for when the user right-clicks on a cell to flag the cell
    if done or r[x][y]: return # Check if game is done or the cell is revealed, if so return from function
    f[x][y] = not f[x][y] # Toggle the flag state of the cell (from unflagged to flagged or unflagged to flagged)
    btns[x][y].config(text="🚩" if f[x][y] else "") # Put the flag text on the cell
    return "break" # Return from function

def reset(): # Create a function to reset the game
    for i in range(N): # Iterate through the rows
        for j in range(N): # Iterate through the columns
            r[i][j] = f[i][j] = False # Reset revealed and flagged states of the cell
            b[i][j] = 0 # Reset the value of the cell
            btns[i][j].config(text="", bg="SystemButtonFace", relief=tk.RAISED) # Reset the cell to be unclicked and unflagged
    for m in random.sample([(i,j) for i in range(N) for j in range(N)], M): b[m[0]][m[1]] = -1 # Randomly put mines on the board
    for i in range(N): # Iterate through the rows
        for j in range(N): # Iterate through the columns
            if b[i][j] != -1: # Check if the cell is not a mine
                b[i][j] = sum(b[x][y] == -1 for x in range(max(0,i-1),min(N,i+2)) for y in range(max(0,j-1),min(N,j+2))) # Count number of nearby mines to set the cell to that number
    done = False # Reset the game state to not done

btns = [[tk.Button(root, width=2, height=1, font=("Arial", 12)) for _ in range(N)] for _ in range(N)] # Create a 2D array of buttons for the grid
for i in range(N): # Iterate through the rows
    for j in range(N): # Iterate through the columns
        btns[i][j].config(command=lambda i=i, j=j: click(i, j)); btns[i][j].grid(row=i, column=j) # Make the button clickable and trigger the click function when clicked
        btns[i][j].bind("<Button-3>", lambda e, i=i, j=j: flag(i, j, e)) # Make right-clicking the button trigger the flag function
reset() # Reset the game (which also makes the new game initially)
tk.Button(root, text="Reset", command=reset).grid(row=N, column=0, columnspan=N, sticky="ew") # Create a button to reset the game
root.mainloop() # Start GUI
