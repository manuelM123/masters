from cut import *

def test_case_0():
	cut = calorie_intake_calc(167.64,183.44,75,'N',0.27,'V')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_1():
	cut = calorie_intake_calc(54.68,180.65,19,'M',0.28,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'L'

def test_case_2():
	cut = calorie_intake_calc(183.67,190.97,67,'N',0.06,'M')
	cut.bodyfat = 0.05
	cut.gender = 'F'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 121.38
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'N'
	cut.age = 63

def test_case_3():
	cut = calorie_intake_calc(190.94,202.06,26,'N',0.2,'V')
	cut.bodyfat = 0.15
	cut.weight = 95.03
	cut.amount_exercise = 'E'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.23
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 207.35
	result_determine_calorie_intake = cut.determine_calorie_intake()

