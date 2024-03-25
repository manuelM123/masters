from cut import *

def test_case_0():
	cut = calorie_intake_calc(157.19,195.73,12,'F',0.06,'N')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 177.01
	cut.height = 210.4
	cut.gender = 'N'
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(66.28,191.64,17,'M',0.03,'E')
	cut.height = 174.34
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.15
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_2():
	cut = calorie_intake_calc(109.99,140.33,34,'M',0.28,'N')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 166.61
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 175.52
	cut.height = 211.75
	cut.gender = 'M'
	cut.bodyfat = 0.04
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 182.68

def test_case_3():
	cut = calorie_intake_calc(124.86,168.28,19,'N',0.21,'M')
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_4():
	cut = calorie_intake_calc(55.21,187.48,47,'M',0.26,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 141.78
	result_determine_calorie_intake = cut.determine_calorie_intake()

