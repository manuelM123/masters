from cut import *

def test_case_0():
	cut = calorie_intake_calc(210.63,194.44,15,'M',0.09,'E')

def test_case_1():
	cut = calorie_intake_calc(163.27,201.04,32,'M',0.27,'L')
	cut.height = 172.08
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_2():
	cut = calorie_intake_calc(201.93,185.73,26,'F',0.08,'M')
	cut.gender = 'M'
	cut.height = 161.51
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'M'
	cut.amount_exercise = 'V'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'F'
	cut.height = 162.94

def test_case_3():
	cut = calorie_intake_calc(83.27,175.06,67,'F',0.12,'L')
	cut.height = 151.02
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 115.34
	cut.age = 71
	cut.gender = 'M'
	cut.bodyfat = 0.21
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 99.03

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
	cut = calorie_intake_calc(191.08,148.64,42,'F',0.18,'E')
	cut.height = 193.83

def test_case_6():
	cut = calorie_intake_calc(129.43,165.42,28,'M',0.15,'E')
	result_tdee_calculation = cut.tdee_calculation()

def test_case_7():
	cut = calorie_intake_calc(51.74,211.38,21,'F',0.08,'M')

def test_case_8():
	cut = calorie_intake_calc(54.48,149.44,58,'N',0.27,'V')
	cut.bodyfat = 0.16
	cut.gender = 'N'

