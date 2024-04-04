from cut import *

def test_case_0():
	cut = calorie_intake_calc(143.89,147.54,43,'M',0.05,'M')
	cut.amount_exercise = 'E'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_1():
	cut = calorie_intake_calc(46.06,179.59,69,'M',0.2,'S')
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

