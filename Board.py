class Board:
    def __init__(self) -> None:
        self.board = []
        self.iters = 0
        self.board_state()

    def board_state(self):
        self.board = [
            [7,8,0,4,0,0,1,2,0],
            [6,0,0,0,7,5,0,0,9],
            [0,0,0,6,0,1,0,7,8],
            [0,0,7,0,4,0,2,6,0],
            [0,0,1,0,5,0,9,3,0],
            [9,0,4,0,6,0,0,0,5],
            [0,7,0,3,0,0,0,1,2],
            [1,2,0,0,0,7,4,0,0],
            [0,4,9,2,0,6,0,0,7]
        ]

    def is_valid(self, num:int, pos:tuple) -> bool:
        for i in range(len(self.board[0])):
            if self.board[pos[0]][i] == num and pos[1] != i:
                return False

        for i in range(len(self.board)):
            if self.board[i][pos[1]] == num and pos[0] != i:
                return False
        
        box_x = pos[1] // 3
        box_y = pos[0] // 3

        for i in range(box_y*3, box_y*3 + 3):
            for j in range(box_x*3, box_x*3 +3):
                if self.board[i][j] == num and (i,j) != pos:
                    return False
        return True

    def find_empty(self)-> tuple:
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == 0:
                    return(i,j)
        return (-1, -1)

    def solve(self) -> bool:
        find = self.find_empty()
        if find == (-1, -1):
            return True
        row, col = find

        for i in range(1,10):
            if self.is_valid(i, (row, col)):
                self.board[row][col] = i

                if self.solve():
                    return True
                self.board[row][col] = 0
        return False
        
        
    def __str__(self) -> str:
        print_str = ""
        for i in range(len(self.board)):
            if i % 3 == 0 and i != 0:
                print_str += "-----------------------\n"
            
            for j in range(len(self.board[0])):
                if j % 3 == 0 and j != 0:
                    print_str += " | "

                print_str += str(self.board[i][j])
                print_str += "\n" if j == len(self.board[0]) -1 else " "
                    
                    
        return print_str


        #return super().__str__()

    
a = Board()
print(a)
solved = a.solve()
print(a) if solved else print("Not solvable")