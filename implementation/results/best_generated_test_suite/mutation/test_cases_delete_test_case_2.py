from cut import *

def test_case_0():
	cut = calorie_intake_calc(146.4,186.8,59,'N',0.14,'V')
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 146.94

def test_case_1():
	cut = calorie_intake_calc(141.59,187.45,29,'M',0.2,'L')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'M'
	cut.weight = 143.71
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(93.59,188.59,75,'M',0.02,'V')
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 35
	cut.gender = 'F'
	cut.bodyfat = 0.03
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 216.57
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 141.16
	cut.height = 145.47
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_3():
	cut = calorie_intake_calc(191.15,173.08,62,'N',0.3,'S')
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 85.6
	cut.age = 75
	result_determine_calorie_intake = cut.determine_calorie_intake()

