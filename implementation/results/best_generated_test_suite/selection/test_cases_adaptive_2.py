from cut import *

def test_case_0():
	cut = calorie_intake_calc(81.48,205.11,68,'F',0.2,'S')
	cut.height = 210.67
	cut.amount_exercise = 'E'
	cut.weight = 110.22
	cut.age = 44
	cut.gender = 'F'
	cut.amount_exercise = 'E'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 180.12
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_1():
	cut = calorie_intake_calc(159.08,201.86,46,'M',0.21,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.21
	cut.gender = 'N'
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'S'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.27
	cut.gender = 'M'

