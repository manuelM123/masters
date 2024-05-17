from cut import *

def test_case_0():
	cut = calorie_intake_calc(206.69,221.77,8,'M',0.37,'M')

def test_case_1():
	cut = calorie_intake_calc(163.24,200.62,5,'N',0.49,'N')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'M'

def test_case_2():
	cut = calorie_intake_calc(207.51,141.51,43,'M',0.29,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'N'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'E'
	cut.gender = 'N'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_3():
	cut = calorie_intake_calc(155.62,210.02,7,'F',-0.09,'V')
	cut.bodyfat = 0.35
	cut.bodyfat = 0.11
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = -0.36
	cut.bodyfat = -0.11
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 95.61

def test_case_4():
	cut = calorie_intake_calc(199.22,200.91,31,'F',0.44,'S')
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 80.36
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 11
	cut.weight = 66.85
	cut.amount_exercise = 'M'
	cut.age = 61
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_5():
	cut = calorie_intake_calc(195.25,166.95,15,'N',-0.35,'V')
	cut.bodyfat = 0.43
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 9
	cut.age = 47
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'L'
	cut.amount_exercise = 'M'

