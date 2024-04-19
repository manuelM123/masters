from cut import *

def test_case_0():
	cut = calorie_intake_calc(175.64,208.99,63,'F',0.02,'L')

def test_case_1():
	cut = calorie_intake_calc(137.61,213.29,28,'N',0.04,'V')
	cut.age = 55
	cut.gender = 'F'

def test_case_2():
	cut = calorie_intake_calc(109.55,155.35,70,'N',0.28,'S')
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'M'

def test_case_3():
	cut = calorie_intake_calc(151.18,180.15,10,'F',0.3,'N')
	cut.height = 166.95
	cut.amount_exercise = 'V'
	cut.age = 41
	cut.amount_exercise = 'E'
	result_tdee_calculation = cut.tdee_calculation()

def test_case_4():
	cut = calorie_intake_calc(128.08,198.81,64,'M',0.05,'L')
	cut.age = 41
	cut.gender = 'M'
	cut.gender = 'M'
	cut.height = 198.37
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 57
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.19
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_5():
	cut = calorie_intake_calc(82.88,181.08,52,'F',0.24,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 168.26

def test_case_6():
	cut = calorie_intake_calc(129.43,165.42,28,'M',0.15,'E')
	result_tdee_calculation = cut.tdee_calculation()

