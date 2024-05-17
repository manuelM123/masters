from cut import *

def test_case_0():
	cut = calorie_intake_calc(68.31,214.42,10,'M',0.01,'N')
	cut.gender = 'M'
	cut.bodyfat = 0.47
	cut.amount_exercise = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.66
	cut.bodyfat = 0.6
	result_determine_calorie_intake = cut.determine_calorie_intake()

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
	cut = calorie_intake_calc(190.63,194.3,11,'N',-0.28,'E')
	cut.height = 224.89

def test_case_3():
	cut = calorie_intake_calc(69.1,182.91,74,'M',0.77,'S')
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 224.82

def test_case_4():
	cut = calorie_intake_calc(96.22,144.66,13,'N',-0.29,'V')
	cut.amount_exercise = 'E'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 159.79
	cut.weight = 185.61
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 83.01
	cut.weight = 212.9

def test_case_5():
	cut = calorie_intake_calc(91.98,167.33,38,'M',0.25,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_6():
	cut = calorie_intake_calc(163.89,160.04,81,'N',0.36,'E')
	cut.age = 80
	cut.weight = 154.12
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 15
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 192.23
	cut.weight = 171.67
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 207.32

