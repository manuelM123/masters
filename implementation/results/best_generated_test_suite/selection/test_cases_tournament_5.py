from cut import *

def test_case_0():
	cut = calorie_intake_calc(98.42,178.14,34,'M',0.29,'N')
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.08
	cut.amount_exercise = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 78
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 162.35
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_1():
	cut = calorie_intake_calc(174.42,179.56,10,'F',0.05,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.28
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 201.6
	cut.age = 52
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 12

