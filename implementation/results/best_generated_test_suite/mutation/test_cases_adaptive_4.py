from cut import *

def test_case_0():
	cut = calorie_intake_calc(106.07,162.51,51,'M',0.16,'M')
	cut.weight = 146.16

def test_case_1():
	cut = calorie_intake_calc(147.74,197.68,48,'N',0.15,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 51.88
	cut.bodyfat = 0.04
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.27
	cut.age = 69
	cut.bodyfat = 0.18

def test_case_2():
	cut = calorie_intake_calc(157.27,141.81,27,'M',0.28,'M')
	cut.amount_exercise = 'L'
	cut.gender = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'N'
	cut.height = 207.64
	cut.weight = 188.49
	cut.gender = 'F'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'F'
	cut.age = 54

def test_case_3():
	cut = calorie_intake_calc(104.77,192.83,47,'M',0.11,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 33
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_4():
	cut = calorie_intake_calc(184.53,182.92,46,'F',0.15,'N')
	cut.bodyfat = 0.13
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 215.45

