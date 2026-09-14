//
//  SEMESTER:       EECS 581 Fall 2026
//  PROJECT:        Project 1 - Minesweeper
//  FILE:           board.h
//
//  DESCRIPTION:    Declares the Board class used to represent and manage the 10x10 Minesweeper grid.
//
//  INPUT:          Row and column position to access the cell
//  OUTPUT:         Cell information and the current game board
//
//  COLLABORATORS:  TBD
//  SOURCES:        C++ w3Schools (https://www.w3schools.com/cpp/)
//
//  AUTHOR:         Ivan Kullaya
//  CREATION DATE:  09/12/2026
//
//  AUTHOR'S NOTE:  None
//

#ifndef BOARD_H
#define BOARD_H

#include "cell.h"

class Board 
{
    private:
        static const int SIZE = 10;     // Size fixed at a 10x10 minesweeper gameboard for this project
        Cell grid[SIZE][SIZE];          // Creates a 10x10 array of cell objects

    public:
        Board();                        // Constructor creates a board

        int getSize() const;                    // Getter function to returns the size of the board
        Cell& getCell( int row, int column );   // Getter function to return a specific cell

        void resetBoard();      // Resets every cell on board to the default state
};

#endif
