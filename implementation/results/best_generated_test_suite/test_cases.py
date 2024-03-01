from cut import *

def test_case_0():
	cut = calorie_intake_calc(161.13,218.34,50,'F',0.24,'M')
	cut.gender = 'F'
	cut.age = 73

def test_case_1():
	cut = calorie_intake_calc(192.45,166.01,60,'N',0.27,'S')

def test_case_2():
	cut = calorie_intake_calc(69.02,141.77,74,'M',0.15,'E')
	cut.amount_exercise = 'S'
	cut.bodyfat = 0.25
	cut.bodyfat = 0.14

def test_case_3():
	cut = calorie_intake_calc(139.4,220.61,26,'F',0.24,'E')

