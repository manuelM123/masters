from cut import *

def test_case_0():
	cut = calorie_intake_calc(129.27,171.85,28,'N',-0.35,'E')
	cut.weight = 150.24
	cut.amount_exercise = 'S'
	cut.bodyfat = -0.08
	cut.weight = 187.35
	cut.amount_exercise = 'M'

def test_case_1():
	cut = calorie_intake_calc(74.62,204.43,65,'F',-0.32,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.69
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_2():
	cut = calorie_intake_calc(167.13,188.43,53,'F',-0.24,'L')
	cut.gender = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 165.29
	cut.age = 21
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 174.15
	cut.weight = 39.3

def test_case_3():
	cut = calorie_intake_calc(78.03,170.43,18,'M',0.05,'L')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 150.39
	cut.weight = 147.99
	cut.amount_exercise = 'N'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

