from cut import *

def test_case_0():
	cut = calorie_intake_calc(175.93,212.34,14,'M',-0.44,'E')
	cut.weight = 185.48
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_1():
	cut = calorie_intake_calc(150.92,195.06,34,'F',-0.05,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'V'

def test_case_2():
	cut = calorie_intake_calc(156.74,183.49,50,'M',-0.46,'E')
	cut.age = 55
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'F'

def test_case_3():
	cut = calorie_intake_calc(88.0,155.7,47,'M',0.04,'V')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = -0.06

def test_case_4():
	cut = calorie_intake_calc(144.32,216.36,57,'F',-0.21,'E')
	cut.bodyfat = 0.79
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

