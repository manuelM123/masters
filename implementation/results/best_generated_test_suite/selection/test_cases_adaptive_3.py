from cut import *

def test_case_0():
	cut = calorie_intake_calc(202.35,201.47,39,'M',0.18,'V')
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'E'
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'M'
	cut.gender = 'F'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'F'

def test_case_1():
	cut = calorie_intake_calc(148.72,159.54,38,'M',0.22,'L')
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'F'
	cut.bodyfat = 0.23
	cut.weight = 197.02
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'F'
	cut.age = 59
	cut.bodyfat = 0.24

def test_case_2():
	cut = calorie_intake_calc(43.52,205.5,28,'M',0.01,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'
	cut.weight = 52.11

