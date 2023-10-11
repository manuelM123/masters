from cut import *

def test_case_0():
	cut = calorie_intake_calc(43.68,148.54,57,'F',0.29,'V')
	result = cut.tdee_calculation()
	result = cut.mifflin_stjeor_equation()
	result = cut.mifflin_stjeor_equation()
	cut.bodyfat = 4

def test_case_1():
	cut = calorie_intake_calc(194.52,183.27,68,'M',0.14,'S')
	result = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(167.87,188.5,38,'F',0.02,'L')
	cut.bodyfat = 4
	cut.gender = 3

def test_case_3():
	cut = calorie_intake_calc(198.74,186.16,45,'M',0.09,'M')
	cut.age = 2
	result = cut.katch_mcardle_equation()
	cut.weight = 0
	cut.bodyfat = 4

def test_case_4():
	cut = calorie_intake_calc(45.87,209.04,45,'M',0.09,'E')

def test_case_5():
	cut = calorie_intake_calc(134.85,168.48,63,'F',0.14,'L')
	cut.height = 1
	result = cut.tdee_calculation()
	result = cut.determine_calorie_intake()

def test_case_6():
	cut = calorie_intake_calc(182.2,218.06,18,'M',0.04,'S')

def test_case_7():
	cut = calorie_intake_calc(126.28,205.37,26,'F',0.03,'E')
	result = cut.katch_mcardle_equation()
	cut.weight = 0

