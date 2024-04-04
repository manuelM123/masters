from cut import *

def test_case_0():
	cut = calorie_intake_calc(118.08,148.1,78,'M',0.25,'S')
	cut.gender = 'M'

def test_case_1():
	cut = calorie_intake_calc(171.55,189.24,62,'F',0.26,'N')
	cut.age = 14

def test_case_2():
	cut = calorie_intake_calc(199.85,204.6,55,'N',0.03,'V')
	cut.height = 210.31
	cut.amount_exercise = 'V'

def test_case_3():
	cut = calorie_intake_calc(50.34,188.56,49,'N',0.08,'N')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 73
	cut.bodyfat = 0.11

def test_case_4():
	cut = calorie_intake_calc(96.99,172.69,19,'F',0.29,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 218.14

