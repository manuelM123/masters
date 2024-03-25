from cut import *

def test_case_0():
	cut = calorie_intake_calc(184.38,214.42,23,'F',0.13,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.07

def test_case_1():
	cut = calorie_intake_calc(159.58,145.5,42,'F',0.3,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'E'
	cut.amount_exercise = 'L'

def test_case_2():
	cut = calorie_intake_calc(192.0,146.13,60,'M',0.28,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_3():
	cut = calorie_intake_calc(91.28,217.51,14,'F',0.21,'V')
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 184.7
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_4():
	cut = calorie_intake_calc(188.93,206.74,80,'F',0.27,'M')
	cut.gender = 'N'
	cut.gender = 'N'
	cut.amount_exercise = 'V'

