import Cell
class Automate:
    def __init__(self):
      self.m_cells = {}
      self.createPaths()

    def setGrid(self, grid):
        i = 0
        for l in grid:
            cell = self.m_cells[str(i)]
            cell.setValue(l)
            i = i+1

    def setBonus(self, bonus):
        self.m_bonus = bonus
        for f in self.m_bonus:
            self.m_cells[f].setBonus(self.m_bonus[f])

    def createPaths(self):
        self.m_root = Cell.Cell('')
        self.m_root.isRoot = True
        for i in range(16):
            cell =  Cell.Cell(str(i))
            self.m_cells[str(i)] = cell
            self.m_root.addPath(cell)
## 0  . 1  . 2  . 3
## 4  . 5  . 6  . 7
## 8  . 9  . 10 . 11
## 12 . 13 . 14 . 15
           
        self.createLinks(0, [1, 4, 5])
        self.createLinks(1, [0, 2, 4, 5, 6])
        self.createLinks(2, [1, 3, 5, 6, 7])
        self.createLinks(3, [2, 6, 7])
        self.createLinks(4, [0, 1, 5, 8, 9])
        self.createLinks(5, [0,1, 2, 4, 6, 8, 9, 10])
        self.createLinks(6, [1, 2, 3, 5, 7, 9, 10, 11])
        self.createLinks(7, [2, 3, 6, 10, 11])
        self.createLinks(8, [4, 5, 9, 12, 13])
        self.createLinks(9, [4, 5, 6, 8, 10, 12, 13, 14])
        self.createLinks(10, [5, 6, 7, 9, 11, 13, 14, 15])
        self.createLinks(11, [6, 7, 10, 14, 15])
        self.createLinks(12, [8, 9, 13])
        self.createLinks(13, [8, 9, 10, 12, 14])
        self.createLinks(14, [9, 10, 11, 13, 15])
        self.createLinks(15, [10, 11, 14])

    def createLinks(self, cellId, cellIds):
        cell = self.m_cells[str(cellId)]
        for nodeId in cellIds:
            node = self.m_cells[str(nodeId)]
            cell.addPath(node)

    def findWordPath(self, word):
        idx = -1
        params = {"word": word, "idx": idx }
        res = self.m_root.match(params)
        return res


    def findBestWordPath(self, word):
        result = self.findWordPath(word)
        if result.isMatching == False:
            return Cell.Path()
        bestScore = 0
        bestResult = None
        for path in result.paths:
            currentScore = path.getPoints()
            if currentScore > bestScore:
                bestScore = currentScore
                bestResult = path
        return bestResult

    def getCell(self, i):
       return self.m_cells[str(i)]

    def displayGrid(self):
        i = 0
        for i in range(16):
            cell = self.getCell(i)
            print(cell.getDisplay(), end=' ')
            i = i+1
            if i %4 == 0:
                print('')

