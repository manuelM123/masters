from cut import *

def test_case_0():
	cut = calorie_intake_calc(114.79,204.03,66,'N',0.41,'N')

def test_case_1():
	cut = calorie_intake_calc(96.3,201.97,26,'M',0.14,'L')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_2():
	cut = calorie_intake_calc(84.74,141.73,75,'N',-0.02,'S')
	cut.bodyfat = 0.13

def test_case_3():
	cut = calorie_intake_calc(76.03,178.78,19,'F',-0.35,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 126.8
	cut.amount_exercise = 'N'

def test_case_4():
	cut = calorie_intake_calc(194.13,213.35,81,'N',0.54,'E')
	cut.age = 33
	cut.age = 14

