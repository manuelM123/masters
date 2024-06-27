from cut import *

def test_case_0():
	cut = calorie_intake_calc(140.82,154.7,48,'F',-0.27,'E')
	cut.age = 18
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_1():
	cut = calorie_intake_calc(184.55,180.03,68,'M',0.15,'S')
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'L'
	cut.bodyfat = -0.3
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_2():
	cut = calorie_intake_calc(88.26,189.55,31,'N',0.42,'L')
	cut.age = 76

