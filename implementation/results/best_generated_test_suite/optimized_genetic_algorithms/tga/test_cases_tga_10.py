from cut import *

def test_case_0():
	cut = calorie_intake_calc(152.16,166.11,31,'M',-0.25,'N')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 178.37
	cut.bodyfat = -0.15

def test_case_1():
	cut = calorie_intake_calc(205.3,151.64,31,'M',0.04,'M')
	cut.gender = 'M'
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.67

def test_case_2():
	cut = calorie_intake_calc(173.81,168.68,30,'F',-0.35,'M')
	cut.amount_exercise = 'S'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

