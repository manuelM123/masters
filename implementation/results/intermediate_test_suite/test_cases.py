from cut import *

def test_case_0():
	cut = calorie_intake_calc(122.91,194.79,68,'N',0.21,'M')

def test_case_1():
	cut = calorie_intake_calc(134.46,170.22,42,'M',0.06,'V')
	cut.bodyfat = 0.12
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.21

def test_case_2():
	cut = calorie_intake_calc(146.5,204.87,66,'N',0.01,'E')
	cut.weight = 147.19
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 172.41

def test_case_3():
	cut = calorie_intake_calc(46.87,211.71,13,'F',0.29,'L')
	cut.amount_exercise = 'M'

def test_case_4():
	cut = calorie_intake_calc(101.61,218.09,40,'F',0.16,'S')
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

