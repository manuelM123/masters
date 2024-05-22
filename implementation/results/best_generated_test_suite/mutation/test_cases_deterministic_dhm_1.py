from cut import *

def test_case_0():
	cut = calorie_intake_calc(58.62,210.22,30,'M',0.72,'N')
	cut.amount_exercise = 'N'
	cut.amount_exercise = 'S'
	cut.bodyfat = -0.08
	cut.weight = 187.35
	cut.amount_exercise = 'M'

def test_case_1():
	cut = calorie_intake_calc(121.38,193.11,31,'F',0.2,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 178.53
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'N'
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_2():
	cut = calorie_intake_calc(173.61,224.66,23,'F',0.79,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 150.63

def test_case_3():
	cut = calorie_intake_calc(171.95,141.93,77,'N',0.67,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 46
	cut.height = 203.66
	cut.amount_exercise = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 200.04
	cut.gender = 'F'

def test_case_4():
	cut = calorie_intake_calc(142.31,201.11,41,'M',0.07,'S')
	cut.age = 14
	cut.amount_exercise = 'V'
	cut.weight = 41.79
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'S'

def test_case_5():
	cut = calorie_intake_calc(204.05,185.45,46,'M',0.22,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 212.77

def test_case_6():
	cut = calorie_intake_calc(203.16,217.04,10,'M',-0.32,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 64
	cut.gender = 'F'
	cut.age = 8
	cut.weight = 208.29
	result_determine_calorie_intake = cut.determine_calorie_intake()

