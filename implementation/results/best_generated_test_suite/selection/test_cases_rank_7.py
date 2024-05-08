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
	cut.height = 151.46
	cut.gender = 'F'

def test_case_1():
	cut = calorie_intake_calc(140.02,173.98,81,'N',0.34,'S')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.49
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 20
	cut.bodyfat = 0.68
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.28

def test_case_2():
	cut = calorie_intake_calc(108.33,163.25,57,'F',-0.35,'V')
	result_tdee_calculation = cut.tdee_calculation()

def test_case_3():
	cut = calorie_intake_calc(163.85,176.43,18,'M',0.3,'N')
	cut.weight = 74.92
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
	cut = calorie_intake_calc(108.29,213.19,46,'F',0.25,'N')
	cut.gender = 'N'
	cut.weight = 117.68
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'M'

def test_case_6():
	cut = calorie_intake_calc(121.11,200.08,63,'N',-0.48,'L')
	cut.height = 149.26
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 66
	cut.amount_exercise = 'N'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.18
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'L'

