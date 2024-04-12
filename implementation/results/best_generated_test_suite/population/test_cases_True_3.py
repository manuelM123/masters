from cut import *

def test_case_0():
	cut = calorie_intake_calc(127.34,207.5,23,'F',0.08,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'F'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 33
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 150.18
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.09

def test_case_1():
	cut = calorie_intake_calc(164.21,190.9,42,'M',0.2,'N')
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 17
	cut.weight = 204.19
	cut.bodyfat = 0.05
	cut.height = 169.84
	cut.amount_exercise = 'M'

def test_case_2():
	cut = calorie_intake_calc(84.19,141.44,15,'M',0.22,'L')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'M'

def test_case_3():
	cut = calorie_intake_calc(58.01,205.45,67,'M',0.03,'V')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 176.23

def test_case_4():
	cut = calorie_intake_calc(57.35,213.2,57,'M',0.21,'E')
	cut.age = 59
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 31
	cut.height = 217.92
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'N'

