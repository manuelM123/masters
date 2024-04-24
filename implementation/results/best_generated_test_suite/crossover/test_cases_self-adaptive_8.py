from cut import *

def test_case_0():
	cut = calorie_intake_calc(51.08,216.24,50,'M',0.18,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.09
	cut.amount_exercise = 'L'
	cut.amount_exercise = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.24
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 159.46

def test_case_1():
	cut = calorie_intake_calc(185.46,212.47,60,'F',0.19,'L')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'M'
	cut.amount_exercise = 'E'
	cut.height = 210.46
	cut.weight = 107.36
	cut.weight = 84.89
	cut.gender = 'N'

def test_case_2():
	cut = calorie_intake_calc(122.29,148.23,71,'N',0.16,'E')

def test_case_3():
	cut = calorie_intake_calc(154.0,162.32,37,'F',0.22,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 198.35

def test_case_4():
	cut = calorie_intake_calc(103.83,150.75,76,'F',0.16,'S')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 120.07
	result_tdee_calculation = cut.tdee_calculation()

