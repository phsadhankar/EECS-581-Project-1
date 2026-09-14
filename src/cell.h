//
//  SEMESTER:       EECS 581 Fall 2026
//  PROJECT:        Project 1 - Minesweeper
//  FILE:           cell.h
//
//  DESCRIPTION:    Declares the Cell class and the properties used to represent individual cells on 
//                  the Minesweeper board.
//
//  INPUT:          None
//  OUTPUT:         Cell information, such as mine, flag, covered, and number of adjacent mines.
//
//  COLLABORATORS:  TBD
//  SOURCES:        None
//
//  AUTHOR:         Ivan Kullaya
//  CREATION DATE:  09/12/2026
//
//  AUTHOR'S NOTE:  None
//

#ifndef CELL_H
#define CELL_H

class Cell 
{
    private:
        bool hasMine;       // True if the cell contains a mine
        bool covered;       // True if the cell is covered
        bool flagged;       // True if the cell is flagged
        int adjacentMines;  // Number of mines surrounding this cell (0 to 8)

    public:
        Cell();             // Constructor creates a cell with its default starting values

        // Getter functions to allow other parts of the program to check the current state of the cell
        bool getHasMine() const;
        bool isCovered() const;
        bool isFlagged() const;
        int getAdjacentMines() const;

        // Setter functions to allow the cell's information to change
        void setMine( bool value );
        void setCovered( bool value );
        void setFlagged( bool value );
        void setAdjacentMines( int count );
        void resetCell();
};

#endif
