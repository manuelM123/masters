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
	cut = calorie_intake_calc(55.05,154.88,49,'M',0.24,'E')
	cut.bodyfat = 0.01
	cut.amount_exercise = 'V'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'

def test_case_3():
	cut = calorie_intake_calc(82.29,189.71,20,'N',0.27,'V')
	cut.weight = 163.02
	cut.amount_exercise = 'S'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.19
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.21
	cut.weight = 101.99

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
	cut = calorie_intake_calc(182.38,140.57,16,'N',0.04,'M')
	cut.bodyfat = 0.06
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'E'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'S'
	cut.amount_exercise = 'S'
	cut.weight = 66.01

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
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
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
	cut = calorie_intake_calc(156.31,169.61,61,'F',0.02,'S')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.01
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 204.8
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'M'
	cut.amount_exercise = 'M'
	cut.weight = 191.09
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 128.65

