from cut import *

def test_case_0():
	cut = calorie_intake_calc(139.08,188.74,37,'N',0.1,'M')
	cut.age = 37
	cut.bodyfat = 0.06
	cut.height = 219.29
	cut.height = 176.02

def test_case_1():
	cut = calorie_intake_calc(142.66,140.38,43,'F',0.11,'N')
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 219.96
	cut.weight = 124.81

def test_case_2():
	cut = calorie_intake_calc(89.24,172.29,59,'F',0.27,'V')
	cut.height = 210.58
	cut.bodyfat = 0.12
	cut.bodyfat = 0.27
	cut.height = 194.7
	cut.bodyfat = 0.29
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 188.44
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'M'

def test_case_3():
	cut = calorie_intake_calc(174.62,149.54,42,'F',0.13,'E')
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'N'
	cut.height = 141.94
	cut.weight = 75.38

def test_case_4():
	cut = calorie_intake_calc(77.91,144.9,11,'M',0.16,'E')
	cut.amount_exercise = 'N'
	cut.amount_exercise = 'S'
	cut.amount_exercise = 'V'
	cut.bodyfat = 0.09

