"""
Part 2: Implementation for strings
"""
import argparse

def get_optimal_moves(input_word, output_word):
    '''
    Main function for getting optimal moves

    Inputs: Input word (str),
            Output word (str)
    Output: DP matrix (list:list:int)
    '''
    dp_mtx = _get_dp_matrix(input_word, output_word)
    optimal_sequence = _backtrack_list(dp_mtx, output_word)
    return optimal_sequence

def print_matrix(matrix):
    for row in matrix:
        print(row)

def _get_dp_matrix(input_list, output_list):
    '''
    Get dynamic programming matrix for input and output words

    Inputs: Input word (str),
            Output word (str)
    Output: DP matrix (list:list:int)
    '''
    if not input_list and not output_list:
        return 0
    
    m = len(input_list)
    n = len(output_list)
    
    dp_mtx = [list(range(n+1))] + [[r+1] + [max(m, n)] * n for r in range(m)]
    
    for i in range(m):
        for j in range(n):
            dp_mtx[i+1][j+1] = min(1 + dp_mtx[i+1][j], 
                                   1 + dp_mtx[i][j+1], 
                                   dp_mtx[i][j] + (0 if input_list[i] == output_list[j] else 1))
        
    return dp_mtx

def _backtrack_list(matrix, output_list):
    '''
    Iteratively backtrack DP matrix to get optimal set of moves

    Inputs: DP matrix (list:list:int),
            Input word (str),
            Output word (str),
            Start x position in DP matrix (int),
            Start y position in DP matrix (int)
    Output: Optimal path (list)
    '''
    
    i = len(matrix) - 1
    j = len(matrix[0]) - 1
    optimal_path = []
    while i > 0 and j > 0:
        diagonal = matrix[i-1][j-1]
        vertical = matrix[i-1][j]
        horizontal = matrix[i][j-1]
        current = matrix[i][j]
        if diagonal <= vertical and diagonal <= horizontal and (diagonal <= current):
            # replace or no-operations
            i = i - 1
            j = j - 1
            if diagonal == current - 1:
                # replace or no-operations
                optimal_path.append("Replace " + str(j) + ", " + str(output_list[j]) )
            elif horizontal <= vertical and horizontal <= current:
                # insert
                j = j - 1
                optimal_path.append("Insert " + str(j) + ", " + str(output_list[j]))
            elif vertical <= horizontal and vertical <= current:
                # delete
                i = i - 1
                optimal_path.append("Delete " + str(i))
        elif horizontal <= vertical and horizontal <= current:
            # insert
            j = j - 1
            optimal_path.append("Insert " + str(j) + ", " + str(output_list[j]))
        else:
            # delete
            i = i - 1
            optimal_path.append("Delete " + str(i))

    return reversed(optimal_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Part 2")
    parser.add_argument("input_word", help="Input word")
    parser.add_argument("output_word", help="Output word")

    args = parser.parse_args()
    optimal_moves = get_optimal_moves(args.input_word, args.output_word)
    dp_matrix = _get_dp_matrix(args.input_word, args.output_word)
    
    for move in optimal_moves:
        print(move)
    print("Number of optimal moves: " + str(dp_matrix[-1][-1]))