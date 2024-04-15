from cut import *

def test_case_0():
	cut = calorie_intake_calc(166.69,200.75,74,'N',0.22,'M')
	cut.weight = 131.69
	cut.height = 149.83

def test_case_1():
	cut = calorie_intake_calc(148.09,183.7,46,'M',0.19,'E')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_2():
	cut = calorie_intake_calc(44.54,145.44,69,'F',0.11,'L')
	cut.gender = 'M'
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 24

def test_case_3():
	cut = calorie_intake_calc(97.76,147.83,53,'M',0.27,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

