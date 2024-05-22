from cut import *

def test_case_0():
	cut = calorie_intake_calc(201.11,156.81,45,'F',-0.44,'V')
	cut.gender = 'M'
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'M'
	cut.amount_exercise = 'V'
	cut.age = 53
	cut.bodyfat = 0.16
	cut.height = 203.46

def test_case_1():
	cut = calorie_intake_calc(190.89,151.44,67,'M',-0.11,'V')
	cut.weight = 132.94
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'L'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'M'
	cut.weight = 67.37
	cut.height = 179.33
	cut.height = 220.83
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 99.03

def test_case_2():
	cut = calorie_intake_calc(71.93,170.24,73,'M',0.01,'E')
	cut.bodyfat = 0.28
	cut.height = 146.14
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 37
	cut.amount_exercise = 'S'
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_3():
	cut = calorie_intake_calc(127.8,158.1,78,'F',0.51,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'S'
	cut.amount_exercise = 'M'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 21
	result_determine_calorie_intake = cut.determine_calorie_intake()

