from cut import *

def test_case_0():
	cut = calorie_intake_calc(169.07,197.8,16,'M',0.21,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'M'

def test_case_1():
	cut = calorie_intake_calc(137.89,165.36,45,'F',0.03,'M')
	cut.gender = 'M'
	cut.age = 28

def test_case_2():
	cut = calorie_intake_calc(107.29,182.46,45,'N',0.12,'E')
	cut.weight = 192.74
	cut.gender = 'N'
	cut.age = 40

