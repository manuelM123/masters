from cut import *

def test_case_0():
	cut = calorie_intake_calc(96.19,213.33,46,'M',0.28,'V')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'N'
	cut.age = 32
	cut.age = 25
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'E'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_1():
	cut = calorie_intake_calc(102.26,184.14,57,'M',0.13,'E')
	cut.weight = 201.93
	cut.weight = 84.71
	cut.height = 146.07
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

