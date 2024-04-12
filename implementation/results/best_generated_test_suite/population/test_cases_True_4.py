from cut import *

def test_case_0():
	cut = calorie_intake_calc(127.68,157.18,45,'F',0.11,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.2
	cut.gender = 'N'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 189.93

def test_case_1():
	cut = calorie_intake_calc(138.14,213.85,68,'F',0.3,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(205.26,187.35,15,'N',0.27,'V')
	cut.amount_exercise = 'V'
	cut.age = 47
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.13
	cut.gender = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.29
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 77.72

def test_case_3():
	cut = calorie_intake_calc(185.77,182.43,27,'M',0.19,'M')
	cut.bodyfat = 0.12
	cut.weight = 43.87
	cut.bodyfat = 0.15
	cut.height = 175.13
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

