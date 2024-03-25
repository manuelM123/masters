from cut import *

def test_case_0():
	cut = calorie_intake_calc(48.85,203.44,81,'M',0.25,'V')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.28

def test_case_1():
	cut = calorie_intake_calc(44.39,146.8,39,'N',0.19,'L')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_2():
	cut = calorie_intake_calc(77.78,172.24,71,'M',0.19,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 181.42
	cut.amount_exercise = 'E'
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'E'
	result_determine_calorie_intake = cut.determine_calorie_intake()

