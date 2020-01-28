"""
Part 3: Full implementation of bookshelf problem
"""
import argparse
import os
from part1 import parse_input, save_moves
from part2 import _get_dp_matrix, _backtrack_list

class Shelf():
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        self.optimal_sequence = []
        self.input_arrangement = []
        self.output_arrangement = []
        self._load_conditions()

    def _load_conditions(self):
        self.input_arrangement, self.output_arrangement = parse_input(self.input_file)

    def _save_moves(self):
        save_moves(self.optimal_sequence, self.output_file)

    def get_moves(self):
        dp_mtx = _get_dp_matrix(self.input_arrangement, self.output_arrangement)
        self.optimal_sequence = _backtrack_list(dp_mtx, self.output_arrangement)
        self._save_moves()

if __name__ == "__main__":
    isOut = False
    cwd = os.getcwd()
    parser = argparse.ArgumentParser(description="Part 3")
    parser.add_argument("input_file", help="Input file")
    args = parser.parse_args()

    input_file = os.path.join(cwd, "input-files", args.input_file)
    tail = os.path.split(input_file)[1]
    name = os.path.splitext(tail)[0]
    output_file = name + ".out"
    for dirName, subdirList, fileList in os.walk(cwd):
        for fname in fileList:
            if fname == output_file:
                isOut = True
    
    if not isOut:
        output_file = os.path.join(cwd, "output-files", output_file)
        shelf = Shelf(input_file, output_file)
        optimal_moves = shelf.get_moves()