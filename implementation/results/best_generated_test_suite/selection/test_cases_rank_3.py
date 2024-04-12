from cut import *

def test_case_0():
	cut = calorie_intake_calc(128.64,143.55,52,'F',0.21,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 62

def test_case_1():
	cut = calorie_intake_calc(172.6,190.27,59,'N',0.11,'M')
	cut.height = 166.75
	cut.bodyfat = 0.26
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 84.0
	cut.weight = 67.58
	cut.bodyfat = 0.19
	cut.gender = 'N'

def test_case_2():
	cut = calorie_intake_calc(147.29,150.02,80,'F',0.17,'E')
	cut.height = 181.27
	cut.amount_exercise = 'E'
	cut.weight = 92.75
	cut.age = 66
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'S'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_3():
	cut = calorie_intake_calc(132.67,167.05,62,'M',0.19,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 62
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'F'
	cut.gender = 'N'
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_4():
	cut = calorie_intake_calc(207.2,144.67,12,'M',0.22,'M')
	cut.gender = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'M'

