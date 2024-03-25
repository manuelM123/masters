from cut import *

def test_case_0():
	cut = calorie_intake_calc(76.24,200.19,48,'M',0.12,'L')
	cut.weight = 137.19
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'N'
	cut.amount_exercise = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 152.35
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 142.73
	cut.gender = 'N'

def test_case_1():
	cut = calorie_intake_calc(79.03,196.42,75,'M',0.02,'V')

def test_case_2():
	cut = calorie_intake_calc(90.9,160.43,64,'F',0.27,'E')
	cut.gender = 'N'
	cut.weight = 138.7

def test_case_3():
	cut = calorie_intake_calc(41.19,199.89,68,'M',0.19,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'V'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

