from cut import *

def test_case_0():
	cut = calorie_intake_calc(120.04,193.78,38,'N',0.45,'N')
	cut.age = 58

def test_case_1():
	cut = calorie_intake_calc(185.14,208.62,71,'N',0.26,'L')
	cut.bodyfat = 0.51
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'E'

def test_case_2():
	cut = calorie_intake_calc(164.7,141.64,24,'M',-0.48,'M')
	result_tdee_calculation = cut.tdee_calculation()

def test_case_3():
	cut = calorie_intake_calc(153.96,194.97,12,'N',-0.15,'M')
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_4():
	cut = calorie_intake_calc(78.92,203.53,11,'F',-0.23,'V')
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 70.79
	cut.amount_exercise = 'N'

def test_case_5():
	cut = calorie_intake_calc(83.42,146.7,46,'N',-0.33,'V')
	cut.age = 64
	cut.bodyfat = 0.25

def test_case_6():
	cut = calorie_intake_calc(178.88,217.97,11,'F',0.22,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_7():
	cut = calorie_intake_calc(92.91,214.21,65,'N',-0.04,'S')
	cut.amount_exercise = 'N'

def test_case_8():
	cut = calorie_intake_calc(167.68,187.19,38,'N',0.14,'V')
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 40.37
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'E'

def test_case_9():
	cut = calorie_intake_calc(132.06,223.13,53,'F',0.06,'S')
	cut.weight = 124.46

def test_case_10():
	cut = calorie_intake_calc(168.78,180.6,9,'M',0.38,'S')
	cut.amount_exercise = 'S'
	cut.weight = 112.48

def test_case_11():
	cut = calorie_intake_calc(168.78,180.6,9,'M',0.38,'S')
	cut.amount_exercise = 'S'
	cut.weight = 112.48

def test_case_12():
	cut = calorie_intake_calc(40.79,220.46,40,'M',0.51,'S')
	cut.amount_exercise = 'S'
	cut.gender = 'F'

def test_case_13():
	cut = calorie_intake_calc(62.47,184.93,51,'F',0.44,'N')
	result_tdee_calculation = cut.tdee_calculation()

def test_case_14():
	cut = calorie_intake_calc(85.38,205.25,73,'N',0.39,'E')

def test_case_15():
	cut = calorie_intake_calc(212.31,172.34,81,'F',0.1,'L')
	cut.weight = 73.72
	cut.gender = 'N'

def test_case_16():
	cut = calorie_intake_calc(86.16,211.25,35,'M',0.17,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'M'
	cut.gender = 'N'

def test_case_17():
	cut = calorie_intake_calc(108.22,203.82,74,'F',-0.03,'S')
	cut.weight = 198.58
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'M'
	cut.bodyfat = 0.1

def test_case_18():
	cut = calorie_intake_calc(191.46,171.43,37,'N',0.13,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 142.16

def test_case_19():
	cut = calorie_intake_calc(153.74,214.27,53,'F',0.46,'N')
	cut.amount_exercise = 'S'
	cut.weight = 179.88
	cut.bodyfat = 0.04
	cut.height = 175.39

def test_case_20():
	cut = calorie_intake_calc(142.91,175.91,33,'F',0.25,'S')
	cut.height = 188.91
	cut.bodyfat = 0.23

def test_case_21():
	cut = calorie_intake_calc(192.66,192.08,71,'M',-0.46,'V')
	cut.height = 135.21

