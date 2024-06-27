from cut import *

def test_case_0():
	cut = calorie_intake_calc(65.07,167.05,18,'N',0.46,'V')
	cut.weight = 212.16
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_1():
	cut = calorie_intake_calc(121.37,216.69,15,'M',0.0,'S')
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 47
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_2():
	cut = calorie_intake_calc(116.2,180.89,49,'F',-0.0,'S')
	cut.age = 22
	cut.weight = 155.33
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 156.22

def test_case_3():
	cut = calorie_intake_calc(152.19,180.62,59,'M',-0.4,'N')
	cut.age = 83
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = -0.27

def test_case_4():
	cut = calorie_intake_calc(110.12,209.15,25,'N',-0.49,'E')
	cut.height = 148.87
	cut.age = 44
	cut.bodyfat = 0.63
	cut.gender = 'M'

def test_case_5():
	cut = calorie_intake_calc(106.48,146.47,16,'F',0.65,'N')
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_6():
	cut = calorie_intake_calc(110.66,205.8,59,'N',0.52,'N')
	cut.bodyfat = -0.15
	cut.weight = 192.01
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_7():
	cut = calorie_intake_calc(59.71,136.96,23,'F',0.12,'L')
	cut.amount_exercise = 'E'
	cut.amount_exercise = 'E'

def test_case_8():
	cut = calorie_intake_calc(126.59,164.06,56,'M',-0.03,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_9():
	cut = calorie_intake_calc(194.66,148.72,36,'N',0.77,'M')
	cut.bodyfat = 0.02
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_10():
	cut = calorie_intake_calc(182.52,185.86,63,'M',0.26,'L')
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 29

def test_case_11():
	cut = calorie_intake_calc(199.64,142.96,55,'F',-0.42,'V')

def test_case_12():
	cut = calorie_intake_calc(212.18,183.48,47,'F',-0.1,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = -0.43
	cut.bodyfat = 0.08
	result_tdee_calculation = cut.tdee_calculation()

def test_case_13():
	cut = calorie_intake_calc(200.38,190.05,82,'F',-0.19,'V')
	cut.age = 62
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_14():
	cut = calorie_intake_calc(189.09,183.35,51,'N',0.4,'M')
	result_tdee_calculation = cut.tdee_calculation()

def test_case_15():
	cut = calorie_intake_calc(93.29,159.28,58,'M',0.33,'S')
	cut.gender = 'M'
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = -0.39
	cut.gender = 'M'

def test_case_16():
	cut = calorie_intake_calc(169.04,176.07,67,'N',0.37,'E')
	cut.height = 203.49
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'M'
	cut.age = 83

def test_case_17():
	cut = calorie_intake_calc(138.07,179.79,35,'M',-0.49,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 36.59
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 62.54

def test_case_18():
	cut = calorie_intake_calc(214.12,144.82,7,'N',-0.47,'N')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_19():
	cut = calorie_intake_calc(87.82,186.86,34,'M',-0.28,'V')
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 152.79
	result_determine_calorie_intake = cut.determine_calorie_intake()

