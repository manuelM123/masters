from cut import *

def test_case_0():
	cut = calorie_intake_calc(74.24,183.63,61,'F',-0.5,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = -0.28
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'E'
	cut.bodyfat = -0.18
	cut.amount_exercise = 'V'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 62

def test_case_1():
	cut = calorie_intake_calc(200.22,155.5,69,'M',0.3,'M')
	cut.height = 172.45
	cut.height = 199.85
	cut.amount_exercise = 'V'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.49
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 52
	cut.height = 223.47

