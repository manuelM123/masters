from cut import *

def test_case_0():
	cut = calorie_intake_calc(57.67,142.95,53,'F',0.01,'N')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'M'

def test_case_1():
	cut = calorie_intake_calc(109.64,212.98,60,'M',0.02,'E')
	cut.gender = 'N'

def test_case_2():
	cut = calorie_intake_calc(182.06,217.52,18,'M',0.16,'E')
	cut.height = 141.27

def test_case_3():
	cut = calorie_intake_calc(60.71,168.43,40,'M',0.15,'V')
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 46.7
	cut.age = 42
	cut.weight = 53.63
	cut.age = 73
	cut.age = 44
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 186.21

def test_case_4():
	cut = calorie_intake_calc(80.54,178.65,71,'N',0.03,'S')
	cut.bodyfat = 0.15

def test_case_5():
	cut = calorie_intake_calc(59.55,165.39,22,'F',0.17,'L')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'M'
	cut.amount_exercise = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.0
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.11
	cut.amount_exercise = 'S'

def test_case_6():
	cut = calorie_intake_calc(152.67,183.45,73,'F',0.28,'N')
	cut.height = 177.84
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_7():
	cut = calorie_intake_calc(99.29,167.1,50,'M',0.05,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 146.46

def test_case_8():
	cut = calorie_intake_calc(103.65,183.26,52,'M',0.11,'N')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 205.97
	cut.age = 46
	cut.bodyfat = 0.29
	cut.age = 60
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 78

def test_case_9():
	cut = calorie_intake_calc(116.52,206.75,45,'M',0.19,'S')
	cut.amount_exercise = 'V'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 69.07
	cut.gender = 'F'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'N'
	cut.weight = 126.5

