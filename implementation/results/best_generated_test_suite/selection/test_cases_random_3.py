from cut import *

def test_case_0():
	cut = calorie_intake_calc(51.63,152.43,70,'N',0.06,'N')
	cut.bodyfat = 0.08

def test_case_1():
	cut = calorie_intake_calc(194.63,203.42,63,'M',0.05,'L')
	cut.weight = 70.67
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.05
	cut.gender = 'M'
	cut.bodyfat = 0.13
	cut.height = 209.23
	cut.height = 155.03
	cut.gender = 'M'

def test_case_2():
	cut = calorie_intake_calc(47.86,144.22,67,'F',0.04,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.25

def test_case_3():
	cut = calorie_intake_calc(54.88,215.94,77,'F',0.06,'E')
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'F'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_4():
	cut = calorie_intake_calc(172.59,173.63,54,'N',0.07,'V')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

