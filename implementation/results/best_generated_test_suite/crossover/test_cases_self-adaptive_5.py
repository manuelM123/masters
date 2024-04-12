from cut import *

def test_case_0():
	cut = calorie_intake_calc(205.14,154.11,47,'M',0.21,'L')
	cut.gender = 'F'
	cut.weight = 89.16
	cut.age = 26
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'F'
	cut.age = 16
	cut.amount_exercise = 'N'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_1():
	cut = calorie_intake_calc(210.08,218.04,79,'F',0.15,'S')
	cut.height = 171.34
	cut.amount_exercise = 'S'
	cut.weight = 178.81
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'S'
	cut.height = 203.47
	cut.height = 198.59
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_2():
	cut = calorie_intake_calc(94.24,207.5,12,'M',0.0,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'M'
	cut.bodyfat = 0.15
	cut.weight = 41.0
	cut.bodyfat = 0.07
	cut.weight = 68.19
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_3():
	cut = calorie_intake_calc(87.68,206.43,60,'F',0.15,'V')
	cut.height = 207.72
	cut.amount_exercise = 'S'
	cut.height = 205.36
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.29
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_4():
	cut = calorie_intake_calc(141.97,200.49,50,'M',0.23,'E')
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 41
	cut.amount_exercise = 'N'
	cut.gender = 'F'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

