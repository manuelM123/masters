from cut import *

def test_case_0():
	cut = calorie_intake_calc(48.86,223.21,52,'F',-0.34,'M')

def test_case_1():
	cut = calorie_intake_calc(201.68,164.96,51,'F',-0.05,'S')
	result_tdee_calculation = cut.tdee_calculation()

def test_case_2():
	cut = calorie_intake_calc(148.86,218.49,52,'N',-0.16,'E')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_3():
	cut = calorie_intake_calc(116.03,147.99,10,'F',0.02,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.19

