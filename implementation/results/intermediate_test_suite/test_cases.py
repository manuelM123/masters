from cut import *

def test_case_0():
	cut = calorie_intake_calc(131.15,143.61,21,'M',0.12,'V')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.12

def test_case_1():
	cut = calorie_intake_calc(170.14,160.69,62,'N',0.2,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(47.4,205.8,80,'F',0.12,'E')

def test_case_3():
	cut = calorie_intake_calc(116.19,144.17,41,'N',0.28,'N')
	cut.height = 200.35

