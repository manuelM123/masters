from cut import *

def test_case_0():
	cut = calorie_intake_calc(189.15,141.87,63,'M',0.06,'S')
	result_tdee_calculation = cut.tdee_calculation()

def test_case_1():
	cut = calorie_intake_calc(139.11,180.21,26,'N',0.17,'N')

def test_case_2():
	cut = calorie_intake_calc(131.32,166.75,43,'F',0.03,'E')
	cut.gender = 'F'
	result_determine_calorie_intake = cut.determine_calorie_intake()

