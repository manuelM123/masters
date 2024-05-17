from cut import *

def test_case_0():
	cut = calorie_intake_calc(186.7,158.12,12,'M',0.17,'V')
	cut.bodyfat = 0.42

def test_case_1():
	cut = calorie_intake_calc(144.78,217.97,18,'M',0.46,'V')
	cut.bodyfat = 0.05
	cut.gender = 'N'
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.34
	cut.amount_exercise = 'E'

def test_case_2():
	cut = calorie_intake_calc(154.85,197.32,63,'F',0.13,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = -0.39
	cut.height = 194.3
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'E'
	cut.gender = 'F'
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'N'

def test_case_3():
	cut = calorie_intake_calc(162.24,162.12,53,'N',0.45,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 70

