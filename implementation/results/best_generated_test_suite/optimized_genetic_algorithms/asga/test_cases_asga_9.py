from cut import *

def test_case_0():
	cut = calorie_intake_calc(93.82,164.62,35,'M',-0.15,'S')
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 154.52
	cut.gender = 'F'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_1():
	cut = calorie_intake_calc(81.35,183.29,45,'F',0.06,'N')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_2():
	cut = calorie_intake_calc(210.01,155.14,30,'M',0.05,'M')
	cut.amount_exercise = 'E'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 96.66
	cut.height = 156.41

def test_case_3():
	cut = calorie_intake_calc(121.66,141.02,74,'M',0.75,'N')
	cut.amount_exercise = 'M'

