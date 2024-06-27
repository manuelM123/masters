from cut import *

def test_case_0():
	cut = calorie_intake_calc(179.23,166.39,54,'M',-0.4,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 195.19
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_1():
	cut = calorie_intake_calc(201.84,199.07,52,'F',0.42,'N')
	cut.gender = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(190.92,162.16,26,'F',-0.22,'M')

def test_case_3():
	cut = calorie_intake_calc(77.58,199.29,65,'N',0.61,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'F'

def test_case_4():
	cut = calorie_intake_calc(205.68,196.03,54,'F',0.17,'E')
	cut.amount_exercise = 'E'
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_5():
	cut = calorie_intake_calc(112.52,207.44,45,'M',0.14,'M')
	cut.age = 68
	cut.amount_exercise = 'L'
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_6():
	cut = calorie_intake_calc(47.09,190.33,52,'F',-0.32,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 45

def test_case_7():
	cut = calorie_intake_calc(65.93,186.85,17,'F',-0.1,'E')
	cut.bodyfat = 0.56
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_8():
	cut = calorie_intake_calc(57.66,203.39,55,'M',-0.21,'L')
	cut.weight = 209.05
	result_tdee_calculation = cut.tdee_calculation()

def test_case_9():
	cut = calorie_intake_calc(65.93,186.85,17,'F',-0.1,'E')
	cut.bodyfat = 0.56
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_10():
	cut = calorie_intake_calc(49.06,137.66,14,'F',0.79,'N')
	cut.gender = 'N'
	cut.height = 198.05
	cut.age = 50

def test_case_11():
	cut = calorie_intake_calc(148.79,196.56,55,'N',0.76,'V')
	cut.height = 191.92
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_12():
	cut = calorie_intake_calc(181.68,217.83,70,'M',0.32,'L')
	cut.bodyfat = -0.31
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_13():
	cut = calorie_intake_calc(194.14,208.77,15,'N',-0.09,'N')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_14():
	cut = calorie_intake_calc(150.12,187.89,73,'N',0.71,'M')
	cut.age = 31
	result_tdee_calculation = cut.tdee_calculation()

def test_case_15():
	cut = calorie_intake_calc(127.68,145.37,72,'M',0.06,'V')
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_16():
	cut = calorie_intake_calc(136.72,169.45,23,'F',0.28,'M')
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 210.31
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.66

def test_case_17():
	cut = calorie_intake_calc(133.97,208.73,68,'N',0.05,'S')
	cut.gender = 'F'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_18():
	cut = calorie_intake_calc(151.26,147.74,81,'F',0.17,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'
	cut.weight = 94.6
	cut.gender = 'M'

def test_case_19():
	cut = calorie_intake_calc(96.31,220.98,56,'F',-0.19,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_20():
	cut = calorie_intake_calc(147.35,174.89,39,'F',0.74,'S')
	result_tdee_calculation = cut.tdee_calculation()

def test_case_21():
	cut = calorie_intake_calc(164.19,187.78,75,'F',0.33,'M')
	cut.amount_exercise = 'M'

def test_case_22():
	cut = calorie_intake_calc(166.22,141.75,61,'F',0.06,'N')
	cut.weight = 44.0
	cut.gender = 'F'
	cut.weight = 212.1
	cut.amount_exercise = 'M'

def test_case_23():
	cut = calorie_intake_calc(40.43,205.05,46,'N',0.71,'E')
	cut.weight = 37.5
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'M'
	cut.age = 5

def test_case_24():
	cut = calorie_intake_calc(194.13,180.57,54,'M',0.47,'L')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

