from cut import *

def test_case_0():
	cut = calorie_intake_calc(214.94,171.57,68,'N',0.2,'L')
	cut.bodyfat = -0.2
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.4
	cut.amount_exercise = 'M'
	cut.amount_exercise = 'E'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 156.55
	cut.bodyfat = 0.08
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

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
	cut = calorie_intake_calc(96.63,185.74,33,'F',0.5,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'F'
	cut.gender = 'N'
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 160.69
	cut.gender = 'N'
	cut.height = 175.37
	cut.weight = 162.31
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_5():
	cut = calorie_intake_calc(200.14,179.39,61,'N',-0.18,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 47

def test_case_6():
	cut = calorie_intake_calc(74.64,164.54,15,'F',-0.18,'S')
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'M'
	cut.gender = 'F'
	cut.bodyfat = -0.01
	cut.amount_exercise = 'N'
	cut.height = 159.26
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

