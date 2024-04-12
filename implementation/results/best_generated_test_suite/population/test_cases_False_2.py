from cut import *

def test_case_0():
	cut = calorie_intake_calc(186.32,150.04,34,'F',0.06,'L')
	cut.bodyfat = 0.16
	cut.height = 191.52
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'N'
	cut.bodyfat = 0.13
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_1():
	cut = calorie_intake_calc(142.32,157.58,20,'F',0.26,'N')
	cut.weight = 146.26
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'F'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_2():
	cut = calorie_intake_calc(57.68,216.18,58,'M',0.22,'E')
	cut.bodyfat = 0.18
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 109.33
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'M'

def test_case_3():
	cut = calorie_intake_calc(163.71,192.15,80,'M',0.16,'V')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

