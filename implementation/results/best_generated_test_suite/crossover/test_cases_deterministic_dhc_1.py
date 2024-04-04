from cut import *

def test_case_0():
	cut = calorie_intake_calc(207.74,220.94,29,'M',0.21,'M')
	result_tdee_calculation = cut.tdee_calculation()

def test_case_1():
	cut = calorie_intake_calc(153.44,184.68,24,'M',0.13,'L')
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.27
	cut.age = 25

