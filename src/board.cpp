//
//  SEMESTER:       EECS 581 Fall 2026
//  PROJECT:        Project 1 - Minesweeper
//  FILE:           board.cpp
//
//  DESCRIPTION:    Implements the Board class functions used to create, access, reset, and manage 
//                  the 10x10 Minesweeper grid.
//
//  INPUT:          Row and column positions
//  OUTPUT:         Updated board and cell information
//
//  COLLABORATORS:  TBD
//  SOURCES:        None
//
//  AUTHOR:         Ivan Kullaya
//  CREATION DATE:  09/12/2026
//
//  AUTHOR'S NOTE:  TBD
//

#include "board.h"

// Constructor to build Board and calls resetBoard() to reset every cell in the board
Board::Board()
{
    resetBoard();
}

// Returns the board size (which should always be 10)
int Board::getSize() const
{
    return SIZE;
}

// Returns the cell located in the row/column
Cell& Board::getCell( int row, int column )
{
    return grid[row][column];
}

// Resets every cell in the board to its original starting state
void Board::resetBoard() 
{
    for ( int row = 0; row < SIZE; row++ )    // Loops through every row
    {
        for ( int column = 0; column < SIZE; column++ )     // Loops through every column
        {
            grid[row][column].resetCell();
        }
    }
}
