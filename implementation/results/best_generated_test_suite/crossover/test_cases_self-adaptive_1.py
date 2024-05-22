from cut import *

def test_case_0():
	cut = calorie_intake_calc(179.23,187.42,65,'F',0.5,'M')
	cut.age = 20
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.78
	cut.gender = 'M'

def test_case_1():
	cut = calorie_intake_calc(85.92,196.85,69,'N',-0.33,'E')
	cut.gender = 'N'
	cut.amount_exercise = 'L'
	cut.height = 162.09

def test_case_2():
	cut = calorie_intake_calc(168.63,177.4,35,'F',0.02,'V')
	cut.gender = 'N'
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 222.15
	cut.age = 17
	cut.weight = 166.2
	cut.height = 223.6
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = -0.07
	cut.weight = 214.62
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_3():
	cut = calorie_intake_calc(136.08,163.96,58,'F',-0.33,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_4():
	cut = calorie_intake_calc(204.97,206.95,60,'N',0.29,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 85.16

def test_case_5():
	cut = calorie_intake_calc(153.16,147.57,59,'M',-0.26,'S')
	cut.height = 196.86
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 199.07
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = -0.28
	cut.age = 14
	cut.weight = 83.27
	cut.amount_exercise = 'V'

def test_case_6():
	cut = calorie_intake_calc(81.55,152.83,36,'F',-0.49,'M')
	cut.age = 42
	cut.amount_exercise = 'M'
	cut.bodyfat = 0.1
	cut.gender = 'N'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = -0.31
	cut.gender = 'M'

def test_case_7():
	cut = calorie_intake_calc(114.65,161.28,47,'N',0.66,'M')

def test_case_8():
	cut = calorie_intake_calc(114.65,161.28,47,'N',0.66,'M')

def test_case_9():
	cut = calorie_intake_calc(190.68,179.43,44,'F',0.12,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_10():
	cut = calorie_intake_calc(80.29,201.42,84,'M',0.32,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 206.89

def test_case_11():
	cut = calorie_intake_calc(187.04,169.78,6,'N',0.77,'M')
	cut.age = 64
	cut.bodyfat = 0.12

def test_case_12():
	cut = calorie_intake_calc(169.86,191.51,52,'N',0.31,'V')
	cut.weight = 108.59
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 119.32
	cut.height = 213.69

def test_case_13():
	cut = calorie_intake_calc(69.39,186.04,6,'F',-0.36,'M')

def test_case_14():
	cut = calorie_intake_calc(174.68,179.45,18,'F',0.13,'L')
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_15():
	cut = calorie_intake_calc(87.35,205.97,6,'F',0.43,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 185.75
	cut.bodyfat = -0.22
	cut.gender = 'N'
	cut.weight = 107.96
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 43.66
	cut.weight = 101.81
	cut.age = 36
	cut.amount_exercise = 'N'

def test_case_16():
	cut = calorie_intake_calc(40.56,166.47,37,'M',-0.1,'L')
	cut.amount_exercise = 'V'
	cut.height = 142.68
	result_tdee_calculation = cut.tdee_calculation()

def test_case_17():
	cut = calorie_intake_calc(146.29,224.44,69,'M',-0.14,'E')
	cut.height = 152.08
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 148.31
	cut.age = 33
	cut.bodyfat = 0.71

def test_case_18():
	cut = calorie_intake_calc(100.82,215.28,16,'F',-0.35,'E')
	cut.amount_exercise = 'L'
	cut.amount_exercise = 'M'
	cut.bodyfat = 0.21
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'V'
	cut.height = 152.08
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_19():
	cut = calorie_intake_calc(118.9,158.7,74,'N',-0.27,'N')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'N'
	cut.amount_exercise = 'N'
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = -0.49
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 44
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.52

def test_case_20():
	cut = calorie_intake_calc(61.67,181.45,34,'F',-0.32,'N')

def test_case_21():
	cut = calorie_intake_calc(133.17,146.61,43,'M',0.63,'M')
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 182.39
	cut.weight = 212.07
	cut.weight = 113.75
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 179.66
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_22():
	cut = calorie_intake_calc(41.27,142.02,77,'M',0.68,'V')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'N'
	cut.weight = 45.02
	cut.bodyfat = 0.22

def test_case_23():
	cut = calorie_intake_calc(149.63,176.87,18,'N',0.73,'E')
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 26

def test_case_24():
	cut = calorie_intake_calc(157.38,180.64,72,'M',0.47,'M')
	cut.bodyfat = 0.03
	cut.weight = 43.25
	cut.age = 47
	cut.age = 63
	cut.weight = 115.37
	cut.amount_exercise = 'M'
	cut.height = 203.66

def test_case_25():
	cut = calorie_intake_calc(115.19,136.5,79,'N',-0.02,'V')
	cut.gender = 'F'
	cut.weight = 192.67

def test_case_26():
	cut = calorie_intake_calc(70.28,192.44,17,'M',-0.43,'M')

