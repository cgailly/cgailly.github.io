from termcolor import colored

class Path(object):
    def __init__(self):
        self.path = []
        self.wordMult = 1
        self.points = 0
        
    def getPoints(self):
        return self.wordMult * self.points + len(self.path)

class MatchResult(object):
    def __init__(self):
        self.isMatching = False
        self.paths = []
    

def badResult():
    result = MatchResult()
    result.isMatching = False
    return result

def goodResult():
    result = MatchResult()
    result.isMatching = True
    return result

def createPath(cellId, points, wMult):
    result = Path()
    updatePath(result, cellId, points, wMult)
    return result

def updatePath(path, cellId, points, wMult):
    path.path.insert(0, cellId)
    path.wordMult = path.wordMult * wMult
    path.points = path.points + points
    return path

class Cell:    
    def __init__(self, id):
        self.m_value = ''
        self.m_paths = []
        self.id = id
        self.wordMult = 1
        self.letterMult = 1
        self.isRoot = False

    def getPoints(self, l):
        points = 0
        if self.isRoot:
            return 0
        if l in ['A', 'E', 'I', 'N', 'R', 'S', 'T']:
            points = 1
        if l in ['C', 'L', 'M', 'O', 'U']:
            points = 2
        if l in ['D', 'P']:
            points = 3
        if l in ['B', 'F', 'G', 'H', 'V', 'Z']:
            points = 4
        if l in ['Q', 'Y']:
            points = 6
        if l in ['J', 'X']:
            points = 8
        if l in ['K', 'W']:
            points = 10
        if points == 0:
            raise Exception("Bad string")
        return points * self.letterMult

    def setValue(self, value):
       self.m_value = value

    def setBonus(self, bonus):
        if bonus == 'dl':
            self.letterMult = 2
        if bonus == 'tl':
            self.letterMult = 3
        if bonus == 'dw':
            self.wordMult = 2
        if bonus == 'tw':
            self.wordMult = 3

    def getValue(self):
        return self.m_value

    def addPath(self, cell):
        self.m_paths.append(cell)

    def match(self, params):
        idx = params['idx']
        word = params['word']
        l = ''
        if idx > -1:
            l = word[idx]
        # print('Word = ' + word + ' idx =' + str(idx) + " Is Root : " + str(self.isRoot) + " .  l = " + l + " .  v= " + self.getValue())
        if self.isRoot == False and l != self.getValue():
            return badResult()
        result = goodResult()
        if idx == len(word) - 1:
            path = createPath(self.id, self.getPoints(l), self.wordMult)
            result.paths.append(path)
            return result
        paths = []
        for cell in self.m_paths:
            params = {"word": word, "idx": idx+1 }
            res = cell.match(params)
            if res.isMatching == False:
                continue
            for path in res.paths:
                if self.id in path.path:
                    continue
                if self.isRoot == False:
                    updatePath(path, self.id, self.getPoints(l), self.wordMult)
                paths.append(path)
        if len(paths) == 0:
            return badResult()
        result.paths = paths
        return result
    
    def getDisplay(self):
        color = 'white'
        fmting = []
        if self.letterMult == 2:
            color = 'light_blue'
        if self.letterMult == 3:
            color = 'magenta'
        if self.wordMult == 2:
            color = 'red'
            fmting.append("bold")
        if self.wordMult == 3:
            color = 'yellow'
            fmting.append("bold")
        return colored(self.getValue(), color, attrs=fmting)