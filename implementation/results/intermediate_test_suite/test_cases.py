from cut import *

def test_case_0():
	cut = calorie_intake_calc(63.68,180.6,45,'F',0.23,'S')
	result_tdee_calculation = cut.tdee_calculation()

def test_case_1():
	cut = calorie_intake_calc(190.45,177.62,46,'N',0.24,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(121.32,150.38,44,'M',0.18,'E')
	cut.height = 181.62

def test_case_3():
	cut = calorie_intake_calc(166.69,146.01,45,'N',0.09,'M')
	cut.age = 50

def test_case_4():
	cut = calorie_intake_calc(102.35,174.83,41,'N',0.08,'N')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

