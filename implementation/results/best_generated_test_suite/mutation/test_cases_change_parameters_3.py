from cut import *

def test_case_0():
	cut = calorie_intake_calc(170.15,166.14,51,'M',0.15,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 191.61
	cut.weight = 179.12
	cut.bodyfat = 0.23

def test_case_1():
	cut = calorie_intake_calc(105.78,166.26,25,'M',0.24,'V')
	cut.bodyfat = 0.05
	cut.age = 63
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 29
	cut.amount_exercise = 'S'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 199.29
	cut.height = 184.08

def test_case_2():
	cut = calorie_intake_calc(123.76,177.79,34,'M',0.21,'V')
	cut.height = 157.99
	cut.gender = 'F'
	cut.age = 79
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

