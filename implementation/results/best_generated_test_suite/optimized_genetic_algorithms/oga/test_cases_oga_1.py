from cut import *

def test_case_0():
	cut = calorie_intake_calc(113.61,184.63,74,'M',0.66,'E')

def test_case_1():
	cut = calorie_intake_calc(47.69,213.37,53,'F',0.27,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 45
	result_tdee_calculation = cut.tdee_calculation()

def test_case_2():
	cut = calorie_intake_calc(64.85,150.22,27,'M',0.3,'N')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_3():
	cut = calorie_intake_calc(160.83,212.2,79,'F',-0.22,'M')
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_4():
	cut = calorie_intake_calc(71.79,148.14,8,'F',0.79,'L')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()

