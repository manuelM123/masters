from cut import *

def test_case_0():
	cut = calorie_intake_calc(167.32,174.31,20,'N',0.16,'M')

def test_case_1():
	cut = calorie_intake_calc(201.4,178.28,72,'M',0.29,'N')
	cut.bodyfat = 0.25
	cut.bodyfat = 0.22

def test_case_2():
	cut = calorie_intake_calc(109.39,195.61,61,'F',0.29,'E')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_3():
	cut = calorie_intake_calc(135.57,216.18,27,'M',0.08,'V')
	result_tdee_calculation = cut.tdee_calculation()

def test_case_4():
	cut = calorie_intake_calc(112.69,215.88,36,'N',0.26,'S')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

