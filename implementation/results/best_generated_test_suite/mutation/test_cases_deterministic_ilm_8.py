from cut import *

def test_case_0():
	cut = calorie_intake_calc(115.23,158.09,84,'M',-0.34,'E')
	cut.gender = 'F'
	cut.age = 30
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'N'

def test_case_1():
	cut = calorie_intake_calc(186.65,210.95,50,'M',0.3,'V')
	cut.age = 67
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 69.58
	cut.amount_exercise = 'E'
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 58
	cut.amount_exercise = 'N'

