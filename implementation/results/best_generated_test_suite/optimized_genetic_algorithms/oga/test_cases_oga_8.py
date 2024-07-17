from cut import *

def test_case_0():
	cut = calorie_intake_calc(206.01,207.65,72,'M',-0.25,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.24
	cut.age = 83
	cut.gender = 'M'

def test_case_1():
	cut = calorie_intake_calc(186.51,218.03,23,'M',0.22,'N')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'E'

def test_case_2():
	cut = calorie_intake_calc(97.06,154.5,56,'F',-0.13,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 181.21
	cut.weight = 66.17
	cut.age = 67

def test_case_3():
	cut = calorie_intake_calc(92.64,176.25,52,'M',-0.24,'L')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 32
	cut.age = 76

