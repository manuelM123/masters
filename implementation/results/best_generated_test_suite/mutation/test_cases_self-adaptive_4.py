from cut import *

def test_case_0():
	cut = calorie_intake_calc(53.31,154.33,75,'N',-0.1,'E')
	cut.height = 198.76
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'F'

def test_case_1():
	cut = calorie_intake_calc(197.56,190.12,44,'M',-0.29,'L')

def test_case_2():
	cut = calorie_intake_calc(61.22,206.45,64,'M',0.09,'E')
	cut.age = 55

def test_case_3():
	cut = calorie_intake_calc(174.82,212.26,50,'N',0.2,'V')
	cut.weight = 82.98
	cut.gender = 'N'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 191.39
	cut.weight = 94.79
	cut.height = 176.38
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'F'
	cut.height = 220.28

def test_case_4():
	cut = calorie_intake_calc(130.5,165.5,25,'M',-0.14,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'F'
	result_tdee_calculation = cut.tdee_calculation()

