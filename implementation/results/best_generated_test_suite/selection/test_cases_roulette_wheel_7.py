from cut import *

def test_case_0():
	cut = calorie_intake_calc(210.89,199.49,41,'N',0.26,'M')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 208.58
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_1():
	cut = calorie_intake_calc(182.61,203.51,57,'F',0.14,'V')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_2():
	cut = calorie_intake_calc(145.82,210.41,65,'F',0.22,'S')
	cut.weight = 46.77
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 212.5
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'N'

def test_case_3():
	cut = calorie_intake_calc(125.81,165.41,67,'N',0.22,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

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
	cut = calorie_intake_calc(46.21,152.99,43,'F',0.18,'S')
	cut.bodyfat = 0.26

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
	cut = calorie_intake_calc(130.39,174.3,52,'F',0.07,'L')
	cut.weight = 134.74
	cut.weight = 131.78
	cut.height = 199.7

def test_case_9():
	cut = calorie_intake_calc(162.27,142.28,26,'N',0.01,'M')
	cut.gender = 'N'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 187.41
	cut.amount_exercise = 'L'
	cut.height = 206.32
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 206.49
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 199.19

