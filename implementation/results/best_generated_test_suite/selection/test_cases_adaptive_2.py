from cut import *

def test_case_0():
	cut = calorie_intake_calc(110.68,165.6,23,'F',0.09,'E')
	cut.weight = 154.55
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(83.69,160.53,81,'N',0.2,'M')
	cut.age = 43
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(184.38,178.78,71,'M',0.05,'L')
	cut.height = 201.55
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'V'
	cut.gender = 'F'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 185.32
	cut.gender = 'M'
	cut.age = 66
	cut.age = 80
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_3():
	cut = calorie_intake_calc(135.45,208.5,18,'N',0.01,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_4():
	cut = calorie_intake_calc(206.06,214.71,76,'F',0.25,'E')
	cut.gender = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 34
	cut.gender = 'F'
	cut.age = 13
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.23
	cut.gender = 'N'
	cut.weight = 130.7

