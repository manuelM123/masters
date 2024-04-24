from cut import *

def test_case_0():
	cut = calorie_intake_calc(64.49,166.1,79,'F',0.22,'M')
	cut.bodyfat = 0.14
	cut.age = 29
	cut.amount_exercise = 'M'
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 44.61

def test_case_1():
	cut = calorie_intake_calc(198.96,208.52,31,'F',0.29,'M')
	cut.gender = 'N'
	cut.height = 198.51

def test_case_2():
	cut = calorie_intake_calc(48.11,147.21,81,'M',0.19,'N')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 66
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.0
	cut.amount_exercise = 'N'

def test_case_3():
	cut = calorie_intake_calc(125.81,165.41,67,'N',0.22,'M')
	cut.height = 174.28

def test_case_4():
	cut = calorie_intake_calc(199.53,161.63,22,'F',0.29,'L')
	cut.bodyfat = 0.28
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'L'
	cut.height = 174.79
	cut.age = 23
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 192.06
	cut.height = 190.6
	cut.weight = 200.8
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_5():
	cut = calorie_intake_calc(63.33,206.97,38,'M',0.15,'S')
	cut.weight = 186.31
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'N'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'N'
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 75
	cut.weight = 124.42

def test_case_6():
	cut = calorie_intake_calc(195.85,168.59,50,'M',0.16,'E')
	cut.age = 34
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 181.48
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 161.82
	cut.gender = 'F'
	cut.bodyfat = 0.21
	cut.height = 206.75
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 198.38

def test_case_7():
	cut = calorie_intake_calc(113.23,167.56,17,'M',0.21,'S')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_8():
	cut = calorie_intake_calc(87.54,193.93,57,'F',0.29,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 166.59
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.29
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 72
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 79
	cut.age = 59

