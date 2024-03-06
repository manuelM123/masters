from cut import *

def test_case_0():
	cut = calorie_intake_calc(187.0,153.54,13,'M',0.27,'N')
	cut.weight = 149.34

def test_case_1():
	cut = calorie_intake_calc(97.7,190.12,35,'M',0.28,'L')
	cut.weight = 87.86
	cut.weight = 168.69

def test_case_2():
	cut = calorie_intake_calc(169.34,147.8,28,'F',0.18,'V')
	cut.amount_exercise = 'S'

def test_case_3():
	cut = calorie_intake_calc(189.35,191.67,33,'N',0.15,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()

