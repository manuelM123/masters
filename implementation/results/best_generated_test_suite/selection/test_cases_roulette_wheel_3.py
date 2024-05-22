from cut import *

def test_case_0():
	cut = calorie_intake_calc(45.48,156.24,35,'M',-0.48,'S')
	cut.height = 145.37
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 50.0
	cut.age = 29
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'F'
	cut.weight = 38.82
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_1():
	cut = calorie_intake_calc(160.49,198.26,81,'M',-0.16,'S')
	cut.weight = 93.38

def test_case_2():
	cut = calorie_intake_calc(89.14,207.06,10,'F',0.06,'V')
	cut.age = 24
	cut.amount_exercise = 'E'
	cut.age = 39
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'N'
	cut.age = 58

def test_case_3():
	cut = calorie_intake_calc(43.86,155.68,40,'M',0.6,'V')
	cut.age = 31
	cut.height = 143.3
	cut.bodyfat = -0.16
	cut.weight = 72.67
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 23
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.08
	cut.gender = 'M'

