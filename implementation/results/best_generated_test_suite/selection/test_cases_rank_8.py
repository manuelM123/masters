from cut import *

def test_case_0():
	cut = calorie_intake_calc(149.83,144.41,65,'F',0.04,'M')
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 212.85
	cut.weight = 155.59

def test_case_1():
	cut = calorie_intake_calc(182.61,203.51,57,'F',0.14,'V')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_2():
	cut = calorie_intake_calc(147.98,209.82,16,'F',0.09,'N')
	cut.bodyfat = 0.15
	cut.bodyfat = 0.07
	cut.height = 140.08
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 10
	cut.amount_exercise = 'E'
	cut.weight = 194.95
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_3():
	cut = calorie_intake_calc(125.81,165.41,67,'N',0.22,'M')
	cut.height = 174.28

def test_case_4():
	cut = calorie_intake_calc(199.53,161.63,22,'F',0.29,'L')
	cut.weight = 51.27
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'L'
	cut.height = 174.79
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 192.06
	cut.height = 190.6
	cut.age = 33
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_5():
	cut = calorie_intake_calc(98.7,192.92,16,'F',0.22,'L')

def test_case_6():
	cut = calorie_intake_calc(70.58,156.97,20,'F',0.12,'E')
	cut.height = 196.09
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'F'
	cut.gender = 'M'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'F'
	cut.height = 206.76
	result_determine_calorie_intake = cut.determine_calorie_intake()

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

