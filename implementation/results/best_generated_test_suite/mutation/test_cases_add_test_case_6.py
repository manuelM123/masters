from cut import *

def test_case_0():
	cut = calorie_intake_calc(42.25,149.0,82,'F',-0.46,'S')
	cut.bodyfat = -0.02
	cut.weight = 177.93
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_1():
	cut = calorie_intake_calc(76.56,172.55,61,'N',-0.08,'M')
	cut.amount_exercise = 'E'
	cut.height = 218.47
	cut.weight = 92.49
	cut.height = 198.7
	cut.age = 30

def test_case_2():
	cut = calorie_intake_calc(79.2,191.17,42,'N',-0.26,'E')
	cut.amount_exercise = 'S'

def test_case_3():
	cut = calorie_intake_calc(194.56,164.7,25,'F',-0.14,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'V'

def test_case_4():
	cut = calorie_intake_calc(185.14,176.62,21,'F',0.68,'N')

def test_case_5():
	cut = calorie_intake_calc(198.68,166.2,33,'M',0.13,'E')
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'M'

