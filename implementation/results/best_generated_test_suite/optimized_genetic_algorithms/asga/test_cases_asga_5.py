from cut import *

def test_case_0():
	cut = calorie_intake_calc(159.17,190.75,58,'M',-0.44,'E')
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 191.9

def test_case_1():
	cut = calorie_intake_calc(200.1,192.47,60,'M',0.06,'S')
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 197.41

def test_case_2():
	cut = calorie_intake_calc(209.95,173.35,84,'N',-0.22,'M')
	cut.height = 197.57
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_3():
	cut = calorie_intake_calc(207.37,180.88,72,'N',0.32,'E')
	cut.height = 150.1
	cut.age = 64
	cut.amount_exercise = 'N'
	cut.age = 16

