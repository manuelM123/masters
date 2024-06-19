from cut import *

def test_case_0():
	cut = calorie_intake_calc(40.29,163.24,85,'M',-0.28,'V')
	cut.gender = 'N'
	cut.weight = 156.91

def test_case_1():
	cut = calorie_intake_calc(206.7,140.22,64,'F',0.26,'S')
	cut.weight = 138.65
	cut.weight = 156.21

