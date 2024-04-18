from cut import *

def test_case_0():
	cut = calorie_intake_calc(99.5,183.07,60,'F',0.11,'M')
	cut.height = 165.79
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 178.34

def test_case_1():
	cut = calorie_intake_calc(136.54,163.58,55,'M',0.27,'V')
	cut.age = 55
	cut.height = 199.57
	cut.gender = 'F'
	cut.gender = 'M'

def test_case_2():
	cut = calorie_intake_calc(179.85,153.15,46,'F',0.21,'V')
	cut.height = 185.56
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_3():
	cut = calorie_intake_calc(49.03,214.23,11,'F',0.1,'S')

def test_case_4():
	cut = calorie_intake_calc(76.5,198.36,75,'M',0.01,'M')
	cut.height = 143.84
	cut.gender = 'N'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

