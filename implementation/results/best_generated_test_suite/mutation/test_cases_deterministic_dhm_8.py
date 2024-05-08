from cut import *

def test_case_0():
	cut = calorie_intake_calc(198.82,178.68,10,'N',0.3,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'F'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 154.84
	cut.age = 59

def test_case_1():
	cut = calorie_intake_calc(152.44,213.63,24,'N',0.09,'S')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = -0.42
	cut.age = 39
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 165.3
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'M'
	cut.weight = 122.64

def test_case_2():
	cut = calorie_intake_calc(150.54,181.79,48,'M',0.25,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'E'
	cut.weight = 205.22
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = -0.12
	cut.age = 15
	cut.amount_exercise = 'M'

def test_case_3():
	cut = calorie_intake_calc(83.67,211.26,57,'N',0.16,'E')
	cut.bodyfat = -0.03

def test_case_4():
	cut = calorie_intake_calc(181.72,136.81,7,'N',0.78,'S')
	cut.height = 141.57
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 139.77
	cut.gender = 'N'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 71.88
	cut.gender = 'N'
	cut.height = 213.8
	result_tdee_calculation = cut.tdee_calculation()

def test_case_5():
	cut = calorie_intake_calc(193.92,141.05,48,'N',0.16,'L')
	cut.age = 51
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 25
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.52
	cut.height = 222.81
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.76

def test_case_6():
	cut = calorie_intake_calc(58.68,157.66,44,'F',0.23,'L')
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.28
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 191.97

def test_case_7():
	cut = calorie_intake_calc(140.1,150.83,69,'F',0.42,'N')
	cut.bodyfat = -0.47
	cut.weight = 124.7
	cut.height = 156.06
	cut.gender = 'F'
	cut.amount_exercise = 'M'
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 144.91
	cut.amount_exercise = 'V'
	cut.height = 194.2

