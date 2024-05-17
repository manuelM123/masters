from cut import *

def test_case_0():
	cut = calorie_intake_calc(163.47,162.23,62,'M',0.05,'E')
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'S'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'E'
	cut.weight = 73.59

