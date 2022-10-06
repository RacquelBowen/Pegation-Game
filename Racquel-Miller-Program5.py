import numpy as np
import string

# ---------------------------------------
# CSCI 127, Joy and Beauty of Data      |
# Program 5: Pegathon                   |
# Your Name(Racquel Miller)             |
# Last Modified: November 15, 2021      |
# ---------------------------------------
# A brief overview of the program.
# ---------------------------------------

# ---------------------------------------
# Start of Pegathon Class               |
# ---------------------------------------

class Pegathon:

    def __init__(self, rows, columns, empty_row, empty_col):
        self.board = np.full((rows, columns), True)
        self.board[empty_row][empty_col] = False
        self.pegs_left = rows * columns - 1
        
# ---------------------------------------

    def __str__(self):
        answer = "   "
        for column in range(self.board.shape[1]):
            answer += " " + str(column + 1) + "  "
        answer += "\n"
        answer += self.separator()
        for row in range(self.board.shape[0]):
            answer += str(row + 1) + " |"
            for col in range(self.board.shape[1]):
                if self.board[row][col]:
                    answer += " o |"
                else:
                    answer += "   |"
            answer += "\n"
            answer += self.separator()
        return answer

    
# ---------------------------------------

    def separator(self):
        answer = "  +"
        for _ in range(self.board.shape[1]):
            answer += "---+"
        answer += "\n"
        return answer

# ---------------------------------------
# The four missing methods go here.  Do |
# not modify anything else.             |
# --------------------------------------|

    def game_over(self):
#gets the number of rows there are from the length of 'self.board'
        num_rows = len(self.board)
#gets the number of columns there are from adding 1 to 'pegs_left' and
#divides it by the length of 'self.board' and return the integer number
#of that value
        num_columns = int((self.pegs_left + 1) / len(self.board))
        north = ""
        east = ""
        south = ""
        west = ""
        Y_or_N = []
#checks each row individually and in that row it checks each column
        for y in range(0, num_rows):
            for x in range(0, num_columns):
#if the self.board value in the sepcific row and column is False, meaning it
#doesn't have a peg it checks to see if two spots around them, North, East,
#South, and West and diagonally of the False value have a peg in that slot,
#if so, it assigns 'east', west, 'south', and 'north' to be the string "Yes"
                if self.board[y][x] == False:
                    if (y - 2) >= 0:
                        if self.board[y-1][x] and self.board[y-2][x]:
                            north = "Yes"
#appends 'north' to the list 'Y_or_N'
                            Y_or_N.append(north)
                    if (y - 2) >= 0:
                        if (x + 2) < num_columns:
                            if self.board[y-1][x+1] and self.board[y-2][x+2]:
                                northeast = "Yes"
#appends 'northeast' to the list 'Y_or_N'
                                Y_or_N.append(northeast)
                    if (x + 2) < num_columns:
                        if self.board[y][x+1] and self.board[y][x+2]:
                            east = "Yes"
#appends 'east' to the list 'Y_or_N'
                            Y_or_N.append(east)
                    if (x + 2) < num_columns:
                        if (y + 2) < num_rows:
                            if self.board[y+1][x+1] and self.board[y+2][x+2]:
                                southeast = "Yes"
#appends 'southeast' to the list 'Y_or_N'
                                Y_or_N.append(southeast)
                    if (y + 2) < num_rows:
                        if self.board[y+1][x] and self.board[y+2][x]:
                            south = "Yes"
#appends 'south' to the list 'Y_or_N'
                            Y_or_N.append(south)
                    if (y + 2) < num_rows:
                        if (x - 2) >= 0:
                            if self.board[y+1][x-1] and self.board[y+1][x-2]:
                                southwest = "Yes"
#appends 'southwest' to the list 'Y_or_N'
                                Y_or_N.append(southwest)
                    if (x - 2) >= 0:
                        if self.board[y][x-1] and self.board[y][x-2]:
                            west = "Yes"
#appends 'west' to the list 'Y_or_N'
                            Y_or_N.append(west)
                    if (x - 2) >= 0:
                        if (y - 2) >= 0:
                            if self.board[y-1][x-1] and self.board[y-2][x-2]:
                                northwest = "Yes"
#appends 'northwest' to the list 'Y_or_N'
                                Y_or_N.append(northwest)
#checks to see if the string "Yes" is in the list 'Y_or_N', if so it returns False
        for i in range(0, len(Y_or_N)):
            if Y_or_N[i] == "Yes":
                Y_or_N.clear()
                return False
        else:
            return True

    def final_message(self):
#gets the number of rows there are from the length of 'self.board'
        num_rows = len(self.board)
#gets the number of columns there are from adding 1 to 'pegs_left' and
#divides it by the length of 'self.board' and return the integer number
#of that value
        num_columns = int((self.pegs_left + 1) / len(self.board))
        count = 0
