from cut import *

def test_case_0():
	cut = calorie_intake_calc(189.92,186.27,22,'F',0.29,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 196.34
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 198.34
	cut.weight = 84.72
	cut.gender = 'F'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_1():
	cut = calorie_intake_calc(42.81,170.23,15,'M',0.2,'V')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'N'
	cut.amount_exercise = 'L'
	cut.gender = 'F'
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 60

def test_case_2():
	cut = calorie_intake_calc(177.93,193.86,52,'N',0.27,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 29
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 164.22
	cut.bodyfat = 0.26
	cut.weight = 154.45
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_3():
	cut = calorie_intake_calc(193.22,220.55,21,'N',0.12,'L')
	cut.amount_exercise = 'N'
	cut.height = 148.05

def test_case_4():
	cut = calorie_intake_calc(49.71,183.18,25,'M',0.27,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'E'
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.07
	cut.weight = 177.58
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'F'

