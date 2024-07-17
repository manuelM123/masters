from cut import *

def test_case_0():
	cut = calorie_intake_calc(83.78,164.59,33,'F',0.5,'L')
	cut.gender = 'M'
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'F'

def test_case_1():
	cut = calorie_intake_calc(101.06,168.37,83,'M',0.26,'M')

def test_case_2():
	cut = calorie_intake_calc(197.81,190.4,42,'F',-0.18,'V')
	cut.age = 81

def test_case_3():
	cut = calorie_intake_calc(62.55,221.25,85,'M',0.53,'V')
	cut.bodyfat = 0.1
	cut.height = 185.48

def test_case_4():
	cut = calorie_intake_calc(94.83,224.81,70,'F',0.75,'V')
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 138.62

def test_case_5():
	cut = calorie_intake_calc(61.34,189.69,13,'N',0.75,'E')
	cut.age = 33

def test_case_6():
	cut = calorie_intake_calc(62.03,199.96,26,'M',0.57,'E')

def test_case_7():
	cut = calorie_intake_calc(195.35,150.32,79,'N',0.25,'E')
	cut.gender = 'M'

def test_case_8():
	cut = calorie_intake_calc(163.66,221.66,31,'F',0.15,'V')
	cut.amount_exercise = 'M'
	cut.age = 7
	cut.gender = 'F'

