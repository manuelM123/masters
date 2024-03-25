from cut import *

def test_case_0():
	cut = calorie_intake_calc(83.86,181.79,17,'F',0.24,'L')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 64.54
	cut.amount_exercise = 'M'
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'V'
	cut.gender = 'F'
	cut.amount_exercise = 'E'

def test_case_1():
	cut = calorie_intake_calc(188.13,158.11,28,'N',0.07,'V')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'F'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 81
	cut.height = 220.12
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'

def test_case_2():
	cut = calorie_intake_calc(133.2,213.46,51,'N',0.21,'L')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'M'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'N'
	cut.gender = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 28

