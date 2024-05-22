from cut import *

def test_case_0():
	cut = calorie_intake_calc(58.62,210.22,30,'M',0.72,'N')
	cut.weight = 150.24
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = -0.08
	cut.weight = 187.35
	cut.age = 73

def test_case_1():
	cut = calorie_intake_calc(74.62,204.43,65,'F',-0.32,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.71
	cut.height = 148.44

def test_case_2():
	cut = calorie_intake_calc(53.58,150.37,83,'M',-0.16,'N')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 150.63

def test_case_3():
	cut = calorie_intake_calc(197.63,188.28,52,'N',0.67,'E')
	cut.amount_exercise = 'V'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 43.94
	cut.height = 136.53

def test_case_4():
	cut = calorie_intake_calc(158.14,195.72,66,'M',-0.33,'S')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_5():
	cut = calorie_intake_calc(171.95,141.93,77,'N',0.67,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'L'
	cut.amount_exercise = 'M'
	cut.age = 67
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 200.04
	cut.gender = 'F'

def test_case_6():
	cut = calorie_intake_calc(207.23,167.75,50,'F',0.19,'V')
	cut.gender = 'F'
	result_tdee_calculation = cut.tdee_calculation()

