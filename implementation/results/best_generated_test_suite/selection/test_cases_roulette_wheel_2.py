from cut import *

def test_case_0():
	cut = calorie_intake_calc(86.58,199.82,61,'M',-0.25,'E')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 21
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'F'
	cut.bodyfat = 0.46
	cut.height = 139.19
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'F'

def test_case_1():
	cut = calorie_intake_calc(167.72,173.6,8,'F',0.48,'M')
	cut.gender = 'F'
	cut.age = 76
	cut.height = 212.97
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(108.33,163.25,57,'F',-0.35,'V')
	result_tdee_calculation = cut.tdee_calculation()

def test_case_3():
	cut = calorie_intake_calc(163.85,176.43,18,'M',0.3,'N')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 183.02
	cut.bodyfat = -0.28
	cut.weight = 189.97
	cut.gender = 'F'
	cut.age = 38
	cut.gender = 'F'

def test_case_4():
	cut = calorie_intake_calc(101.54,221.35,70,'F',0.36,'V')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'V'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'F'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_5():
	cut = calorie_intake_calc(108.36,198.38,59,'N',0.43,'L')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 155.8
	cut.amount_exercise = 'L'
	cut.weight = 125.56

def test_case_6():
	cut = calorie_intake_calc(100.49,176.27,26,'F',0.61,'L')
	result_tdee_calculation = cut.tdee_calculation()

