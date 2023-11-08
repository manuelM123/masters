from cut import *

def test_case_0():
	cut = calorie_intake_calc(44.64,162.04,57,'N',0.11,'L')
	cut.height = 177.73
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(207.66,188.31,26,'M',0.27,'V')

def test_case_2():
	cut = calorie_intake_calc(182.28,140.47,12,'N',0.13,'L')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 70

def test_case_3():
	cut = calorie_intake_calc(100.83,185.95,48,'F',0.29,'M')
	result_tdee_calculation = cut.tdee_calculation()

