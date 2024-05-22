from cut import *

def test_case_0():
	cut = calorie_intake_calc(209.89,138.65,14,'M',0.59,'N')
	cut.gender = 'N'
	cut.amount_exercise = 'V'
	cut.height = 179.2
	cut.amount_exercise = 'N'

def test_case_1():
	cut = calorie_intake_calc(198.67,161.9,43,'F',-0.25,'S')
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'M'
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'M'
	cut.amount_exercise = 'N'
	cut.gender = 'F'
	cut.gender = 'M'

def test_case_2():
	cut = calorie_intake_calc(137.13,153.66,24,'F',-0.2,'M')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 6
	cut.gender = 'F'
	cut.amount_exercise = 'S'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_3():
	cut = calorie_intake_calc(123.59,160.41,74,'M',0.67,'L')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'M'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.05
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 61.88

def test_case_4():
	cut = calorie_intake_calc(82.92,184.01,38,'F',-0.4,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = -0.07
	cut.gender = 'F'
	cut.age = 6

def test_case_5():
	cut = calorie_intake_calc(141.81,165.37,73,'M',0.04,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 219.27
	cut.bodyfat = 0.41
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.57
	cut.amount_exercise = 'N'

def test_case_6():
	cut = calorie_intake_calc(162.87,170.0,60,'F',-0.16,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 64.51
	cut.height = 218.72
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 76

def test_case_7():
	cut = calorie_intake_calc(47.16,170.98,39,'N',0.07,'V')
	cut.height = 182.31
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

