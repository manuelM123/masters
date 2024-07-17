from cut import *

def test_case_0():
	cut = calorie_intake_calc(54.66,174.35,80,'F',-0.47,'L')

def test_case_1():
	cut = calorie_intake_calc(130.41,223.13,66,'M',0.33,'L')
	cut.gender = 'N'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'N'
	cut.height = 196.25

def test_case_2():
	cut = calorie_intake_calc(103.24,168.26,22,'N',0.03,'V')
	cut.weight = 105.69
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_3():
	cut = calorie_intake_calc(158.09,203.43,24,'N',-0.35,'M')
	cut.bodyfat = 0.66

def test_case_4():
	cut = calorie_intake_calc(195.66,203.54,5,'F',-0.48,'S')
	cut.bodyfat = 0.0

def test_case_5():
	cut = calorie_intake_calc(86.8,138.62,49,'M',0.7,'N')
	cut.amount_exercise = 'V'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'N'
	cut.amount_exercise = 'V'

def test_case_6():
	cut = calorie_intake_calc(91.24,143.08,11,'F',-0.37,'E')
	cut.weight = 60.74
	result_determine_calorie_intake = cut.determine_calorie_intake()

