from cut import *

def test_case_0():
	cut = calorie_intake_calc(128.67,154.59,68,'M',0.11,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(130.89,218.22,19,'M',0.15,'M')
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 66
	cut.age = 56
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 150.66
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 104.3

def test_case_2():
	cut = calorie_intake_calc(134.15,140.96,37,'N',0.26,'V')
	cut.bodyfat = 0.18
	cut.age = 73
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 207.19
	cut.height = 159.87
	cut.height = 155.41

def test_case_3():
	cut = calorie_intake_calc(113.56,170.71,60,'F',0.06,'V')
	cut.weight = 134.85
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'E'
	cut.weight = 194.75
	cut.weight = 47.54
	cut.age = 70
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_4():
	cut = calorie_intake_calc(84.18,206.06,24,'N',0.05,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()

