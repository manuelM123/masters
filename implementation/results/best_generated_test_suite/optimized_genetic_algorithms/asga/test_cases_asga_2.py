from cut import *

def test_case_0():
	cut = calorie_intake_calc(185.79,163.22,79,'F',-0.48,'E')
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 141.34

def test_case_1():
	cut = calorie_intake_calc(86.19,153.6,69,'F',-0.08,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 76

def test_case_2():
	cut = calorie_intake_calc(41.45,204.49,74,'M',0.29,'L')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.38

