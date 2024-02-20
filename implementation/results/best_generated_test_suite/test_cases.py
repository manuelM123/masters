from cut import *

def test_case_0():
	cut = calorie_intake_calc(181.45,175.57,30,'M',0.05,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 86.96
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(67.39,217.24,16,'N',0.17,'S')
	result_tdee_calculation = cut.tdee_calculation()

def test_case_2():
	cut = calorie_intake_calc(131.14,175.38,66,'M',0.11,'L')

def test_case_3():
	cut = calorie_intake_calc(146.5,204.87,66,'N',0.01,'E')
	cut.weight = 147.19
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 172.41

def test_case_4():
	cut = calorie_intake_calc(46.87,211.71,13,'F',0.29,'L')
	cut.amount_exercise = 'M'

def test_case_5():
	cut = calorie_intake_calc(203.18,167.95,78,'F',0.27,'E')
	cut.age = 53
	cut.amount_exercise = 'L'

def test_case_6():
	cut = calorie_intake_calc(203.18,167.95,78,'F',0.27,'E')
	cut.age = 53
	cut.amount_exercise = 'L'

