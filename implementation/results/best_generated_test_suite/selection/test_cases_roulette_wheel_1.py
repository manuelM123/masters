from cut import *

def test_case_0():
	cut = calorie_intake_calc(66.91,156.02,60,'M',0.1,'M')
	cut.age = 45
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 182.33

def test_case_1():
	cut = calorie_intake_calc(188.05,184.86,30,'M',0.0,'V')
	cut.gender = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 201.61

