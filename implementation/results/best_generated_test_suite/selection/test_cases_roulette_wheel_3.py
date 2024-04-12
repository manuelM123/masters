from cut import *

def test_case_0():
	cut = calorie_intake_calc(108.52,170.06,75,'M',0.2,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 69.33
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 201.57
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(68.95,150.23,55,'F',0.06,'E')
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 175.57
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 47
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_2():
	cut = calorie_intake_calc(79.37,217.64,19,'F',0.21,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.02
	cut.height = 162.65
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 105.79
	cut.bodyfat = 0.12

