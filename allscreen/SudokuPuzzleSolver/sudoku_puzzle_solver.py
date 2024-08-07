from kivy.uix.screenmanager import Screen

class SudokuPuzzleSolverView(Screen):
    def sudoku(self):
        try:
            a1=int(self.ids.a1.text)
            a2=int(self.ids.a2.text)
            a3=int(self.ids.a3.text)
            a4=int(self.ids.a4.text)
            a5=int(self.ids.a5.text)
            a6=int(self.ids.a6.text)
            a7=int(self.ids.a7.text)
            a8=int(self.ids.a8.text)
            a9=int(self.ids.a9.text)
            b1=int(self.ids.b1.text)
            b2=int(self.ids.b2.text)
            b3=int(self.ids.b3.text)
            b4=int(self.ids.b4.text)
            b5=int(self.ids.b5.text)
            b6=int(self.ids.b6.text)
            b7=int(self.ids.b7.text)
            b8=int(self.ids.b8.text)
            b9=int(self.ids.b9.text)
            c1=int(self.ids.c1.text)
            c2=int(self.ids.c2.text)
            c3=int(self.ids.c3.text)
            c4=int(self.ids.c4.text)
            c5=int(self.ids.c5.text)
            c6=int(self.ids.c6.text)
            c7=int(self.ids.c7.text)
            c8=int(self.ids.c8.text)
            c9=int(self.ids.c9.text)
            d1=int(self.ids.d1.text)
            d2=int(self.ids.d2.text)
            d3=int(self.ids.d3.text)
            d4=int(self.ids.d4.text)
            d5=int(self.ids.d5.text)
            d6=int(self.ids.d6.text)
            d7=int(self.ids.d7.text)
            d8=int(self.ids.d8.text)
            d9=int(self.ids.d9.text)
            e1=int(self.ids.e1.text)
            e2=int(self.ids.e2.text)
            e3=int(self.ids.e3.text)
            e4=int(self.ids.e4.text)
            e5=int(self.ids.e5.text)
            e6=int(self.ids.e6.text)
            e7=int(self.ids.e7.text)
            e8=int(self.ids.e8.text)
            e9=int(self.ids.e9.text)
            f1=int(self.ids.f1.text)
            f2=int(self.ids.f2.text)
            f3=int(self.ids.f3.text)
            f4=int(self.ids.f4.text)
            f5=int(self.ids.f5.text)
            f6=int(self.ids.f6.text)
            f7=int(self.ids.f7.text)
            f8=int(self.ids.f8.text)
            f9=int(self.ids.f9.text)
            g1=int(self.ids.g1.text)
            g2=int(self.ids.g2.text)
            g3=int(self.ids.g3.text)
            g4=int(self.ids.g4.text)
            g5=int(self.ids.g5.text)
            g6=int(self.ids.g6.text)
            g7=int(self.ids.g7.text)
            g8=int(self.ids.g8.text)
            g9=int(self.ids.g9.text)
            h1=int(self.ids.h1.text)
            h2=int(self.ids.h2.text)
            h3=int(self.ids.h3.text)
            h4=int(self.ids.h4.text)
            h5=int(self.ids.h5.text)
            h6=int(self.ids.h6.text)
            h7=int(self.ids.h7.text)
            h8=int(self.ids.h8.text)
            h9=int(self.ids.h9.text)
            i1=int(self.ids.i1.text)
            i2=int(self.ids.i2.text)
            i3=int(self.ids.i3.text)
            i4=int(self.ids.i4.text)
            i5=int(self.ids.i5.text)
            i6=int(self.ids.i6.text)
            i7=int(self.ids.i7.text)
            i8=int(self.ids.i8.text)
            i9=int(self.ids.i9.text)

        #to find duplicate in suduko puzzle
            def dup(mylist):
                newlist = [] # empty list to hold unique elements from the list
                duplist = [] # empty list to hold the duplicate elements from the list
                for i in mylist:
                    if i not in newlist:
                        newlist.append(i)
                    else:
                        duplist.append(i) 
                duplist=set(duplist)
                if 0 in duplist:
                    if duplist=={0}:
                        a=False
                    else:
                        a=True
                elif 0 not in duplist:
                    a=True
                else:
                    a=False
                return a

            grid=[[a1,a2,a3,b1,b2,b3,c1,c2,c3]
                 ,[a4,a5,a6,b4,b5,b6,c4,c5,c6]
                 ,[a7,a8,a9,b7,b8,b9,c7,c8,c9]
                 ,[d1,d2,d3,e1,e2,e3,f1,f2,f3]
                 ,[d4,d5,d6,e4,e5,e6,f4,f5,f6]
                 ,[d7,d8,d9,e7,e8,e9,f7,f8,f9]
                 ,[g1,g2,g3,h1,h2,h3,i1,i2,i3]
                 ,[g4,g5,g6,h4,h5,h6,i4,i5,i6]
                 ,[g7,g8,g9,h7,h8,h9,i7,i8,i9]]
            M = 9
            def solve(grid, row, col, num):
                for x in range(9):
                    if grid[row][x] == num:
                        return False
                for x in range(9):
                    if grid[x][col] == num:
                        return False
                startRow = row - row % 3
                startCol = col - col % 3
                for i in range(3):
                    for j in range(3):
                        if grid[i + startRow][j + startCol] == num:
                            return False
                return True
            def Suduko(grid, row, col):
 
                if (row == M - 1 and col == M):
                    return True
                if col == M:
                    row += 1
                    col = 0
                if grid[row][col] > 0:
                    return Suduko(grid, row, col + 1)
                for num in range(1, M + 1, 1): 
     
                    if solve(grid, row, col, num):
         
                        grid[row][col] = num
                        if Suduko(grid, row, col + 1):
                            return True
                    grid[row][col] = 0
                return False
            if a1==0 and a2==0 and a3==0 and a4==0 and a5==0 and a6==0 and a7==0 and a8==0 and a9==0 and b1==0 and b2==0 and b3==0 and b4==0 and b5==0 and b6==0 and b7==0 and b8==0 and b9==0 and c1==0 and c2==0 and c3==0 and c4==0 and c5==0 and c6==0 and c7==0 and c8==0 and c9==0 and d1==0 and d2==0 and d3==0 and d4==0 and d5==0 and d6==0 and d7==0 and d8==0 and d9==0 and e1==0 and e2==0 and e3==0 and e4==0 and e5==0 and e6==0 and e7==0 and e8==0 and e9==0 and f1==0 and f2==0 and f3==0 and f4==0 and f5==0 and f6==0 and f7==0 and f8==0 and f9==0 and g1==0 and g2==0 and g3==0 and g4==0 and g5==0 and g6==0 and g7==0 and g8==0 and g9==0 and h1==0 and h2==0 and h3==0 and h4==0 and h5==0 and h6==0 and h7==0 and h8==0 and h9==0 and i1==0 and i2==0 and i3==0 and i4==0 and i5==0 and i6==0 and i7==0 and i8==0 and i9==0:
                n_sudoku=self.ids.n_sudoku
                n_sudoku.text='Default puzzle ,please enter new puzzle'
    #duplicate check start
            elif dup([a1,a2,a3,b1,b2,b3,c1,c2,c3]):
                n_sudoku=self.ids.n_sudoku
                n_sudoku.text="Don't use same numbers in same column or row."
            elif dup([a4,a5,a6,b4,b5,b6,c4,c5,c6]):
                n_sudoku=self.ids.n_sudoku
                n_sudoku.text="Don't use same numbers in same column or row."
            elif dup([a7,a8,a9,b7,b8,b9,c7,c8,c9]):
                n_sudoku=self.ids.n_sudoku
                n_sudoku.text="Don't use same numbers in same column or row."
            elif dup([d1,d2,d3,e1,e2,e3,f1,f2,f3]):
                n_sudoku=self.ids.n_sudoku
                n_sudoku.text="Don't use same numbers in same column or row."
            elif dup([d4,d5,d6,e4,e5,e6,f4,f5,f6]):
                n_sudoku=self.ids.n_sudoku
                n_sudoku.text="Don't use same numbers in same column or row."
            elif dup([d7,d8,d9,e7,e8,e9,f7,f8,f9]):
                n_sudoku=self.ids.n_sudoku
                n_sudoku.text="Don't use same numbers in same column or row."
            elif dup([g1,g2,g3,h1,h2,h3,i1,i2,i3]):
                n_sudoku=self.ids.n_sudoku
                n_sudoku.text="Don't use same numbers in same column or row."
            elif dup([g4,g5,g6,h4,h5,h6,i4,i5,i6]):
                n_sudoku=self.ids.n_sudoku
                n_sudoku.text="Don't use same numbers in same column or row."
            elif dup([g7,g8,g9,h7,h8,h9,i7,i8,i9]):
                n_sudoku=self.ids.n_sudoku
                n_sudoku.text="Don't use same numbers in same column or row."
            elif dup([a1,a4,a7,d1,d4,d7,g1,g4,g7]):
                n_sudoku=self.ids.n_sudoku
                n_sudoku.text="Don't use same numbers in same column or row."
            elif dup([a2,a5,a8,d2,d5,d8,g2,g5,g8]):
                n_sudoku=self.ids.n_sudoku
                n_sudoku.text="Don't use same numbers in same column or row."
            elif dup([a3,a6,a9,d3,d6,d9,g3,g6,g9]):
                n_sudoku=self.ids.n_sudoku
                n_sudoku.text="Don't use same numbers in same column or row."
            elif dup([b1,b4,b7,e1,e4,e7,h1,h4,h7]):
                n_sudoku=self.ids.n_sudoku
                n_sudoku.text="Don't use same numbers in same column or row."
            elif dup([b2,b5,b8,e2,e5,e8,h2,h5,h8]):
                n_sudoku=self.ids.n_sudoku
                n_sudoku.text="Don't use same numbers in same column or row."
            elif dup([b3,b6,b9,e3,e6,e9,h3,h6,h9]):
                n_sudoku=self.ids.n_sudoku
                n_sudoku.text="Don't use same numbers in same column or row."
            elif dup([c1,c4,c7,f1,f4,f7,i1,i4,i7]):
                n_sudoku=self.ids.n_sudoku
                n_sudoku.text="Don't use same numbers in same column or row."
            elif dup([c2,c5,c8,f2,f5,f8,i2,i5,i8]):
                n_sudoku=self.ids.n_sudoku
                n_sudoku.text="Don't use same numbers in same column or row."
            elif dup([c3,c6,c9,f3,f6,f9,i3,i6,i9]):
                n_sudoku=self.ids.n_sudoku
                n_sudoku.text="Don't use same numbers in same column or row."
    #duplicate check end
            elif (Suduko(grid, 0, 0)):
                [[a1,a2,a3,b1,b2,b3,c1,c2,c3]
                 ,[a4,a5,a6,b4,b5,b6,c4,c5,c6]
                 ,[a7,a8,a9,b7,b8,b9,c7,c8,c9]
                 ,[d1,d2,d3,e1,e2,e3,f1,f2,f3]
                 ,[d4,d5,d6,e4,e5,e6,f4,f5,f6]
                 ,[d7,d8,d9,e7,e8,e9,f7,f8,f9]
                 ,[g1,g2,g3,h1,h2,h3,i1,i2,i3]
                 ,[g4,g5,g6,h4,h5,h6,i4,i5,i6]
                 ,[g7,g8,g9,h7,h8,h9,i7,i8,i9]]=grid
                self.ids.a1.text=str(a1)
                self.ids.a2.text=str(a2)
                self.ids.a3.text=str(a3)
                self.ids.a4.text=str(a4)
                self.ids.a5.text=str(a5)
                self.ids.a6.text=str(a6)
                self.ids.a7.text=str(a7)
                self.ids.a8.text=str(a8)
                self.ids.a9.text=str(a9)
                self.ids.b1.text=str(b1)
                self.ids.b2.text=str(b2)
                self.ids.b3.text=str(b3)
                self.ids.b4.text=str(b4)
                self.ids.b5.text=str(b5)
                self.ids.b6.text=str(b6)
                self.ids.b7.text=str(b7)
                self.ids.b8.text=str(b8)
                self.ids.b9.text=str(b9)
                self.ids.c1.text=str(c1)
                self.ids.c2.text=str(c2)
                self.ids.c3.text=str(c3)
                self.ids.c4.text=str(c4)
                self.ids.c5.text=str(c5)
                self.ids.c6.text=str(c6)
                self.ids.c7.text=str(c7)
                self.ids.c8.text=str(c8)
                self.ids.c9.text=str(c9)
                self.ids.d1.text=str(d1)
                self.ids.d2.text=str(d2)
                self.ids.d3.text=str(d3)
                self.ids.d4.text=str(d4)
                self.ids.d5.text=str(d5)
                self.ids.d6.text=str(d6)
                self.ids.d7.text=str(d7)
                self.ids.d8.text=str(d8)
                self.ids.d9.text=str(d9)
                self.ids.e1.text=str(e1)
                self.ids.e2.text=str(e2)
                self.ids.e3.text=str(e3)
                self.ids.e4.text=str(e4)
                self.ids.e5.text=str(e5)
                self.ids.e6.text=str(e6)
                self.ids.e7.text=str(e7)
                self.ids.e8.text=str(e8)
                self.ids.e9.text=str(e9)
                self.ids.f1.text=str(f1)
                self.ids.f2.text=str(f2)
                self.ids.f3.text=str(f3)
                self.ids.f4.text=str(f4)
                self.ids.f5.text=str(f5)
                self.ids.f6.text=str(f6)
                self.ids.f7.text=str(f7)
                self.ids.f8.text=str(f8)
                self.ids.f9.text=str(f9)
                self.ids.g1.text=str(g1)
                self.ids.g2.text=str(g2)
                self.ids.g3.text=str(g3)
                self.ids.g4.text=str(g4)
                self.ids.g5.text=str(g5)
                self.ids.g6.text=str(g6)
                self.ids.g7.text=str(g7)
                self.ids.g8.text=str(g8)
                self.ids.g9.text=str(g9)
                self.ids.h1.text=str(h1)
                self.ids.h2.text=str(h2)
                self.ids.h3.text=str(h3)
                self.ids.h4.text=str(h4)
                self.ids.h5.text=str(h5)
                self.ids.h6.text=str(h6)
                self.ids.h7.text=str(h7)
                self.ids.h8.text=str(h8)
                self.ids.h9.text=str(h9)
                self.ids.i1.text=str(i1)
                self.ids.i2.text=str(i2)
                self.ids.i3.text=str(i3)
                self.ids.i4.text=str(i4)
                self.ids.i5.text=str(i5)
                self.ids.i6.text=str(i6)
                self.ids.i7.text=str(i7)
                self.ids.i8.text=str(i8)
                self.ids.i9.text=str(i9)
                n_sudoku=self.ids.n_sudoku
                n_sudoku.text='Puzzle Solved'
        except:
            n_sudoku=self.ids.n_sudoku
            n_sudoku.text='Error!'

