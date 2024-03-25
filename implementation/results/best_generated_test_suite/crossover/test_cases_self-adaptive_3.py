from cut import *

def test_case_0():
	cut = calorie_intake_calc(78.01,205.24,52,'M',0.22,'N')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.18
	cut.bodyfat = 0.01
	cut.height = 140.67
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.27
	result_tdee_calculation = cut.tdee_calculation()

def test_case_1():
	cut = calorie_intake_calc(165.92,201.86,80,'M',0.24,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'M'

def test_case_2():
	cut = calorie_intake_calc(108.55,220.95,48,'F',0.12,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 194.01
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'V'
	cut.amount_exercise = 'N'
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'V'
	cut.gender = 'N'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

