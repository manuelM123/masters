from cut import *

def test_case_0():
	cut = calorie_intake_calc(172.17,167.05,48,'N',-0.28,'M')
	cut.amount_exercise = 'M'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 77
	cut.height = 208.12
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_1():
	cut = calorie_intake_calc(152.5,210.23,29,'M',0.04,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 56
	cut.age = 66
	cut.amount_exercise = 'E'

def test_case_2():
	cut = calorie_intake_calc(116.97,147.31,6,'M',-0.23,'M')
	cut.height = 156.92
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 216.72
	cut.height = 221.66
	cut.bodyfat = 0.09
	cut.weight = 169.78
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = -0.17

def test_case_3():
	cut = calorie_intake_calc(142.69,199.84,73,'N',0.45,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 7
	cut.gender = 'N'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'F'
	cut.age = 69
	result_tdee_calculation = cut.tdee_calculation()

def test_case_4():
	cut = calorie_intake_calc(57.65,168.38,56,'N',-0.44,'L')
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 83
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'M'
	cut.gender = 'N'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'F'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 53.75

def test_case_5():
	cut = calorie_intake_calc(166.2,139.69,68,'M',0.65,'E')
	cut.gender = 'N'
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'F'
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_6():
	cut = calorie_intake_calc(153.61,201.03,67,'M',0.14,'M')
	cut.height = 162.49
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 71
	cut.bodyfat = -0.44
	cut.weight = 180.11
	cut.amount_exercise = 'M'
	cut.age = 64

def test_case_7():
	cut = calorie_intake_calc(193.12,220.49,78,'F',0.63,'L')
	cut.age = 31
	cut.gender = 'M'
	result_tdee_calculation = cut.tdee_calculation()

