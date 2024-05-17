from cut import *

def test_case_0():
	cut = calorie_intake_calc(124.31,164.21,30,'M',0.21,'S')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 8

def test_case_1():
	cut = calorie_intake_calc(49.85,145.6,74,'M',-0.04,'S')
	cut.age = 20
	cut.gender = 'M'
	result_tdee_calculation = cut.tdee_calculation()

def test_case_2():
	cut = calorie_intake_calc(63.93,135.3,66,'M',0.0,'V')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 35.54
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.31

def test_case_3():
	cut = calorie_intake_calc(69.84,163.35,43,'F',-0.16,'E')
	cut.age = 27
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 160.82
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 168.97
	cut.amount_exercise = 'S'

def test_case_4():
	cut = calorie_intake_calc(56.68,145.41,54,'M',-0.14,'M')
	cut.gender = 'F'
	cut.weight = 93.05
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'M'

