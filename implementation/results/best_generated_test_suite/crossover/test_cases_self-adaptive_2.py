from cut import *

def test_case_0():
	cut = calorie_intake_calc(169.07,197.8,16,'M',0.21,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'M'

def test_case_1():
	cut = calorie_intake_calc(41.34,180.41,71,'M',0.27,'V')
	cut.bodyfat = 0.07

def test_case_2():
	cut = calorie_intake_calc(129.72,148.42,54,'N',0.28,'L')
	cut.age = 22

def test_case_3():
	cut = calorie_intake_calc(116.81,219.24,38,'F',0.24,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