#checks to see if the function 'game_over' from the same class 'Pegathon' is True
        if self.game_over():
#goes through each row and then in that row, checks to see if each column's value
#is True, if it is, it adds 1 to the value 'count'
            for i in range(0, num_rows):
                for j in range(0, num_columns):
                    if self.board[i][j] == True:
                        count += 1
#checks to see if 'count' is less than or equal to 2
            if count <= 2:
                print("Number of Pegs left:", count, "\nYou're a Peg-genious!")
#checks to see if 'count' is equivalent to 3 or 4
            elif count == 3 or count == 4:
                print("Number of Pegs left:", count, "\nI've worked with better. But not many.")
#checks to see if 'count' is equicalent to 5 or 6
            elif count == 5 or count == 6:
                print("Number of Pegs left: " + str(count) + "\n" + str(count) + " left? Really? You're gonna have to do better than that.")
#checks to see if the 'count' is equal to or greater than 7
            elif count >= 7:
                print("Number of Pegs left:", count, "\nPeg-naramous! Rack 'em up and redeem yourself")
            
    def legal_move(self, row_start, col_start, row_end, col_end):
#finds the index number of the middle peg for its row and column
        row_mid_end_start = int((row_end + row_start)/2)
        row_mid_start_end = int((row_start + row_end)/2)
        col_mid_end_start = int((col_end + col_start)/2)
        col_mid_start_end = int((col_start + col_end)/2)

#checks to see if that peg's index is a positive value for its row and column
        if row_mid_end_start >= 0:
            mid_row = row_mid_end_start
        if row_mid_start_end >= 0:
            mid_row = row_mid_start_end
        if col_mid_end_start >= 0:
            mid_col = col_mid_end_start
        if col_mid_start_end >= 0:
            mid_col = col_mid_start_end
#checks to see if the starting row and column have a peg , and it checks to see
#if the chosen peg will land in an empty peg spot, and checks to see if there
#is a peg it can jump over, making it a legal move
        if self.board[row_start][col_start] == True and self.board[row_end][col_end] == False and self.board[mid_row][mid_col] == True:
            return True
        else:
            return False
        
    def make_move(self, row_start, col_start, row_end, col_end):
        final_row = 0
        final_col = 0
#gets the indexs for the row and column of the peg being jumped over
        row_remove_end_start = int((row_end + row_start)/2)
        row_remove_start_end = int((row_start + row_end)/2)
        col_remove_end_start = int((col_end + col_start)/2)
        col_remove_start_end = int((col_start + col_end)/2)
#checks to see if the peg's index values are positve numbers
        if row_remove_end_start >= 0:
            final_row = row_remove_end_start
        if row_remove_start_end >= 0:
            final_row = row_remove_start_end
        if col_remove_end_start >= 0:
            final_col = col_remove_end_start
        if col_remove_start_end >= 0:
            final_col = col_remove_start_end
#sets the starting peg index to have no peg in its box, and then sets the ending
#peg index to have a peg in the specified index slot, finally it sets the middle
#peg being jumped over to have no peg in it by getting the indexes of the
#'final_row' and 'final_col'
        self.board[row_start][col_start] = False
        self.board[row_end][col_end] = True
        self.board[final_row][final_col] = False
        return self.board

# ---------------------------------------
# End of Pegathon Class                 |
# ---------------------------------------

def get_choice(low, high, message):
    message += " [" + str(low) + " - " + str(high) + "]: "
    legal_choice = False
    while not legal_choice:
        legal_choice = True
        answer = input(message)
        for character in answer:
            if character not in string.digits:
                legal_choice = False
                print("That is not a number, try again.")
                break 
        if legal_choice:
            answer = int(answer)
            if (answer < low) or (answer > high):
                legal_choice = False
                print("That is not a valid choice, try again.")
    return answer

# ---------------------------------------

def main():
    print("Welcome to Pegathon!")
    print("-----------------------------------\n")
    
    rows = get_choice(1, 9, "Enter the number of rows")
    columns = get_choice(1, 9, "Enter the number of columns")
    row = get_choice(1, rows, "Enter the empty space row") - 1
    column = get_choice(1, columns, "Enter empty space column") - 1   
    game = Pegathon(rows, columns, row, column)
    print()

    print(game)
    while (not game.game_over()):
        row_start = get_choice(1, rows, "Enter the row of the peg to move") - 1
        col_start = get_choice(1, columns, "Enter the column of the peg to move") - 1
        row_end = get_choice(1, rows, "Enter the row where the peg lands") - 1
        col_end = get_choice(1, columns, "Enter the column where the peg lands") - 1
        if game.legal_move(row_start, col_start, row_end, col_end):
            game.make_move(row_start, col_start, row_end, col_end)
        else:
            print("Sorry.  That move is not allowed.")
        print()
        print(game)
    game.final_message()

# ---------------------------------------

main()
