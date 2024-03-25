from cut import *

def test_case_0():
	cut = calorie_intake_calc(89.13,175.88,81,'N',0.06,'L')
	cut.bodyfat = 0.02
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 78.2
	cut.weight = 154.34
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_1():
	cut = calorie_intake_calc(137.47,213.77,48,'F',0.05,'V')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 169.22
	result_tdee_calculation = cut.tdee_calculation()

def test_case_2():
	cut = calorie_intake_calc(56.15,191.41,10,'M',0.28,'L')
	cut.amount_exercise = 'M'
	cut.bodyfat = 0.11
	cut.bodyfat = 0.09
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'E'
	cut.height = 178.84
	cut.height = 189.36
	cut.age = 17
	cut.weight = 130.97
	result_determine_calorie_intake = cut.determine_calorie_intake()

