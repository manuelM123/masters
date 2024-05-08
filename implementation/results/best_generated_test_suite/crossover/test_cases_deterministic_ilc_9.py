from cut import *

def test_case_0():
	cut = calorie_intake_calc(109.9,216.28,66,'M',-0.21,'V')

def test_case_1():
	cut = calorie_intake_calc(60.11,175.5,11,'F',0.01,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = -0.45
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 141.18
	cut.bodyfat = 0.48
	cut.gender = 'F'
	cut.weight = 187.73

def test_case_2():
	cut = calorie_intake_calc(80.78,174.86,69,'M',0.04,'E')
	cut.weight = 129.03
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = -0.5
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 185.12
	cut.age = 58
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_3():
	cut = calorie_intake_calc(141.37,143.27,81,'F',0.69,'E')

def test_case_4():
	cut = calorie_intake_calc(56.42,164.32,21,'N',-0.4,'E')
	cut.amount_exercise = 'N'
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.17
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'E'
	cut.gender = 'M'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_5():
	cut = calorie_intake_calc(200.14,179.39,61,'N',-0.18,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 47

def test_case_6():
	cut = calorie_intake_calc(142.58,179.57,62,'M',-0.19,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 191.17
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 171.48
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_7():
	cut = calorie_intake_calc(159.21,172.18,84,'F',0.01,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.31
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 73
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'N'

def test_case_8():
	cut = calorie_intake_calc(126.52,184.05,78,'F',0.46,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 71
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_9():
	cut = calorie_intake_calc(44.47,165.7,81,'N',0.37,'L')

