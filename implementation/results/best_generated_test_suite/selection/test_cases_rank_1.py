from cut import *

def test_case_0():
	cut = calorie_intake_calc(64.49,166.1,79,'F',0.22,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'N'
	cut.amount_exercise = 'L'
	cut.height = 170.0
	cut.weight = 44.61

def test_case_1():
	cut = calorie_intake_calc(188.66,207.17,41,'M',0.17,'E')
	cut.height = 162.86
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 163.17
	cut.age = 75
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.13
	cut.weight = 90.39
	cut.bodyfat = 0.29
	result_tdee_calculation = cut.tdee_calculation()

def test_case_2():
	cut = calorie_intake_calc(48.11,147.21,81,'M',0.19,'N')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.17
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.0
	cut.amount_exercise = 'N'

def test_case_3():
	cut = calorie_intake_calc(70.12,220.23,76,'F',0.05,'M')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 79
	cut.gender = 'N'

def test_case_4():
	cut = calorie_intake_calc(60.62,168.91,72,'N',0.27,'M')
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 40
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 144.82
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_5():
	cut = calorie_intake_calc(63.33,206.97,38,'M',0.15,'S')
	cut.weight = 186.31
	cut.age = 23
	cut.amount_exercise = 'N'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'N'
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 75
	cut.weight = 124.42

def test_case_6():
	cut = calorie_intake_calc(147.3,156.19,41,'M',0.14,'L')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 44.57
	cut.bodyfat = 0.3
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'M'
	cut.weight = 159.6
	cut.weight = 103.9

def test_case_7():
	cut = calorie_intake_calc(143.07,193.18,75,'M',0.25,'S')
	cut.bodyfat = 0.16
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.11

def test_case_8():
	cut = calorie_intake_calc(93.29,151.95,79,'N',0.22,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'F'
	cut.height = 180.86
	cut.bodyfat = 0.21

