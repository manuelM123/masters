from cut import *

def test_case_0():
	cut = calorie_intake_calc(178.9,162.77,81,'N',0.16,'N')
	cut.age = 74
	cut.age = 43
	cut.gender = 'M'
	cut.weight = 199.12
	cut.height = 178.32
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 181.66
	cut.bodyfat = 0.23

def test_case_1():
	cut = calorie_intake_calc(144.6,146.12,79,'F',0.17,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 188.65
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 169.16
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 164.32
	cut.bodyfat = 0.11
	cut.gender = 'N'
	cut.bodyfat = 0.22

def test_case_2():
	cut = calorie_intake_calc(65.14,201.41,14,'M',0.13,'L')
	cut.height = 208.24
	cut.bodyfat = 0.21
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

