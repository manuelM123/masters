from cut import *

def test_case_0():
	cut = calorie_intake_calc(183.98,216.94,20,'M',-0.24,'M')
	cut.bodyfat = -0.41
	cut.height = 169.6
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 77.31
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(135.24,177.66,52,'F',-0.3,'S')
	cut.amount_exercise = 'N'
	cut.height = 164.64
	cut.amount_exercise = 'L'
	cut.amount_exercise = 'V'
	cut.weight = 194.58

def test_case_2():
	cut = calorie_intake_calc(174.61,189.45,85,'F',-0.18,'M')
	cut.age = 75
	cut.weight = 39.42

def test_case_3():
	cut = calorie_intake_calc(116.96,195.02,26,'F',0.62,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_4():
	cut = calorie_intake_calc(52.78,197.41,20,'N',0.62,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.77
	cut.amount_exercise = 'E'
	cut.amount_exercise = 'M'
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_5():
	cut = calorie_intake_calc(35.55,165.53,47,'N',0.8,'S')

def test_case_6():
	cut = calorie_intake_calc(43.0,135.13,55,'N',-0.45,'N')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 166.79
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_7():
	cut = calorie_intake_calc(141.88,135.13,8,'N',0.13,'N')
	cut.height = 202.71
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 137.13
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_8():
	cut = calorie_intake_calc(182.89,205.31,33,'F',0.16,'V')
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 64.91
	cut.height = 202.14
	cut.amount_exercise = 'M'
	cut.weight = 183.94
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'F'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.49

