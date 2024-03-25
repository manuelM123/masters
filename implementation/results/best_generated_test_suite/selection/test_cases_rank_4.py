from cut import *

def test_case_0():
	cut = calorie_intake_calc(108.6,142.31,39,'N',0.16,'L')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.18
	cut.weight = 181.94
	cut.height = 207.56
	cut.amount_exercise = 'V'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.03

def test_case_1():
	cut = calorie_intake_calc(132.45,184.1,12,'N',0.07,'L')
	cut.age = 28
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'N'
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.18

def test_case_2():
	cut = calorie_intake_calc(158.63,183.5,81,'M',0.3,'E')
	cut.height = 183.93
	cut.bodyfat = 0.02
	cut.gender = 'N'
	cut.bodyfat = 0.24

def test_case_3():
	cut = calorie_intake_calc(58.44,216.29,62,'M',0.2,'M')
	cut.gender = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 213.31
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 166.19
	cut.height = 201.32
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_4():
	cut = calorie_intake_calc(65.84,172.97,65,'M',0.29,'S')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 67
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 75
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 203.1
	cut.weight = 176.57
	cut.height = 148.49

def test_case_5():
	cut = calorie_intake_calc(142.47,160.16,62,'M',0.13,'V')
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 138.41
	cut.amount_exercise = 'M'
	cut.height = 143.15
	cut.age = 72
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()

