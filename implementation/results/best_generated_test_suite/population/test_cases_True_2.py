from cut import *

def test_case_0():
	cut = calorie_intake_calc(169.96,194.49,60,'M',-0.14,'M')
	cut.height = 168.96
	cut.height = 204.04
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 184.2
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 208.94
	cut.amount_exercise = 'E'
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(167.61,175.62,5,'N',-0.42,'N')
	cut.amount_exercise = 'N'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = -0.48
	cut.amount_exercise = 'M'
	cut.amount_exercise = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'V'

def test_case_2():
	cut = calorie_intake_calc(127.7,155.58,24,'M',0.56,'M')

def test_case_3():
	cut = calorie_intake_calc(66.03,165.19,52,'F',0.11,'L')
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 43
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'N'
	result_tdee_calculation = cut.tdee_calculation()

def test_case_4():
	cut = calorie_intake_calc(113.85,143.08,65,'F',0.3,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_5():
	cut = calorie_intake_calc(143.92,193.02,43,'M',0.37,'E')
	cut.amount_exercise = 'S'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = -0.1

def test_case_6():
	cut = calorie_intake_calc(193.9,204.2,75,'M',-0.15,'S')

def test_case_7():
	cut = calorie_intake_calc(63.75,195.9,31,'F',0.41,'V')
	cut.height = 152.72
	cut.weight = 61.8
	cut.amount_exercise = 'N'
	cut.amount_exercise = 'V'
	cut.age = 13
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_8():
	cut = calorie_intake_calc(116.14,137.96,56,'N',-0.4,'L')
	cut.amount_exercise = 'S'
	cut.age = 68
	cut.height = 147.86
	cut.amount_exercise = 'V'
	cut.height = 212.24
	cut.bodyfat = -0.44
	cut.bodyfat = 0.28
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.47
	cut.gender = 'M'

