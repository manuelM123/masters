from cut import *

def test_case_0():
	cut = calorie_intake_calc(160.37,204.2,26,'F',0.06,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 86.86

def test_case_1():
	cut = calorie_intake_calc(185.87,144.73,25,'M',0.07,'S')
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'L'
	cut.amount_exercise = 'E'
	result_tdee_calculation = cut.tdee_calculation()

def test_case_2():
	cut = calorie_intake_calc(208.7,152.01,35,'N',0.15,'L')

def test_case_3():
	cut = calorie_intake_calc(55.66,183.43,69,'M',0.27,'E')
	cut.gender = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

