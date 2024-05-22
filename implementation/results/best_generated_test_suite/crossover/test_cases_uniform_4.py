from cut import *

def test_case_0():
	cut = calorie_intake_calc(58.62,210.22,30,'M',0.72,'N')
	cut.weight = 150.24
	cut.amount_exercise = 'S'
	cut.bodyfat = -0.08
	cut.bodyfat = 0.41
	cut.amount_exercise = 'M'

def test_case_1():
	cut = calorie_intake_calc(74.62,204.43,65,'F',-0.32,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.71
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_2():
	cut = calorie_intake_calc(204.4,205.91,25,'F',0.43,'L')
	cut.amount_exercise = 'E'
	cut.gender = 'M'
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 167.48
	cut.amount_exercise = 'V'
	result_tdee_calculation = cut.tdee_calculation()

def test_case_3():
	cut = calorie_intake_calc(64.52,139.7,5,'F',0.64,'N')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_4():
	cut = calorie_intake_calc(112.12,153.12,40,'M',-0.21,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 200.06
	cut.gender = 'N'
	cut.height = 168.32
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_5():
	cut = calorie_intake_calc(91.75,170.4,49,'N',-0.4,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 171.64
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'V'

def test_case_6():
	cut = calorie_intake_calc(126.66,194.54,22,'F',0.47,'M')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

