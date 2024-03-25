from cut import *

def test_case_0():
	cut = calorie_intake_calc(163.36,195.45,79,'M',0.0,'V')

def test_case_1():
	cut = calorie_intake_calc(117.51,178.89,60,'M',0.2,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'N'
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 68.22
	cut.age = 40
	cut.amount_exercise = 'L'
	result_tdee_calculation = cut.tdee_calculation()

def test_case_2():
	cut = calorie_intake_calc(92.44,212.55,14,'M',0.19,'V')
	cut.height = 190.82
	cut.amount_exercise = 'N'
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.07

def test_case_3():
	cut = calorie_intake_calc(157.47,154.07,49,'M',0.27,'E')
	cut.gender = 'F'
	cut.height = 199.69
	cut.height = 209.53
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'F'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

