from cut import *

def test_case_0():
	cut = calorie_intake_calc(144.77,165.97,54,'F',0.22,'M')
	cut.weight = 49.19
	cut.gender = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'E'
	cut.weight = 155.23
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(136.6,181.44,62,'M',0.27,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 30
	cut.amount_exercise = 'M'
	cut.bodyfat = 0.07
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_2():
	cut = calorie_intake_calc(127.57,172.87,45,'N',0.22,'L')
	cut.gender = 'N'
	cut.height = 144.6
	cut.weight = 119.23
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

