from cut import *

def test_case_0():
	cut = calorie_intake_calc(158.58,193.28,66,'M',0.04,'V')
	cut.amount_exercise = 'V'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 52
	cut.gender = 'N'

def test_case_1():
	cut = calorie_intake_calc(94.44,153.51,28,'M',0.05,'N')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'L'

def test_case_2():
	cut = calorie_intake_calc(102.05,154.06,23,'M',0.2,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_3():
	cut = calorie_intake_calc(124.71,190.75,16,'M',0.28,'S')
	cut.gender = 'M'
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.26
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'M'

