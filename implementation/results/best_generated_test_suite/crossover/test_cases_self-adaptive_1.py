from cut import *

def test_case_0():
	cut = calorie_intake_calc(118.31,188.6,67,'M',-0.34,'N')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_1():
	cut = calorie_intake_calc(86.55,138.05,81,'M',0.27,'M')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 196.86
	cut.height = 181.87
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'F'
	cut.height = 161.07

def test_case_2():
	cut = calorie_intake_calc(133.51,167.59,64,'F',-0.36,'S')
	cut.age = 71
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'L'
	cut.bodyfat = -0.41
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 60.77
	cut.bodyfat = 0.29
	cut.bodyfat = 0.67
	cut.height = 176.83

def test_case_3():
	cut = calorie_intake_calc(92.73,189.48,16,'N',0.15,'N')

def test_case_4():
	cut = calorie_intake_calc(37.11,174.07,80,'F',0.74,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = -0.25
	cut.height = 181.79
	cut.bodyfat = -0.03
	cut.age = 49

def test_case_5():
	cut = calorie_intake_calc(87.21,165.42,11,'M',-0.19,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'F'
	cut.age = 84
	cut.gender = 'N'
	cut.amount_exercise = 'V'
	cut.weight = 198.37
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

