#!python3.10
import unittest
import Automate
import Game

class TestStringMethods(unittest.TestCase):
    def testDisplay(self):
        automate = Automate.Automate()
        automate.setGrid("ABCDEFGHIJKLMNOP")
        automate.setBonus({"3": "tl","8": "dl","10": "dl","12": "dw", "5": "tw"})
        print('')
        automate.displayGrid()

    def test(self):
        automate = Automate.Automate()
        automate.setGrid("ABCDEFGHIJKLMNOP")
        res = automate.findWordPath("A")
        self.assertEqual(res.isMatching, True)
        res = automate.findWordPath("W")
        self.assertEqual(res.isMatching, False)
        res = automate.findWordPath("ABCD")
        self.assertEqual(res.isMatching, True)
        res = automate.findWordPath("ABCDZ")
        self.assertEqual(res.isMatching, False)
        res = automate.findWordPath("AFKP")
        self.assertEqual(res.isMatching, True)
        res = automate.findWordPath("AC")
        self.assertEqual(res.isMatching, False)
        res = automate.findWordPath("PKFA")
        self.assertEqual(res.isMatching, True)
        res = automate.findWordPath("ABA")
        self.assertEqual(res.isMatching, False)

    def testPath(self):
        automate = Automate.Automate()
        automate.setGrid("ABCDEFGHIJKLMNOP")
        res = automate.findWordPath("A")
        for path in res.paths:
            print(str(path.path))
        self.assertEqual(['0'], res.paths[0].path)
        res = automate.findWordPath("ABCD")
        self.assertEqual(['0', '1', '2', '3'], res.paths[0].path)
        res = automate.findWordPath("PKFA")
        self.assertEqual(['15', '10', '5', '0'], res.paths[0].path)

    def testPoints(self):
        automate = Automate.Automate()
        automate.setGrid("ABCDEFGHIJKLMNOP")
        res = automate.findWordPath("ABC")
        self.assertEqual(7, res.points)
        

    def testPoints(self):
        automate = Automate.Automate()
        automate.setGrid("ABCDEFGHIJKLMNOP")
        automate.setBonus({"3": "tl","8": "dl","10": "dl"})
        res = automate.findWordPath("ABCDHGFEIJK")
        # 1 + 4 + 2 + 3 * 3 + 1 + 4 + 4 + 4 + 1 * 2 + 8 + 10 * 2 = 59
        self.assertEqual(70, res.paths[0].getPoints())
    
    def testPoints_wm(self):
        automate = Automate.Automate()
        automate.setGrid("ABCDEFGHIJKLMNOP")
        automate.setBonus({"0": "dw", "5": "tw", "3": "tl","8": "dl","10": "dl"})
        res = automate.findWordPath("ABCDHGFEIJK")
        # 1 + 4 + 2 + 3 * 3 + 1 + 4 + 4 + 4 + 1 * 2 + 8 + 10 * 2 = 59 * 2 * 3 = 354
        self.assertEqual(365, res.paths[0].getPoints())

    def test_bestResult(self):
        automate = Automate.Automate()
        automate.setGrid("ZAAAAAAAAAAAAWAA")
        automate.setBonus({"0": "dl", "5": "tw", "8": "tl","12": 'dl'})
        res = automate.findBestWordPath("ZAAAW")
        self.assertEqual(['0', '5', '8', '12', '13'], res.path)


    def testRound(self):
        words = [
                        "PEU",
                        "PURGE",
                        "SURS",
                        "PU",
                        "LEGS",
                        "EMEUS",
                        "MEUS",
                        "SEMEUR",
                        "GUE",
                        "PILE",
                        "RUES",
                        "LIEGE",
                        "LIEGES",
                        "URGE",
                        "PURGEAMES",
                        "SEMAS",
                        "LIEGEAS",
                        "SUE",
                        "PESE",
                        "SUD",
                        "PURS",
                        "IL",
                        "GUS",
                        "GUR",
                        "PILEUSE",
                        "PESA",
                        "KEA",
                        "LIEUSE",
                        "EPURGE",
                        "DUPES",
                        "SESAME",
                        "GEL",
                        "KEAS",
                        "SUS",
                        "SUR",
                        "RUSAMES",
                        "AS",
                        "ILES",
                        "LEGE",
                        "PILEURS",
                        "IPES",
                        "SEL",
                        "LIEURS",
                        "MELS",
                        "PLIE",
                        "GUES",
                        "PLEURS",
                        "MAS",
                        "SEP",
                        "SES",
                        "SEMA",
                        "SAME",
                        "PURGEA",
                        "PIES",
                        "BD",
                        "RU",
                        "SEME",
                        "PIEU",
                        "SA",
                        "SE",
                        "LEGES",
                        "ASE",
                        "LIEUR",
                        "PUES",
                        "LIEUS",
                        "DRUPE",
                        "KG",
                        "PURGEAS",
                        "RUPE",
                        "PLIEUR",
                        "SU",
                        "USA",
                        "RUE",
                        "PILS",
                        "USE",
                        "DUPE",
                        "SLIP",
                        "LIE",
                        "PIE",
                        "SEMEURS",
                        "LIEGEA",
                        "USUELS",
                        "RUS",
                        "LEURS",
                        "PEUR",
                        "EMEU",
                        "LE",
                        "LI",
                        "ASES",
                        "SELS",
                        "PURGES",
                        "ILE",
                        "DG",
                        "DRU",
                        "PLIEUSE",
                        "ILEUS",
                        "USUEL",
                        "DRUS",
                        "SPI",
                        "PIEGEAS",
                        "GURS",
                        "GURU",
                        "MESUSA",
                        "ILS",
                        "DRUES",
                        "DU",
                        "MESUSE",
                        "MA",
                        "ME",
                        "AME",
                        "GRUE",
                        "USUS",
                        "SEMES",
                        "EME",
                        "US",
                        "PIEGEA",
                        "ML",
                        "EUS",
                        "DRUPES",
                        "LESA",
                        "SLIPS",
                        "LESE",
                        "URGES",
                        "PLEUR",
                        "ES",
                        "EU",
                        "PLIES",
                        "URGEA",
                        "DURS",
                        "RUSES",
                        "MEL",
                        "SUES",
                        "MES",
                        "DRUE",
                        "DUELS",
                        "SURSEME",
                        "MESA",
                        "PIEGE",
                        "USAMES",
                        "GELS",
                        "AMES",
                        "PEURS",
                        "EPURGES",
                        "LIES",
                        "URDU",
                        "PLI",
                        "SURSEMA",
                        "LIEU",
                        "PIEUSE",
                        "GURUS",
                        "DUE",
                        "DUEL",
                        "URUS",
                        "DUES",
                        "DUR",
                        "PIEGES",
                        "PUE",
                        "DUS",
                        "MEURS",
                        "PILEUR",
                        "PILES",
                        "USES",
                        "PUR",
                        "PUS",
                        "SUPE",
                        "LEI",
                        "RUSE",
                        "SEPS",
                        "LEUS",
                        "LEUR",
                        "LEM",
                        "PLIEURS",
                        "RUSA",
                        "GRUES",
                        "PI",
                        "LES",
                        "LEMS",
                        "LEU",
                        "IPE",
                        "EPI"
                    ]
        bonus = {"3": "tl", "8": "dl", "10": "dl" }
        round = Game.Round()
        round.setGrid("USPIRUELDGSMBKEA")
        round.setBonus(bonus)
        print('')
        round.automate.displayGrid()
        print('')
        results = round.findWordPath(words)     
        for path in results:
            print(path.word + " " + str(path.getPoints()) + " pts " + str(path.path))
        
# A B C D
# E F G H
# I J K L
# M N O P

if __name__ == '__main__':
    unittest.main()