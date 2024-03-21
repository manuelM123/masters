from cut import *

def test_case_0():
	cut = calorie_intake_calc(67.51,217.63,38,'F',0.12,'N')
	cut.weight = 69.35

def test_case_1():
	cut = calorie_intake_calc(208.69,203.5,13,'N',0.27,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_2():
	cut = calorie_intake_calc(174.57,183.94,80,'M',0.05,'E')
	cut.age = 66
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()

