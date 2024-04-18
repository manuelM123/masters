from cut import *

def test_case_0():
	cut = calorie_intake_calc(57.47,158.68,59,'M',0.24,'L')
	cut.amount_exercise = 'V'
	cut.bodyfat = 0.07
	cut.height = 178.14

def test_case_1():
	cut = calorie_intake_calc(182.84,147.31,67,'N',0.05,'S')

def test_case_2():
	cut = calorie_intake_calc(209.86,208.15,73,'M',0.02,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.22

