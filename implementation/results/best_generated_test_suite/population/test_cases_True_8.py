from cut import *

def test_case_0():
	cut = calorie_intake_calc(155.05,151.28,14,'N',0.22,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'M'
	cut.height = 190.69
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 48
	cut.age = 32

def test_case_1():
	cut = calorie_intake_calc(120.86,186.0,73,'F',0.05,'M')

def test_case_2():
	cut = calorie_intake_calc(89.61,163.14,81,'M',0.09,'N')
	cut.amount_exercise = 'E'
	cut.height = 189.73
	cut.height = 153.88
	cut.amount_exercise = 'L'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 148.56
	cut.weight = 145.32
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 45.66

def test_case_3():
	cut = calorie_intake_calc(66.45,169.48,11,'M',0.3,'V')
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 200.71
	cut.gender = 'M'
	cut.weight = 162.82
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'V'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 217.67
	cut.bodyfat = 0.29

def test_case_4():
	cut = calorie_intake_calc(95.43,190.96,46,'F',0.05,'L')
	cut.bodyfat = 0.13
	cut.gender = 'F'
	cut.weight = 138.63
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 166.27
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 209.62
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_5():
	cut = calorie_intake_calc(133.43,208.82,46,'M',0.29,'E')
	cut.height = 219.82
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 28
	cut.amount_exercise = 'V'

def test_case_6():
	cut = calorie_intake_calc(123.21,207.2,64,'F',0.11,'N')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 10
	cut.amount_exercise = 'N'
	cut.weight = 102.59
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_7():
	cut = calorie_intake_calc(66.72,160.35,23,'M',0.03,'V')
	cut.amount_exercise = 'L'
	cut.gender = 'F'

