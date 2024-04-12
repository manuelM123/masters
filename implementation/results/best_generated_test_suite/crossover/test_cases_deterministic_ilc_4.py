from cut import *

def test_case_0():
	cut = calorie_intake_calc(190.8,142.09,68,'N',0.23,'S')
	cut.amount_exercise = 'E'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.09
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.2
	cut.height = 172.87

def test_case_1():
	cut = calorie_intake_calc(201.93,218.42,81,'F',0.14,'S')

def test_case_2():
	cut = calorie_intake_calc(121.96,158.08,22,'N',0.29,'N')
	cut.amount_exercise = 'V'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 155.22
	cut.amount_exercise = 'M'
	cut.amount_exercise = 'E'
	cut.bodyfat = 0.2
	cut.amount_exercise = 'S'
	cut.height = 215.62
	cut.age = 30
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_3():
	cut = calorie_intake_calc(47.89,161.71,18,'F',0.08,'N')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_4():
	cut = calorie_intake_calc(195.96,205.46,54,'M',0.03,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'L'

