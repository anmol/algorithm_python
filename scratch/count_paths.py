#!/usr/bin/python3


def valid_cell(grid, row, col):
    pass


def is_end(grid, row, col):
    pass


def count_paths(grid, row, col):
    if not valid_cell(grid, row, col):
        return 0
    if is_end(grid, row, col):
        return 1
    return count_paths(grid, row+1, col) + count_paths(grid, row, col+1)

if __name__ == '__main__':
