from cut import *

def test_case_0():
	cut = calorie_intake_calc(109.9,216.28,66,'M',-0.21,'V')

def test_case_1():
	cut = calorie_intake_calc(139.24,213.07,83,'N',0.41,'V')
	cut.gender = 'F'
	cut.age = 50
	cut.age = 42
	cut.amount_exercise = 'L'

def test_case_2():
	cut = calorie_intake_calc(80.78,174.86,69,'M',0.04,'E')
	cut.weight = 129.03
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = -0.5
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 185.12
	cut.age = 58
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_3():
	cut = calorie_intake_calc(87.85,169.56,33,'N',-0.23,'N')
	cut.age = 16
	cut.gender = 'F'
	cut.height = 137.94

def test_case_4():
	cut = calorie_intake_calc(75.55,211.49,29,'N',-0.09,'S')

