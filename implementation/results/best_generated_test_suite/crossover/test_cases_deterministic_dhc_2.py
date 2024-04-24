from cut import *

def test_case_0():
	cut = calorie_intake_calc(115.6,170.95,13,'F',0.04,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.13
	cut.age = 30
	cut.height = 154.37
	cut.bodyfat = 0.29

def test_case_1():
	cut = calorie_intake_calc(206.22,176.77,30,'N',0.04,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'S'
	cut.height = 216.64
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 22

def test_case_2():
	cut = calorie_intake_calc(64.32,145.91,75,'F',0.04,'S')
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 165.83
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_3():
	cut = calorie_intake_calc(177.32,178.11,56,'F',0.18,'V')
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_4():
	cut = calorie_intake_calc(93.11,220.07,68,'F',0.03,'M')
	cut.age = 45
	cut.bodyfat = 0.1

def test_case_5():
	cut = calorie_intake_calc(75.18,151.63,38,'N',0.01,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_6():
	cut = calorie_intake_calc(81.79,196.07,41,'F',0.11,'N')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 164.94
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

