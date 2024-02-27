from cut import *

def test_case_0():
<<<<<<< Updated upstream
	cut = calorie_intake_calc(144.85,219.01,41,'F',0.28,'E')
	cut.height = 158.7
	cut.bodyfat = 0.18

def test_case_1():
	cut = calorie_intake_calc(118.7,161.37,38,'N',0.05,'S')
	cut.gender = 'M'
	cut.height = 153.43

def test_case_2():
	cut = calorie_intake_calc(175.09,220.59,21,'F',0.27,'S')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'E'
	cut.amount_exercise = 'L'

def test_case_3():
	cut = calorie_intake_calc(145.91,154.95,71,'N',0.27,'L')
	cut.bodyfat = 0.18
	cut.gender = 'F'

def test_case_4():
	cut = calorie_intake_calc(103.69,219.8,34,'F',0.15,'M')
	result_tdee_calculation = cut.tdee_calculation()
=======
	cut = calorie_intake_calc(105.19,167.88,46,'N',0.15,'L')

def test_case_1():
	cut = calorie_intake_calc(169.91,191.98,74,'N',0.19,'E')

def test_case_2():
	cut = calorie_intake_calc(123.06,206.3,41,'N',0.09,'V')

def test_case_3():
	cut = calorie_intake_calc(142.74,213.92,65,'F',0.15,'V')

def test_case_4():
	cut = calorie_intake_calc(165.38,185.68,17,'M',0.14,'N')

def test_case_5():
	cut = calorie_intake_calc(111.15,193.36,63,'M',0.05,'S')
	cut.weight = 193.4
	cut.gender = 'N'
	cut.age = 56

def test_case_6():
	cut = calorie_intake_calc(58.86,144.35,38,'N',0.26,'V')

def test_case_7():
	cut = calorie_intake_calc(43.98,154.54,63,'F',0.22,'V')
	cut.gender = 'F'
>>>>>>> Stashed changes

