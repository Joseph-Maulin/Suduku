import sys


class suduku_solver:
    def __init__(self, puzzle):
        self.cell_cache = {}
        self.init_values = {}
        self.puzzle = puzzle
        self.puzzle_array = None
        self.keys = []
        self.read_into_arr()
        self.set_cell_cache()

    def read_into_arr(self):
        self.puzzle_array = self.puzzle.split()
        for row in range(len(self.puzzle_array)):
            self.puzzle_array[row] = [int(x) for x in self.puzzle_array[row]]

    def search(self):

        place = 0
        per_iter = 1
        while place < len(self.keys)+1:

            # break when complete
            if place == len(self.keys):
                break

            # get cell row and col
            row = self.keys[place] // 9
            col = self.keys[place] % 9

            # reset key values - tried
            values = self.check_values(self.keys[place])
            self.cell_cache[self.keys[place]]['values'] = values
            for num in self.cell_cache[self.keys[place]]['tried']:
                del self.cell_cache[self.keys[place]]['values'][self.cell_cache[self.keys[place]]['values'].index(num)]


            # if values
            if self.cell_cache[self.keys[place]]['values']:

                # set tried and add to puzzle
                value = self.cell_cache[self.keys[place]]['values'][0]
                self.puzzle_array[row][col] = value
                self.cell_cache[self.keys[place]]['tried'].append(value)

                # move up key place
                place += 1

            # revert
            else:
                # empty place tried
                self.cell_cache[self.keys[place]]['tried'] = []
                self.puzzle_array[row][col] = 0
                place -= 1
                row = self.keys[place] // 9
                col = self.keys[place] % 9
                self.puzzle_array[row][col] = 0

        self.set_solution()

        # print solution
        for line in self.puzzle_array:
            print(line)


    def set_solution(self):
        self.solution = {}
        for x in range(81):
            row = x // 9
            col = x % 9
            self.solution[x] = self.puzzle_array[row][col]



    def set_cell_cache(self):
        cell_index = 0
        while cell_index < 81:
            values = self.check_values(cell_index)
            if values:
                self.cell_cache[cell_index] = {'values':self.check_values(cell_index), 'tried':[]}
                self.keys.append(cell_index)
            cell_index += 1


    def check_values(self, cell):
        nums = [x for x in range(1,10)]

        row = cell // 9
        col = cell % 9

        if self.puzzle_array[row][col] != 0:
            self.init_values[cell] = self.puzzle_array[row][col]
            return []

        for i in range(9):

            # row
            num = self.puzzle_array[row][i]
            if num > 0:
                try:
                    del nums[nums.index(num)]
                except:
                    pass

            # col
            num = self.puzzle_array[i][col]
            if num > 0:
                try:
                    del nums[nums.index(num)]
                except:
                    pass

        # block
        row_block = row // 3
        col_block = col // 3

        # 0  - range(0,3)
        # 1 - range(3,6)
        # 2 - range(6, 9)
        for i in range(3 * row_block, 3 + 3 * row_block):
            for j in range(3 * col_block, 3 + 3 * col_block):
                num = int(self.puzzle_array[i][j])
                if num > 0:
                    try:
                        del nums[nums.index(num)]
                    except:
                        continue
        return nums


if __name__ == "__main__":
    p="""
    000100502
    000090000
    098500070
    000061000
    005000040
    920050030
    000704008
    000000709
    350000006
    """
    # a = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
    # [6, 7, 2, 1, 9, 5, 3, 4, 8],
    # [1, 9, 8, 3, 4, 2, 5, 6, 7],
    # [8, 1, 9, 7, 6, 4, 0, 0, 3],
    # [4, 0, 0, 8, 0, 3, 0, 0, 1],
    # [7, 0, 0, 0, 2, 0, 0, 0, 6],
    # [0, 6, 0, 0, 0, 0, 2, 8, 0],
    # [0, 0, 0, 4, 1, 9, 0, 0, 5],
    # [0, 0, 0, 0, 8, 0, 0, 7, 9]]



    solver = suduku_solver(p)
    print(solver.puzzle_array)
    print(solver.init_values)

    # solver.puzzle_array = a
    # print(solver.check_values(33))
    solver.search()
    print(solver.solution)
