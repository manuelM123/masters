from cut import *

def test_case_0():
	cut = calorie_intake_calc(77.39,186.93,31,'M',0.29,'V')

def test_case_1():
	cut = calorie_intake_calc(77.85,143.88,10,'F',0.18,'L')
	cut.gender = 'M'
	cut.height = 210.96
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 55
	cut.age = 65

def test_case_2():
	cut = calorie_intake_calc(147.18,146.9,49,'F',0.22,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 184.31
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 208.23
	cut.amount_exercise = 'N'
	cut.gender = 'F'

def test_case_3():
	cut = calorie_intake_calc(170.7,157.07,52,'F',0.22,'L')
	cut.height = 174.55
	cut.gender = 'M'
	cut.age = 73
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 36
	cut.age = 31

def test_case_4():
	cut = calorie_intake_calc(66.26,176.82,15,'F',0.23,'S')
	cut.height = 168.61
	cut.weight = 54.12
	cut.weight = 60.11
	cut.height = 206.73
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 11
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'S'

