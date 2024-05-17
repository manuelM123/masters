from cut import *

def test_case_0():
	cut = calorie_intake_calc(49.58,197.22,69,'F',0.11,'S')
	cut.bodyfat = 0.61
	cut.gender = 'N'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.02
	cut.height = 169.11
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_1():
	cut = calorie_intake_calc(188.38,145.31,8,'M',-0.4,'V')
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'L'
	cut.bodyfat = 0.53

def test_case_2():
	cut = calorie_intake_calc(211.25,205.8,53,'F',0.1,'L')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.36
	cut.amount_exercise = 'S'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 70.16
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_3():
	cut = calorie_intake_calc(208.52,143.11,67,'N',0.53,'L')
	cut.amount_exercise = 'E'
	cut.amount_exercise = 'V'

def test_case_4():
	cut = calorie_intake_calc(195.71,155.3,58,'M',0.17,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = -0.39
	cut.height = 167.16
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.66
	cut.gender = 'N'
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_5():
	cut = calorie_intake_calc(51.26,196.5,80,'F',-0.01,'V')

def test_case_6():
	cut = calorie_intake_calc(138.43,194.22,78,'F',-0.06,'E')
	cut.age = 59
	cut.height = 212.27
	cut.weight = 187.66
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 32
	cut.weight = 38.34

