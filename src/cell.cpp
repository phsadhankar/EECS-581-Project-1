//
//  SEMESTER:       EECS 581 Fall 2026
//  PROJECT:        Project 1 - Minesweeper
//  FILE:           cell.cpp
//
//  DESCRIPTION:    Implements the Cell class functions used to access and modify individual cell 
//                  states.
//
//  INPUT:          Values used to update the cell's state
//  OUTPUT:         Current information about the cell
//
//  COLLABORATORS:  TBD
//  SOURCES:        None
//
//  AUTHOR:         Ivan Kullaya
//  CREATION DATE:  09/12/2026
//
//  AUTHOR'S NOTE:  None
//

#include "cell.h"

// Constructor to build Cell and calls resetCell() to reset the cell
Cell::Cell() 
{
    resetCell();
}

// Returns true if the cell contains a mine
bool Cell::getHasMine() const
{
    return hasMine;
}

// Returns true if the cell is still covered
bool Cell::isCovered() const
{
    return covered;
}

// Returns true if the cell currently has a flag
bool Cell::isFlagged() const
{
    return flagged;
}

// Returns the number of mines surrounding this cell
int Cell::getAdjacentMines() const
{
    return adjacentMines;
}

// Sets whether this cell contains a mine
void Cell::setMine( bool value )
{
    hasMine = value;
}

// Sets whether this cell is covered
void Cell::setCovered( bool value )
{
    covered = value;
}

// Sets whether this cell has a flag
void Cell::setFlagged ( bool value )
{
    flagged = value;
}

// Sets the number of mines surrounding this cell
void Cell::setAdjacentMines( int count )
{
    adjacentMines = count;
}

// Resets the cell to its default starting values
void Cell::resetCell()
{
    hasMine = false;
    covered = true;
    flagged = false;
    adjacentMines = 0;
}
