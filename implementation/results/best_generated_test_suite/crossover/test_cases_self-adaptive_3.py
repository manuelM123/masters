from cut import *

def test_case_0():
	cut = calorie_intake_calc(184.24,169.14,74,'N',0.24,'N')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 193.82
	cut.amount_exercise = 'E'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.28
	cut.bodyfat = 0.7
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_1():
	cut = calorie_intake_calc(207.6,211.97,84,'N',0.48,'N')
	cut.weight = 44.49
	cut.height = 184.89
	cut.weight = 97.95

def test_case_2():
	cut = calorie_intake_calc(62.65,182.5,62,'F',-0.47,'L')

def test_case_3():
	cut = calorie_intake_calc(47.44,209.67,72,'F',0.47,'E')
	cut.gender = 'F'
	cut.bodyfat = 0.27
	cut.weight = 152.48
	cut.height = 139.89
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 191.42
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = -0.21

def test_case_4():
	cut = calorie_intake_calc(159.63,195.93,29,'M',-0.09,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 197.38

