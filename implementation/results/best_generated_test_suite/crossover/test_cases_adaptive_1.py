from cut import *

def test_case_0():
	cut = calorie_intake_calc(142.02,170.87,18,'M',0.21,'M')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 190.67
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 62
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(79.71,140.18,22,'N',0.16,'N')
	cut.weight = 148.46
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 55
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'M'

def test_case_2():
	cut = calorie_intake_calc(98.72,177.53,38,'F',0.1,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_3():
	cut = calorie_intake_calc(40.24,186.11,10,'M',0.0,'E')
	cut.weight = 199.83
	cut.height = 156.34
	result_tdee_calculation = cut.tdee_calculation()

