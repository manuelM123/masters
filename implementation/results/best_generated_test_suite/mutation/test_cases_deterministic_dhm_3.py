from cut import *

def test_case_0():
	cut = calorie_intake_calc(129.86,160.35,37,'F',0.17,'M')
	cut.gender = 'N'
	cut.gender = 'F'
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_1():
	cut = calorie_intake_calc(86.74,171.69,17,'F',0.11,'V')
	cut.bodyfat = 0.77
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'N'
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(88.74,181.01,69,'F',0.64,'N')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 215.99
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_3():
	cut = calorie_intake_calc(74.1,172.31,82,'N',-0.15,'M')

def test_case_4():
	cut = calorie_intake_calc(78.18,152.04,19,'M',-0.4,'M')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 148.13
	cut.amount_exercise = 'L'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.2
	result_tdee_calculation = cut.tdee_calculation()

