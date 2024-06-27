from cut import *

def test_case_0():
	cut = calorie_intake_calc(210.13,164.94,45,'M',-0.26,'V')
	cut.gender = 'N'
	cut.age = 62
	cut.amount_exercise = 'M'

def test_case_1():
	cut = calorie_intake_calc(144.07,152.77,66,'M',0.7,'S')

def test_case_2():
	cut = calorie_intake_calc(179.32,218.77,13,'M',0.05,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = -0.06
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_3():
	cut = calorie_intake_calc(133.36,215.34,46,'M',0.03,'V')
	cut.bodyfat = -0.4
	cut.gender = 'F'
	result_tdee_calculation = cut.tdee_calculation()

