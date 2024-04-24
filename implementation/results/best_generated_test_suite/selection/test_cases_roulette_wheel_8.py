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
	cut = calorie_intake_calc(209.77,208.99,10,'M',0.22,'V')
	cut.bodyfat = 0.11
	cut.amount_exercise = 'E'
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(106.02,207.51,60,'N',0.14,'S')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_3():
	cut = calorie_intake_calc(95.65,215.72,44,'F',0.11,'L')
	cut.bodyfat = 0.1
	result_tdee_calculation = cut.tdee_calculation()

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

def test_case_5():
	cut = calorie_intake_calc(168.84,177.17,28,'M',0.12,'M')

def test_case_6():
	cut = calorie_intake_calc(146.33,158.51,60,'M',0.05,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

