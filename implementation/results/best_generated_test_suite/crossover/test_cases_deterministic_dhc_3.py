from cut import *

def test_case_0():
	cut = calorie_intake_calc(76.93,183.78,58,'F',0.18,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 147.22

def test_case_1():
	cut = calorie_intake_calc(73.72,211.22,28,'M',0.04,'S')
	cut.age = 77
	cut.amount_exercise = 'E'
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 197.51
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 151.73
	cut.gender = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 56

def test_case_2():
	cut = calorie_intake_calc(165.98,199.66,73,'M',0.08,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.17
	cut.gender = 'F'
	cut.gender = 'M'
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'M'
	cut.gender = 'N'

def test_case_3():
	cut = calorie_intake_calc(125.04,174.77,61,'N',0.24,'V')
	cut.age = 55
	cut.bodyfat = 0.28
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'F'

def test_case_4():
	cut = calorie_intake_calc(152.2,161.22,24,'M',0.12,'N')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 77

