from cut import *

def test_case_0():
	cut = calorie_intake_calc(78.82,213.42,12,'F',0.07,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(110.27,217.4,81,'M',-0.33,'V')
	cut.gender = 'N'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_2():
	cut = calorie_intake_calc(79.05,200.95,12,'M',0.77,'E')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 174.86
	cut.height = 198.8
	cut.weight = 199.95
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 50
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'L'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_3():
	cut = calorie_intake_calc(155.28,157.68,20,'M',-0.46,'V')
	cut.weight = 79.83
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 176.37
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 198.19
	cut.amount_exercise = 'N'
	cut.weight = 206.15

