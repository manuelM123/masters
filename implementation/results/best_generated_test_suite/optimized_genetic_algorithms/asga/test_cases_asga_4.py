from cut import *

def test_case_0():
	cut = calorie_intake_calc(44.17,157.72,50,'M',0.15,'E')
	cut.amount_exercise = 'S'
	cut.weight = 173.9
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'L'

def test_case_1():
	cut = calorie_intake_calc(69.0,214.7,30,'M',-0.07,'N')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'N'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_2():
	cut = calorie_intake_calc(129.85,191.73,48,'F',-0.41,'V')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 162.89

def test_case_3():
	cut = calorie_intake_calc(138.8,144.47,65,'N',0.72,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 74

