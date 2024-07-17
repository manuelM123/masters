from cut import *

def test_case_0():
	cut = calorie_intake_calc(181.74,174.48,36,'M',-0.04,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.55

def test_case_1():
	cut = calorie_intake_calc(84.32,186.63,81,'N',0.2,'E')
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 78

