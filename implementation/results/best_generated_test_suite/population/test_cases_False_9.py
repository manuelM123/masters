from cut import *

def test_case_0():
	cut = calorie_intake_calc(115.6,170.95,13,'F',0.04,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.13
	cut.age = 30
	cut.height = 154.37
	cut.bodyfat = 0.29

def test_case_1():
	cut = calorie_intake_calc(54.68,180.65,19,'M',0.28,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'L'

def test_case_2():
	cut = calorie_intake_calc(190.84,213.57,34,'N',0.14,'E')
	cut.height = 203.56
	cut.weight = 116.97
	cut.height = 158.57
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'L'

def test_case_3():
	cut = calorie_intake_calc(190.94,202.06,26,'N',0.2,'V')
	cut.bodyfat = 0.15
	cut.weight = 95.03
	cut.amount_exercise = 'E'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.23
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 207.35
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_4():
	cut = calorie_intake_calc(93.11,220.07,68,'F',0.03,'M')
	cut.age = 45
	cut.bodyfat = 0.1

