from cut import *

def test_case_0():
<<<<<<< Updated upstream
	cut = calorie_intake_calc(185.47,180.11,38,'F',0.16,'N')
	result_tdee_calculation = cut.tdee_calculation()

def test_case_1():
	cut = calorie_intake_calc(150.62,205.66,67,'F',0.26,'V')
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
=======
	cut = calorie_intake_calc(210.31,210.64,20,'F',0.26,'S')
	cut.age = 24
	cut.weight = 52.5
	result_tdee_calculation = cut.tdee_calculation()

def test_case_1():
	cut = calorie_intake_calc(93.11,195.2,30,'M',0.18,'N')

def test_case_2():
	cut = calorie_intake_calc(157.25,148.47,49,'F',0.04,'L')
	cut.height = 150.31
>>>>>>> Stashed changes

