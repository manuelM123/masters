from cut import *

def test_case_0():
	cut = calorie_intake_calc(188.64,146.93,69,'F',0.18,'L')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'L'
	cut.weight = 133.72

def test_case_1():
	cut = calorie_intake_calc(148.49,150.79,66,'N',0.44,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.71
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_2():
	cut = calorie_intake_calc(204.4,205.91,25,'F',0.43,'L')
	cut.amount_exercise = 'E'
	cut.gender = 'M'
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 167.48
	cut.amount_exercise = 'V'
	result_tdee_calculation = cut.tdee_calculation()

def test_case_3():
	cut = calorie_intake_calc(197.63,188.28,52,'N',0.67,'E')
	cut.amount_exercise = 'V'
	cut.bodyfat = -0.48
	cut.weight = 43.94
	cut.height = 136.53

def test_case_4():
	cut = calorie_intake_calc(112.12,153.12,40,'M',-0.21,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 200.06
	cut.gender = 'N'
	cut.height = 168.32
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_5():
	cut = calorie_intake_calc(54.57,202.46,16,'N',-0.24,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'M'
	cut.age = 38
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 139.9

def test_case_6():
	cut = calorie_intake_calc(126.46,139.76,11,'N',0.17,'M')
	cut.gender = 'F'
	cut.age = 83

