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
	cut = calorie_intake_calc(190.84,213.57,34,'N',0.14,'E')
	cut.height = 203.56
	cut.weight = 116.97
	cut.height = 158.57
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'L'

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

def test_case_4():
	cut = calorie_intake_calc(112.78,166.05,36,'N',0.17,'M')
	cut.gender = 'F'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 73.86
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'N'

