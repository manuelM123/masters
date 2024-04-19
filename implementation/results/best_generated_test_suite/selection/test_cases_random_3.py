from cut import *

def test_case_0():
	cut = calorie_intake_calc(76.28,196.19,52,'N',0.23,'L')

def test_case_1():
	cut = calorie_intake_calc(198.96,208.52,31,'F',0.29,'M')
	cut.gender = 'N'
	cut.bodyfat = 0.15

def test_case_2():
	cut = calorie_intake_calc(177.0,173.03,21,'F',0.08,'L')
	cut.amount_exercise = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'S'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'S'
	cut.amount_exercise = 'V'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.04

def test_case_3():
	cut = calorie_intake_calc(210.1,201.57,78,'N',0.03,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'N'
	cut.bodyfat = 0.28

def test_case_4():
	cut = calorie_intake_calc(128.08,198.81,64,'M',0.05,'L')
	cut.age = 41
	cut.gender = 'M'
	cut.gender = 'M'
	cut.height = 198.37
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 57
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.19
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_5():
	cut = calorie_intake_calc(109.96,195.73,31,'N',0.28,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 164.46

def test_case_6():
	cut = calorie_intake_calc(129.43,165.42,28,'M',0.15,'E')
	result_tdee_calculation = cut.tdee_calculation()

def test_case_7():
	cut = calorie_intake_calc(207.83,160.77,72,'F',0.13,'E')
	cut.age = 52
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'N'
	cut.height = 179.07
	result_tdee_calculation = cut.tdee_calculation()

