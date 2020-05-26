"""
Write a function that will take 3 arguments:
bombs = list of bomb locations
rows, columns

mine_sweeper([[0,0],[1,2], 3,4])
bomb at the row index 0 and at the column index 0
bomb at the row index 1 and at the column index 2
3 rows
4 columns
we should return an 3x4 array with the bombs as -1 value
"""

# as for me it is myserable solution in terms of time and space complexity


def mine_sweeper(bombs, num_rows, num_cols):
    field = [[0 for i in range(num_cols)] for j in range(num_rows)]

    for bomb_location in bombs:
        (bomb_row, bomb_col) = bomb_location
        field[bomb_row][bomb_col] = -1

        # +2 added to bomb_row and bomb_col
        # only since the last element in the range is not included
        row_range = range(bomb_row - 1, bomb_row + 2)
        """we encompass a cell before the bomb in a row
        and a cell next after the bomb in the same row
        as adjacent locations to count the bombs around them.
        Same thing with the column"""
        col_range = range(bomb_col - 1, bomb_col + 2)
        """we launch the loop through a row and its columns each time
        when we encounter the bomb in the bomb loop.
        Thus we can see all adjacent cells around them
        and aggregate the number of neighboring bombs"""
        for i in row_range:
            for j in col_range:
                if(0 <= i < num_rows and 0 <= j < num_cols and field[i][j] != -1):
                    field[i][j] += 1
    return field


print(mine_sweeper([[0, 0], [1, 2]], 3, 4))
