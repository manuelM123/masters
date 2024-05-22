from cut import *

def test_case_0():
	cut = calorie_intake_calc(181.93,182.11,79,'F',-0.22,'S')
	cut.amount_exercise = 'S'
	cut.weight = 75.81
	cut.height = 197.21
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'L'
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'N'
	cut.amount_exercise = 'V'

def test_case_1():
	cut = calorie_intake_calc(110.12,155.12,16,'F',-0.21,'S')
	cut.amount_exercise = 'E'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'M'
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 174.72
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_2():
	cut = calorie_intake_calc(58.99,196.07,9,'N',0.3,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 135.66
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'L'
	cut.height = 182.24

def test_case_3():
	cut = calorie_intake_calc(41.65,146.24,45,'M',0.08,'L')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 138.34

def test_case_4():
	cut = calorie_intake_calc(42.29,153.45,10,'N',0.66,'L')
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'N'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 25
	cut.weight = 66.0

