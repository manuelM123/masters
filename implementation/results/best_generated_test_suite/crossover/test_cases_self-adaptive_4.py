from cut import *

def test_case_0():
	cut = calorie_intake_calc(134.54,206.81,16,'N',0.19,'V')
	cut.height = 197.25
	cut.age = 21
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.17
	cut.bodyfat = 0.16
	cut.age = 47
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 205.11

def test_case_1():
	cut = calorie_intake_calc(73.85,147.14,31,'M',0.21,'S')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 190.05
	cut.amount_exercise = 'N'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 97.88
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_2():
	cut = calorie_intake_calc(166.68,195.47,41,'M',0.21,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'S'
	cut.weight = 100.47
	cut.height = 203.73
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'M'
	cut.height = 165.0

def test_case_3():
	cut = calorie_intake_calc(136.44,157.37,68,'F',0.05,'S')
	cut.age = 53
	cut.amount_exercise = 'E'
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 159.75
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 155.21
	cut.weight = 46.03

