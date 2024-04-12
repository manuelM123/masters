from cut import *

def test_case_0():
	cut = calorie_intake_calc(62.64,156.09,12,'F',0.04,'E')

def test_case_1():
	cut = calorie_intake_calc(97.99,180.9,79,'N',0.26,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 36
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 113.46
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'M'

def test_case_2():
	cut = calorie_intake_calc(118.79,162.68,71,'M',0.14,'S')
	cut.height = 147.67
	cut.height = 179.6
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 62.9
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_3():
	cut = calorie_intake_calc(207.02,193.64,41,'N',0.22,'L')
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 206.73
	cut.amount_exercise = 'N'
	cut.amount_exercise = 'E'
	cut.bodyfat = 0.26
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'L'
	cut.height = 207.55
	cut.gender = 'N'

def test_case_4():
	cut = calorie_intake_calc(104.68,165.97,34,'N',0.23,'V')
	cut.weight = 98.26
	cut.amount_exercise = 'N'
	cut.age = 76
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_5():
	cut = calorie_intake_calc(202.51,145.03,38,'F',0.18,'S')
	cut.age = 14
	cut.bodyfat = 0.07
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_6():
	cut = calorie_intake_calc(84.62,195.05,61,'M',0.21,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'F'

def test_case_7():
	cut = calorie_intake_calc(161.63,172.67,62,'M',0.11,'L')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'M'
	cut.gender = 'N'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()

