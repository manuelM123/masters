from cut import *

def test_case_0():
	cut = calorie_intake_calc(120.87,178.68,56,'F',-0.08,'L')
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'F'
	cut.age = 74
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_1():
	cut = calorie_intake_calc(90.18,135.86,34,'M',0.16,'V')
	cut.age = 36
	result_tdee_calculation = cut.tdee_calculation()

def test_case_2():
	cut = calorie_intake_calc(94.41,155.64,16,'F',-0.19,'S')
	cut.amount_exercise = 'E'
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 53
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 208.43
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 160.81
	cut.weight = 140.16

def test_case_3():
	cut = calorie_intake_calc(197.5,223.3,56,'M',0.46,'V')
	cut.amount_exercise = 'L'
	cut.age = 65
	cut.age = 5
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'V'
	cut.gender = 'M'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_4():
	cut = calorie_intake_calc(172.34,152.26,21,'F',0.3,'N')

def test_case_5():
	cut = calorie_intake_calc(206.4,174.74,85,'F',0.77,'S')
	cut.height = 152.58

def test_case_6():
	cut = calorie_intake_calc(81.53,156.97,84,'F',0.79,'N')
	cut.age = 69
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 141.02
	cut.weight = 101.01
	cut.age = 43

def test_case_7():
	cut = calorie_intake_calc(109.59,209.48,44,'M',-0.15,'V')
	cut.bodyfat = -0.42
	cut.height = 193.61
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.05
	cut.age = 53
	cut.age = 85
	cut.age = 41
	cut.gender = 'F'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_8():
	cut = calorie_intake_calc(184.64,169.3,6,'N',0.71,'S')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

