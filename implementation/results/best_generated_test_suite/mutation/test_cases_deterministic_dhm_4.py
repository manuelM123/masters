from cut import *

def test_case_0():
	cut = calorie_intake_calc(121.04,162.45,47,'F',0.02,'V')

def test_case_1():
	cut = calorie_intake_calc(207.83,152.03,80,'N',0.28,'S')
	cut.weight = 202.38
	cut.bodyfat = 0.02
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 171.95
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'E'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_2():
	cut = calorie_intake_calc(55.81,142.98,60,'M',0.17,'V')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 15
	cut.gender = 'M'
	cut.weight = 118.68
	cut.height = 158.68
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.18
	cut.age = 23

def test_case_3():
	cut = calorie_intake_calc(70.53,161.95,24,'M',0.2,'E')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.19
	cut.weight = 101.56
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 73

def test_case_4():
	cut = calorie_intake_calc(67.07,152.87,34,'M',0.17,'M')
	cut.bodyfat = 0.11
	cut.gender = 'F'
	cut.bodyfat = 0.25
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 83.79
	result_tdee_calculation = cut.tdee_calculation()

def test_case_5():
	cut = calorie_intake_calc(165.87,191.41,46,'F',0.27,'M')
	cut.weight = 194.41
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 142.26

