from cut import *

def test_case_0():
	cut = calorie_intake_calc(79.48,153.64,51,'M',0.07,'S')
	cut.amount_exercise = 'S'
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 56
	cut.amount_exercise = 'N'
	cut.height = 194.89
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 77.56

def test_case_1():
	cut = calorie_intake_calc(80.41,220.76,27,'M',0.27,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_2():
	cut = calorie_intake_calc(190.02,220.73,71,'M',0.02,'L')
	result_tdee_calculation = cut.tdee_calculation()

def test_case_3():
	cut = calorie_intake_calc(209.74,190.87,56,'M',0.01,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 208.16
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 152.97

def test_case_4():
	cut = calorie_intake_calc(173.44,141.36,38,'M',0.13,'S')
	cut.amount_exercise = 'N'

