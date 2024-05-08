from cut import *

def test_case_0():
	cut = calorie_intake_calc(163.3,218.67,47,'N',-0.04,'N')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 65.19
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 78
	cut.amount_exercise = 'E'
	cut.age = 68

def test_case_1():
	cut = calorie_intake_calc(147.75,220.88,43,'F',0.05,'M')

def test_case_2():
	cut = calorie_intake_calc(185.87,173.33,51,'M',-0.34,'M')
	cut.weight = 115.15
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 155.93
	cut.gender = 'M'
	cut.bodyfat = 0.03
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'M'

def test_case_3():
	cut = calorie_intake_calc(44.48,164.49,34,'F',0.28,'V')
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 39
	cut.height = 210.03
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'F'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 157.01
	cut.weight = 174.69
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