#Reset sudoku
    def reset_sudoku(self):
        self.ids.a1.text="0"
        self.ids.a2.text="0"
        self.ids.a3.text="0"
        self.ids.a4.text="0"
        self.ids.a5.text="0"
        self.ids.a6.text="0"
        self.ids.a7.text="0"
        self.ids.a8.text="0"
        self.ids.a9.text="0"
        self.ids.b1.text="0"
        self.ids.b2.text="0"
        self.ids.b3.text='0'
        self.ids.b4.text='0'
        self.ids.b5.text='0'
        self.ids.b6.text='0'
        self.ids.b7.text='0'
        self.ids.b8.text='0'
        self.ids.b9.text='0'
        self.ids.c1.text='0'
        self.ids.c2.text='0'
        self.ids.c3.text='0'
        self.ids.c4.text='0'
        self.ids.c5.text='0'
        self.ids.c6.text='0'
        self.ids.c7.text='0'
        self.ids.c8.text='0'
        self.ids.c9.text='0'
        self.ids.d1.text='0'
        self.ids.d2.text='0'
        self.ids.d3.text='0'
        self.ids.d4.text='0'
        self.ids.d5.text='0'
        self.ids.d6.text='0'
        self.ids.d7.text='0'
        self.ids.d8.text='0'
        self.ids.d9.text='0'
        self.ids.e1.text='0'
        self.ids.e2.text='0'
        self.ids.e3.text='0'
        self.ids.e4.text='0'
        self.ids.e5.text='0'
        self.ids.e6.text='0'
        self.ids.e7.text='0'
        self.ids.e8.text='0'
        self.ids.e9.text='0'
        self.ids.f1.text='0'
        self.ids.f2.text='0'
        self.ids.f3.text='0'
        self.ids.f4.text='0'
        self.ids.f5.text='0'
        self.ids.f6.text='0'
        self.ids.f7.text='0'
        self.ids.f8.text='0'
        self.ids.f9.text='0'
        self.ids.g1.text='0'
        self.ids.g2.text='0'
        self.ids.g3.text='0'
        self.ids.g4.text='0'
        self.ids.g5.text='0'
        self.ids.g6.text='0'
        self.ids.g7.text='0'
        self.ids.g8.text='0'
        self.ids.g9.text='0'
        self.ids.h1.text='0'
        self.ids.h2.text='0'
        self.ids.h3.text='0'
        self.ids.h4.text='0'
        self.ids.h5.text='0'
        self.ids.h6.text='0'
        self.ids.h7.text='0'
        self.ids.h8.text='0'
        self.ids.h9.text='0'
        self.ids.i1.text='0'
        self.ids.i2.text='0'
        self.ids.i3.text='0'
        self.ids.i4.text='0'
        self.ids.i5.text='0'
        self.ids.i6.text='0'
        self.ids.i7.text='0'
        self.ids.i8.text='0'
        self.ids.i9.text='0'
        n_sudoku=self.ids.n_sudoku
        n_sudoku.text='Reset Completed'
