from cut import *

def test_case_0():
	cut = calorie_intake_calc(170.57,155.77,79,'M',0.17,'S')
	cut.age = 23
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 44
	cut.gender = 'F'
	cut.amount_exercise = 'S'

def test_case_1():
	cut = calorie_intake_calc(209.77,208.99,10,'M',0.22,'V')
	cut.bodyfat = 0.11
	cut.amount_exercise = 'E'
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(152.73,207.12,15,'N',0.04,'N')
	cut.height = 190.32
	cut.age = 37
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_3():
	cut = calorie_intake_calc(141.95,215.36,37,'M',0.28,'V')
	cut.weight = 68.48
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.26

def test_case_4():
	cut = calorie_intake_calc(95.08,163.77,62,'M',0.2,'L')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'F'
	cut.bodyfat = 0.12
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'L'
	cut.age = 60
	cut.weight = 86.73
	cut.height = 141.05
	cut.gender = 'M'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

