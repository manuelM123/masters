from cut import *

def test_case_0():
	cut = calorie_intake_calc(134.35,144.7,8,'M',-0.43,'L')

def test_case_1():
	cut = calorie_intake_calc(201.68,164.96,51,'F',-0.05,'S')
	result_tdee_calculation = cut.tdee_calculation()

def test_case_2():
	cut = calorie_intake_calc(148.86,218.49,52,'N',-0.16,'E')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_3():
	cut = calorie_intake_calc(116.51,145.55,46,'F',-0.23,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.19

def test_case_4():
	cut = calorie_intake_calc(170.48,190.95,53,'M',-0.08,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 191.29
	cut.height = 189.76
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 20

