from cut import *

def test_case_0():
	cut = calorie_intake_calc(53.75,200.81,37,'M',-0.38,'S')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 47
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_1():
	cut = calorie_intake_calc(167.2,200.59,52,'F',-0.06,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 7
	cut.amount_exercise = 'N'
	cut.amount_exercise = 'L'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'N'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 62

def test_case_2():
	cut = calorie_intake_calc(156.59,179.38,16,'M',0.55,'S')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.05

def test_case_3():
	cut = calorie_intake_calc(36.39,216.06,73,'F',-0.31,'L')
	cut.weight = 127.24
	cut.weight = 184.57
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'V'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

