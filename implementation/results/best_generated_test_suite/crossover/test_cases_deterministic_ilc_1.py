from cut import *

def test_case_0():
	cut = calorie_intake_calc(67.26,141.13,39,'N',0.08,'M')

def test_case_1():
	cut = calorie_intake_calc(80.21,156.23,77,'F',0.02,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 32

