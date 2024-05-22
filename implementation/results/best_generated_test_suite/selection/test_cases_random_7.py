from cut import *

def test_case_0():
	cut = calorie_intake_calc(182.72,183.19,14,'N',0.5,'V')
	cut.amount_exercise = 'N'
	cut.age = 71

def test_case_1():
	cut = calorie_intake_calc(158.96,197.99,23,'F',0.63,'L')
	cut.bodyfat = 0.5
	cut.amount_exercise = 'V'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'F'
	cut.amount_exercise = 'S'
	cut.amount_exercise = 'E'
	cut.age = 49
	cut.amount_exercise = 'L'

def test_case_2():
	cut = calorie_intake_calc(71.87,178.85,36,'M',-0.33,'V')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 162.77
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 171.14
	cut.age = 15
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 182.07
	cut.age = 55

