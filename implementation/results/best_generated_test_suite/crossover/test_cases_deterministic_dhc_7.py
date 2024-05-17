from cut import *

def test_case_0():
	cut = calorie_intake_calc(102.96,154.63,62,'N',0.63,'S')
	cut.weight = 88.08
	cut.height = 219.78
	cut.height = 146.44

def test_case_1():
	cut = calorie_intake_calc(170.51,171.76,75,'N',-0.35,'V')
	cut.age = 64
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'N'
	cut.weight = 90.89
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'M'
	cut.age = 6
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

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
	cut = calorie_intake_calc(142.28,140.23,59,'N',0.68,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_4():
	cut = calorie_intake_calc(156.74,165.97,23,'M',0.09,'V')
	cut.weight = 203.03
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'M'
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
	cut = calorie_intake_calc(214.49,218.81,81,'F',0.24,'M')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.45
	cut.height = 141.67
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'F'
	cut.height = 149.21

def test_case_7():
	cut = calorie_intake_calc(102.74,196.13,83,'M',0.6,'N')
	cut.gender = 'M'

