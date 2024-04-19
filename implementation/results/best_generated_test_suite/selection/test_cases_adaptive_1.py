from cut import *

def test_case_0():
	cut = calorie_intake_calc(206.21,156.85,29,'F',0.25,'S')
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.15
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'N'
	cut.amount_exercise = 'E'
	cut.weight = 77.3
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(92.39,196.71,73,'N',0.18,'S')
	cut.bodyfat = 0.25

def test_case_2():
	cut = calorie_intake_calc(66.0,179.67,12,'M',0.26,'M')
	cut.weight = 115.89
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 60
	result_tdee_calculation = cut.tdee_calculation()

def test_case_3():
	cut = calorie_intake_calc(87.39,211.1,41,'M',0.17,'L')
	cut.weight = 97.95
	cut.amount_exercise = 'E'
	cut.height = 176.26
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 154.93
	cut.bodyfat = 0.28
	cut.weight = 87.71

