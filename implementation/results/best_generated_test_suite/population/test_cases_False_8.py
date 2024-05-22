from cut import *

def test_case_0():
	cut = calorie_intake_calc(157.46,150.27,18,'M',0.11,'E')
	cut.age = 22
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 138.97

def test_case_1():
	cut = calorie_intake_calc(195.96,207.74,34,'F',0.57,'M')
	cut.gender = 'M'
	cut.bodyfat = 0.75
	cut.weight = 141.69

def test_case_2():
	cut = calorie_intake_calc(98.65,137.23,42,'F',0.16,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.03
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.44

def test_case_3():
	cut = calorie_intake_calc(68.08,212.83,38,'N',-0.12,'L')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.6

def test_case_4():
	cut = calorie_intake_calc(162.21,189.51,79,'N',0.18,'V')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 43
	cut.gender = 'N'
	cut.age = 37
	cut.age = 39

def test_case_5():
	cut = calorie_intake_calc(171.95,141.93,77,'N',0.67,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'
	cut.age = 46
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'L'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 16
	cut.age = 20
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_6():
	cut = calorie_intake_calc(79.47,154.78,64,'M',-0.29,'V')
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'N'

