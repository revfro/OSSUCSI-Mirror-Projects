import unittest

class Movie:
	def __init__(self, title, budget, year):
		self.title=title
		self.budget=budget
		self.year=year

# Movie is Movie(String,Natural,Natural)
# interp. a movie with title, budget in USD, and year released

M1 = Movie("Titanic", 32498332, 1998)
M2 = Movie("Avengers Endgame", 67864438564, 2019)
M3 = Movie("Passion: Resurrection", 67864438564, 2023)
# 
# def fnForMovie(m):
# 	...m.title
# 	...m.budget
# 	...m.year
	
# Design a function that tells the title of the latest released of the two movies
# Movie,Movie->Str
# Determine which of two movies was most recently released

#def latestRelease(m1, m2):		#stub
#	return ""

def latestRelease(m1,m2):
	if m1.year > m2.year:
		return m1.title
	else:
		return m2.title

# testing

class LatestReleaseTest(unittest.TestCase):
    def testFirst(self):
        self.assertEqual(latestRelease(M1, M2), M2.title)
    def testSecond(self):
        self.assertEqual(latestRelease(Movie("",123,1901),Movie("a",123,1902)), "a")
    def testThird(self):
        self.assertEqual(latestRelease(M1, M3), M3.title)
    def testFourth(self):
        self.assertEqual(latestRelease(M2, M3), M3.title)

if __name__ == '__main__':
	unittest.main()

