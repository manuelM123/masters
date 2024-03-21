from cut import *

def test_case_0():
	cut = calorie_intake_calc(125.22,204.04,40,'F',0.22,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 109.07

def test_case_1():
	cut = calorie_intake_calc(66.89,191.99,53,'F',0.17,'S')

def test_case_2():
	cut = calorie_intake_calc(171.65,168.23,37,'M',0.19,'S')
	cut.gender = 'M'
	cut.weight = 118.17
	cut.gender = 'N'

