from cut import *

def test_case_0():
	cut = calorie_intake_calc(60.94,208.97,67,'M',0.2,'M')
	cut.gender = 'M'
	cut.weight = 161.35

def test_case_1():
	cut = calorie_intake_calc(137.92,185.68,13,'F',0.02,'E')
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 184.3
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 205.7
	cut.weight = 210.82
	cut.gender = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.03
	cut.gender = 'N'
	cut.amount_exercise = 'E'

def test_case_2():
	cut = calorie_intake_calc(67.28,189.52,14,'N',0.22,'E')
	cut.bodyfat = 0.09
	cut.gender = 'M'
	cut.age = 76
	cut.gender = 'F'
	result_tdee_calculation = cut.tdee_calculation()

