import os
import csv

MY_DIR = os.path.dirname(os.path.realpath(__file__))
MY_CONFIG_FILE = 'starting_board_10x10.csv'


def display_board(board, gen):
    """
    take the board as a list of lists and display each entry.
    The board is a m x n rectangular list that contains
    either 0 or 1 in it.

    If it contains a 0, print a dot char ('.')
    If it contains a 1, print a star char ('*')
    recall that print( 'foo', end='') will prevent a newline to be printed

    TODO: iterate thru the list of lists and display each position of the board
    """
    print(f'Displaying board for generation {gen}')

    # TODO: complete the display board code

def count_num_neighbors(board, row, col):
    """
    take the row and col and find out how many neighbors the square has
    """
    pass

    # TODO: calculate the number of neighbors that a square has

    return -1

def update_board(board):
    """
    This function will update the board using the rules for
    how to update each square.

    iterate thru the board.  When the function ends, the board should be
    updated to reflect the next generation.

    The rules for updating the board from 1 generation to another:

    if the square has a '1' in it it is considered "populated"
    if the square has a '0' in it is is considered 'empty'

    Check each square in your grid.
    If it has a 1 in it, then :
         * if it has 1 or 0 "neighbors" (populated adjacent squares, including
         diagonals), then it "dies" (loneliness).  So the square will be
         updated to be 0.
         * if it has 4 or more "neighbors" (including diagonals), then it
         "dies" (overcrowding).  So the square will be updated to 0
         * if it has 2 or 3 neighbors, then it is happy and stays alive
    If it has a 0 in it, then :
         * If it has precisely 3 neighbors (not more, not fewer), then a
         new entity is "born".  So the square will be updated to 1
         * Any other number of neighbors causes no change and the square
         stays 0
    Edge/Corner case :
         for squares on the edge or corner of the map, DO NOT wrap around the
         map.  ie., a corner square has only 3 neighboring squares.  a
         Non-corner Edge square has 5 neighbors.
    """
    pass

    # TODO: modify the board to reflect the next generation

def load_board(board, infile_name):
    """
    open the CSV file and read in the values.  These will
    all be 1s or 0s and should populate the initial board.
    """
    pass

    # TODO: load the csv file int the board

def main():
    """
    Main loop
    """
    print('hello, starting Conway Life')

    # Init primary vars
    board = []
    num_rows = 10
    num_cols = 10

    infile_name = MY_DIR + '/' + MY_CONFIG_FILE

    load_board(board, infile_name)

    generations_to_do = 10

    for i in range(generations_to_do-1):
        display_board(board, i)
        update_board(board)

    # do one final display to show end state
    display_board(board, i+1)




if __name__ == '__main__':
    main()
