from cut import *

def test_case_0():
	cut = calorie_intake_calc(102.96,154.63,62,'N',0.63,'S')
	cut.weight = 88.08
	cut.height = 219.78
	cut.height = 146.44

def test_case_1():
	cut = calorie_intake_calc(157.14,184.87,45,'N',0.8,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.12
	cut.height = 183.79
	cut.gender = 'N'
	cut.amount_exercise = 'N'
	cut.bodyfat = -0.48
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = -0.16

def test_case_2():
	cut = calorie_intake_calc(209.01,210.87,55,'M',0.61,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'
	cut.bodyfat = -0.14
	cut.gender = 'N'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 219.54
	cut.age = 59

def test_case_3():
	cut = calorie_intake_calc(49.26,171.55,76,'N',0.65,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = -0.47

def test_case_4():
	cut = calorie_intake_calc(156.74,165.97,23,'M',0.09,'V')
	cut.weight = 203.03
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'M'
	cut.amount_exercise = 'L'
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 198.42

def test_case_5():
	cut = calorie_intake_calc(84.81,190.84,60,'N',-0.45,'N')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 212.49
	cut.age = 80
	cut.bodyfat = 0.29
	cut.bodyfat = 0.32
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'N'
	cut.amount_exercise = 'V'

def test_case_6():
	cut = calorie_intake_calc(214.49,218.81,81,'F',0.24,'M')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.45
	cut.height = 141.67
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'F'
	cut.height = 149.21

def test_case_7():
	cut = calorie_intake_calc(51.39,180.22,61,'N',0.78,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_8():
	cut = calorie_intake_calc(194.39,188.18,33,'M',-0.47,'E')
	cut.amount_exercise = 'V'
	cut.amount_exercise = 'L'
	cut.bodyfat = -0.48
	cut.height = 184.42
	cut.weight = 51.16
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.58
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

