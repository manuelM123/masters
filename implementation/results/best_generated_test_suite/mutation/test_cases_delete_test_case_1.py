from cut import *

def test_case_0():
	cut = calorie_intake_calc(107.41,159.46,69,'N',0.21,'N')
	cut.weight = 195.68
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'M'

def test_case_1():
	cut = calorie_intake_calc(85.6,182.1,20,'N',0.06,'N')
	cut.height = 143.97
	cut.gender = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 45

def test_case_2():
	cut = calorie_intake_calc(92.06,162.73,30,'M',0.14,'S')

