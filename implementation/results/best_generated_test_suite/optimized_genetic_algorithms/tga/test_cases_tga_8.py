from cut import *

def test_case_0():
	cut = calorie_intake_calc(174.6,183.22,58,'F',0.13,'S')
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 56
	cut.bodyfat = 0.21

def test_case_1():
	cut = calorie_intake_calc(56.2,213.18,56,'M',0.08,'M')
	cut.amount_exercise = 'E'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(92.67,139.55,37,'N',0.42,'L')

def test_case_3():
	cut = calorie_intake_calc(133.45,195.08,76,'N',0.5,'L')

