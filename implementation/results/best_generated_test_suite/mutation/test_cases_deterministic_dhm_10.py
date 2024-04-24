from cut import *

def test_case_0():
	cut = calorie_intake_calc(174.12,151.09,70,'F',0.18,'N')
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.11
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.22
	cut.height = 141.44
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'M'
	cut.weight = 71.36
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_1():
	cut = calorie_intake_calc(56.71,140.01,40,'F',0.23,'S')
	cut.height = 153.13
	cut.weight = 182.41
	cut.weight = 77.64
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_2():
	cut = calorie_intake_calc(169.4,188.01,45,'F',0.17,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 166.2
	cut.height = 178.21
	cut.height = 218.71

def test_case_3():
	cut = calorie_intake_calc(139.2,201.85,72,'M',0.04,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 148.9
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'N'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

