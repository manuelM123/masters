from cut import *

def test_case_0():
	cut = calorie_intake_calc(102.96,154.63,62,'N',0.63,'S')
	cut.weight = 88.08
	cut.height = 219.78
	cut.height = 146.44

def test_case_1():
	cut = calorie_intake_calc(83.06,211.62,34,'F',-0.37,'N')
	cut.gender = 'N'
	cut.bodyfat = -0.09
	cut.weight = 114.46
	cut.height = 202.12
	result_tdee_calculation = cut.tdee_calculation()

def test_case_2():
	cut = calorie_intake_calc(209.01,210.87,55,'M',0.61,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'
	cut.bodyfat = -0.14
	cut.gender = 'N'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 219.54
	cut.age = 59

def test_case_3():
	cut = calorie_intake_calc(49.26,171.55,76,'N',0.65,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = -0.47

def test_case_4():
	cut = calorie_intake_calc(156.74,165.97,23,'M',0.09,'V')
	cut.weight = 203.03
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'L'
	cut.amount_exercise = 'L'
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 198.42

def test_case_5():
	cut = calorie_intake_calc(84.81,190.84,60,'N',-0.45,'N')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 212.49
	cut.age = 80
	cut.bodyfat = 0.29
	cut.bodyfat = 0.32
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'N'
	cut.amount_exercise = 'V'

def test_case_6():
	cut = calorie_intake_calc(163.89,160.04,81,'N',0.36,'E')
	cut.age = 80
	cut.weight = 154.12
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 15
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 192.23
	cut.weight = 171.67
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 207.32

