from cut import *

def test_case_0():
	cut = calorie_intake_calc(165.39,157.64,80,'F',0.15,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 166.5
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'F'
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'F'
	cut.age = 22

def test_case_1():
	cut = calorie_intake_calc(103.66,145.83,39,'M',-0.2,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'M'
	cut.gender = 'N'

def test_case_2():
	cut = calorie_intake_calc(66.79,201.32,45,'F',0.61,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 125.32
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 28
	cut.gender = 'N'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

