from cut import *

def test_case_0():
	cut = calorie_intake_calc(39.98,202.91,58,'N',0.32,'L')
	cut.age = 84

def test_case_1():
	cut = calorie_intake_calc(104.08,182.72,63,'F',0.27,'L')
	cut.gender = 'F'
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 35.48

def test_case_2():
	cut = calorie_intake_calc(207.14,161.02,15,'M',0.03,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_3():
	cut = calorie_intake_calc(192.15,151.12,21,'M',-0.38,'N')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

