from cut import *

def test_case_0():
	cut = calorie_intake_calc(125.35,209.35,63,'M',-0.15,'S')
	cut.bodyfat = -0.12
	cut.age = 40
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_1():
	cut = calorie_intake_calc(129.6,139.21,19,'M',0.27,'L')

def test_case_2():
	cut = calorie_intake_calc(86.08,149.26,36,'F',0.2,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'N'

