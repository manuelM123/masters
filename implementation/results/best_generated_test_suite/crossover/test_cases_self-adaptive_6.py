from cut import *

def test_case_0():
	cut = calorie_intake_calc(44.0,192.97,11,'M',-0.46,'S')

def test_case_1():
	cut = calorie_intake_calc(78.67,173.07,34,'M',-0.48,'S')
	cut.height = 164.68
	cut.age = 50
	cut.height = 154.0
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 140.42
	cut.height = 187.9
	cut.gender = 'N'
	cut.weight = 207.24

def test_case_2():
	cut = calorie_intake_calc(160.62,174.57,63,'M',-0.32,'N')
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_3():
	cut = calorie_intake_calc(74.4,195.9,53,'F',0.19,'V')
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'F'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 29
	cut.height = 178.09
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

