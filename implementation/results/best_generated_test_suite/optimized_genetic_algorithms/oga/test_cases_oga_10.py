from cut import *

def test_case_0():
	cut = calorie_intake_calc(100.15,148.24,62,'M',-0.37,'E')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 205.05
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'N'

def test_case_1():
	cut = calorie_intake_calc(84.8,159.22,24,'F',-0.28,'E')
	cut.amount_exercise = 'M'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 27

def test_case_2():
	cut = calorie_intake_calc(153.74,188.49,35,'F',0.04,'V')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'S'
	cut.weight = 119.92
	result_tdee_calculation = cut.tdee_calculation()

def test_case_3():
	cut = calorie_intake_calc(124.12,144.37,31,'F',-0.35,'V')
	cut.weight = 60.15
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'M'

def test_case_4():
	cut = calorie_intake_calc(106.61,173.53,18,'N',0.76,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 42
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

