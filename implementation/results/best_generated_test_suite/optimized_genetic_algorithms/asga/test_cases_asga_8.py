from cut import *

def test_case_0():
	cut = calorie_intake_calc(115.48,136.94,77,'M',0.45,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(105.84,168.86,14,'F',0.6,'S')

def test_case_2():
	cut = calorie_intake_calc(158.91,194.65,44,'F',0.17,'S')
	cut.bodyfat = 0.02
	cut.age = 75
	cut.height = 173.29
	result_tdee_calculation = cut.tdee_calculation()

def test_case_3():
	cut = calorie_intake_calc(100.31,198.24,47,'M',-0.41,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'N'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'N'

