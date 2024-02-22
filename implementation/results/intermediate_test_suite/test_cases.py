from cut import *

def test_case_0():
	cut = calorie_intake_calc(40.89,196.11,20,'M',0.05,'E')
	result_tdee_calculation = cut.tdee_calculation()

def test_case_1():
	cut = calorie_intake_calc(194.38,177.76,35,'F',0.1,'M')
	cut.age = 70
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_2():
	cut = calorie_intake_calc(80.82,147.12,23,'N',0.16,'L')
	cut.amount_exercise = 'E'
	cut.age = 23
	cut.bodyfat = 0.13

def test_case_3():
	cut = calorie_intake_calc(160.97,205.03,79,'F',0.23,'N')

