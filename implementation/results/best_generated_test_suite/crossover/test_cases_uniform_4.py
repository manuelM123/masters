from cut import *

def test_case_0():
	cut = calorie_intake_calc(173.84,211.45,54,'M',-0.31,'S')
	cut.bodyfat = 0.61
	cut.gender = 'M'
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 66

def test_case_1():
	cut = calorie_intake_calc(209.19,167.15,13,'M',0.76,'L')
	cut.height = 156.76
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'F'
	result_tdee_calculation = cut.tdee_calculation()

def test_case_2():
	cut = calorie_intake_calc(186.63,145.8,30,'M',0.23,'E')
	cut.height = 210.16

def test_case_3():
	cut = calorie_intake_calc(97.37,156.62,57,'M',0.33,'M')
	cut.weight = 198.29
	cut.weight = 166.25
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 195.01
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'V'

def test_case_4():
	cut = calorie_intake_calc(151.41,149.71,45,'M',0.01,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = -0.22
	cut.age = 43
	cut.height = 201.7
	cut.age = 47
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'S'
	cut.age = 16
	cut.height = 139.45

