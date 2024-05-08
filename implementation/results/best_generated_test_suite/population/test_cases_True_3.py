from cut import *

def test_case_0():
	cut = calorie_intake_calc(43.72,194.04,70,'F',-0.32,'E')
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'M'
	cut.bodyfat = -0.42
	cut.gender = 'F'
	cut.age = 62
	cut.gender = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 16

def test_case_1():
	cut = calorie_intake_calc(116.72,159.79,85,'N',0.27,'L')
	cut.weight = 137.08

def test_case_2():
	cut = calorie_intake_calc(107.53,167.12,55,'M',-0.31,'N')
	cut.weight = 93.48
	cut.height = 180.06
	cut.gender = 'M'
	cut.amount_exercise = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'

def test_case_3():
	cut = calorie_intake_calc(179.14,223.24,48,'M',0.3,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'V'
	cut.bodyfat = -0.07
	cut.height = 196.56
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 204.01
	cut.amount_exercise = 'S'
	cut.weight = 76.48
	cut.weight = 194.47
	cut.age = 21

def test_case_4():
	cut = calorie_intake_calc(199.37,193.54,49,'F',0.12,'L')
	cut.bodyfat = 0.09
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'V'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 149.63
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'S'
	cut.weight = 44.99

def test_case_5():
	cut = calorie_intake_calc(202.75,145.46,64,'N',0.52,'L')
	cut.weight = 179.83
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 215.61
	cut.bodyfat = 0.38
	cut.gender = 'M'
	cut.gender = 'N'

def test_case_6():
	cut = calorie_intake_calc(180.82,207.8,5,'F',-0.03,'E')
	cut.gender = 'F'
	cut.weight = 140.76
	cut.age = 71

def test_case_7():
	cut = calorie_intake_calc(103.83,211.88,26,'N',-0.27,'L')
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 23
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 17

def test_case_8():
	cut = calorie_intake_calc(125.8,165.12,65,'F',0.52,'E')
	cut.gender = 'F'

