from cut import *

def test_case_0():
	cut = calorie_intake_calc(155.88,158.76,76,'M',-0.08,'L')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.25
	cut.gender = 'F'

def test_case_1():
	cut = calorie_intake_calc(164.54,205.69,18,'F',0.57,'N')
	cut.bodyfat = 0.51

def test_case_2():
	cut = calorie_intake_calc(92.31,206.29,49,'F',0.02,'V')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 159.15
	cut.weight = 69.82

def test_case_3():
	cut = calorie_intake_calc(38.12,163.62,32,'M',-0.03,'L')
	cut.amount_exercise = 'L'
	cut.gender = 'F'
	result_determine_calorie_intake = cut.determine_calorie_intake()

