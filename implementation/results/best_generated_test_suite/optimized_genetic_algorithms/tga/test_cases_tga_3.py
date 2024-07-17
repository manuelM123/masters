from cut import *

def test_case_0():
	cut = calorie_intake_calc(158.93,153.16,60,'N',-0.08,'E')
	cut.bodyfat = 0.72
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 177.16
	result_tdee_calculation = cut.tdee_calculation()

def test_case_1():
	cut = calorie_intake_calc(111.42,170.3,69,'F',-0.03,'S')

def test_case_2():
	cut = calorie_intake_calc(162.28,191.11,13,'M',-0.08,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'F'

def test_case_3():
	cut = calorie_intake_calc(204.59,170.19,12,'F',0.13,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

