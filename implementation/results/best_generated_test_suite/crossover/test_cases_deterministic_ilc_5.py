from cut import *

def test_case_0():
	cut = calorie_intake_calc(174.94,182.44,50,'F',0.25,'M')
	cut.bodyfat = 0.26
	cut.bodyfat = -0.32
	cut.age = 16
	cut.gender = 'N'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'L'
	cut.amount_exercise = 'V'
	cut.weight = 54.3
	cut.bodyfat = 0.16
	cut.bodyfat = -0.35

def test_case_1():
	cut = calorie_intake_calc(178.94,156.1,79,'M',0.39,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'S'
	cut.bodyfat = 0.15

def test_case_2():
	cut = calorie_intake_calc(184.34,144.5,5,'N',-0.08,'S')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.57
	cut.bodyfat = 0.16
	cut.height = 203.78
	cut.amount_exercise = 'M'

def test_case_3():
	cut = calorie_intake_calc(87.83,191.06,27,'M',0.01,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'M'
	cut.gender = 'M'
	cut.bodyfat = -0.27
	cut.age = 20
	cut.bodyfat = 0.43
	cut.bodyfat = 0.02

def test_case_4():
	cut = calorie_intake_calc(38.02,184.64,32,'M',0.78,'N')
	cut.amount_exercise = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'E'
	cut.age = 65

def test_case_5():
	cut = calorie_intake_calc(79.82,186.59,57,'F',0.2,'S')
	cut.height = 224.32
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'L'
	cut.amount_exercise = 'M'
	cut.bodyfat = -0.04
	cut.age = 29
	cut.weight = 200.04
	cut.weight = 192.95

