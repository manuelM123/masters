from cut import *

def test_case_0():
	cut = calorie_intake_calc(132.23,152.43,75,'M',0.14,'V')
	cut.age = 76
	cut.bodyfat = 0.02
	cut.bodyfat = -0.12
	cut.weight = 180.0
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_1():
	cut = calorie_intake_calc(49.11,160.34,31,'F',-0.41,'L')

def test_case_2():
	cut = calorie_intake_calc(176.24,208.73,11,'N',-0.33,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.05
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 182.82
	cut.weight = 169.55
	cut.gender = 'N'

def test_case_3():
	cut = calorie_intake_calc(140.35,213.09,33,'F',0.11,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_4():
	cut = calorie_intake_calc(121.85,170.99,68,'M',-0.45,'E')
	cut.bodyfat = -0.11
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 30
	cut.bodyfat = 0.66
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_5():
	cut = calorie_intake_calc(96.91,214.71,29,'M',0.38,'N')
	cut.gender = 'N'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'M'
	cut.gender = 'F'
	cut.gender = 'F'

