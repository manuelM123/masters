from cut import *

def test_case_0():
	cut = calorie_intake_calc(206.69,221.77,8,'M',0.37,'M')

def test_case_1():
	cut = calorie_intake_calc(65.39,213.47,58,'M',-0.32,'E')
	cut.amount_exercise = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 67
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 148.06
	cut.age = 57
	cut.amount_exercise = 'V'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'N'

