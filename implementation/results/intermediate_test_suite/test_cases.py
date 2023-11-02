from cut import *

def test_case_0():
	cut = calorie_intake_calc(51.78,171.52,72,'M',0.27,'L')
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_1():
	cut = calorie_intake_calc(72.84,163.04,12,'M',0.2,'N')

def test_case_2():
	cut = calorie_intake_calc(153.68,171.49,53,'F',0.06,'M')
	cut.gender = 'F'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_3():
	cut = calorie_intake_calc(161.53,206.15,55,'F',0.21,'V')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'N'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_4():
	cut = calorie_intake_calc(79.37,208.48,10,'M',0.1,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 72.72
	cut.weight = 204.29
	cut.age = 70

def test_case_5():
	cut = calorie_intake_calc(128.91,191.48,31,'M',0.21,'S')

