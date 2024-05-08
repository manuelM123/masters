from cut import *

def test_case_0():
	cut = calorie_intake_calc(178.1,212.25,33,'M',0.03,'M')
	cut.amount_exercise = 'L'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'F'
	result_tdee_calculation = cut.tdee_calculation()

def test_case_1():
	cut = calorie_intake_calc(168.14,159.18,34,'F',-0.21,'V')
	cut.weight = 149.36
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 156.84
	cut.height = 194.72
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_2():
	cut = calorie_intake_calc(191.63,153.78,7,'F',-0.41,'E')

def test_case_3():
	cut = calorie_intake_calc(108.77,174.13,33,'N',-0.04,'L')
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'V'
	cut.weight = 176.73
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = -0.34

def test_case_4():
	cut = calorie_intake_calc(170.62,148.41,41,'F',-0.29,'V')
	cut.bodyfat = 0.76

def test_case_5():
	cut = calorie_intake_calc(75.34,173.98,13,'F',-0.09,'E')
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 204.8
	cut.gender = 'N'
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 136.08
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'F'

def test_case_6():
	cut = calorie_intake_calc(183.37,177.4,57,'F',-0.46,'S')
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'N'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = -0.16

def test_case_7():
	cut = calorie_intake_calc(114.27,195.96,83,'F',0.73,'M')
	cut.gender = 'F'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_8():
	cut = calorie_intake_calc(137.06,151.01,76,'M',-0.46,'N')
	cut.bodyfat = 0.32
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'E'
	cut.bodyfat = 0.48
	cut.gender = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 49

def test_case_9():
	cut = calorie_intake_calc(67.56,204.68,61,'F',-0.23,'N')
	cut.bodyfat = -0.41
	result_tdee_calculation = cut.tdee_calculation()

