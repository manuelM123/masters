from cut import *

def test_case_0():
	cut = calorie_intake_calc(99.5,183.07,60,'F',0.11,'M')
	cut.height = 165.79
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 178.34

def test_case_1():
	cut = calorie_intake_calc(97.19,143.89,69,'M',0.02,'V')
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 63.55

