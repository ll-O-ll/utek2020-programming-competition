"""
Part 1: Input and Output
"""
import os

def parse_input(input_file):
    '''
    Read input file (".in" format); organizes initial and final
    arrangements into two lists

    Input: Path to input file (str; must be ".in" format)
    Outputs: Current / input arrangement (list:str)
             Output / desired arrangement (list:str)
    '''
    original_arrangement = []
    desired_arrangement = []

    with open(input_file, "r", encoding="utf8") as f:
        filecontent = f.readlines()
        
        output_status = False
        for line in filecontent:
            line = line.strip("\n")

            if line == "":
                continue

            elif line.startswith("Original"):
                output_status = False
                continue

            elif line.startswith("Desired"):
                output_status = True
                continue

            if not output_status:
                original_arrangement.append(line)
            else:
                desired_arrangement.append(line)

    return original_arrangement, desired_arrangement


def save_moves(moves, output_file):
    '''
    Save moves into a file

    Inputs: List of moves (list)
            Path of file to save output (str; must be ".out" format)
    Output: None; saves file
    '''
    with open(output_file, "w", encoding="utf8") as f:
        for move in moves:
            f.write(move + "\n")


if __name__ == "__main__":
    # Load conditions
    cwd = os.getcwd()
    original_arrangement, desired_arrangement = parse_input(os.path.join(cwd, "data", "part11.in"))
    print(original_arrangement)
    print(desired_arrangement)

    # Save moves
    moves = ["Insert 0-0 'Religion and Mythology, Neil Potts'", "Replace 2-2 'Intro to Algorithms, Thomas Cormen'"]
    save_moves(moves, "example.out")