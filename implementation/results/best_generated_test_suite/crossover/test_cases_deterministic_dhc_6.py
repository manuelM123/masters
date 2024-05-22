from cut import *

def test_case_0():
	cut = calorie_intake_calc(144.61,211.54,74,'F',0.24,'L')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'M'
	cut.age = 37
	cut.gender = 'F'

def test_case_1():
	cut = calorie_intake_calc(89.68,145.83,84,'F',-0.5,'L')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 34
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'N'
	cut.bodyfat = 0.38
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_2():
	cut = calorie_intake_calc(185.1,213.92,16,'F',-0.34,'V')
	cut.weight = 131.69
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

