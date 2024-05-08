from cut import *

def test_case_0():
	cut = calorie_intake_calc(161.56,220.98,68,'N',0.72,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'M'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_1():
	cut = calorie_intake_calc(181.79,141.08,32,'F',-0.09,'E')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 209.48
	cut.bodyfat = 0.36
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 156.26

def test_case_2():
	cut = calorie_intake_calc(163.47,201.36,12,'N',0.12,'S')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 167.71
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'F'
	cut.age = 40
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_3():
	cut = calorie_intake_calc(130.16,184.59,8,'N',0.4,'E')
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'N'

def test_case_4():
	cut = calorie_intake_calc(170.11,183.87,72,'M',0.01,'N')
	cut.age = 24
	cut.age = 57
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

