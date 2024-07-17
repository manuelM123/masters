from cut import *

def test_case_0():
	cut = calorie_intake_calc(77.15,171.24,48,'M',-0.04,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 141.46

def test_case_1():
	cut = calorie_intake_calc(193.06,224.9,23,'M',0.49,'M')
	cut.age = 34
	cut.gender = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(168.15,218.05,21,'F',-0.0,'N')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'V'

def test_case_3():
	cut = calorie_intake_calc(136.78,148.55,41,'M',-0.39,'S')
	cut.height = 159.77

def test_case_4():
	cut = calorie_intake_calc(130.88,193.78,62,'F',-0.15,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 138.48

def test_case_5():
	cut = calorie_intake_calc(70.22,153.62,17,'N',0.33,'M')
	cut.bodyfat = 0.57
	cut.age = 31
	cut.gender = 'M'
	cut.bodyfat = 0.43

def test_case_6():
	cut = calorie_intake_calc(55.47,215.57,28,'F',0.37,'L')
	cut.weight = 135.47
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_7():
	cut = calorie_intake_calc(136.64,152.83,52,'F',0.21,'E')
	cut.gender = 'M'
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 62.0

def test_case_8():
	cut = calorie_intake_calc(102.07,197.73,53,'N',0.54,'E')
	cut.gender = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 153.07

def test_case_9():
	cut = calorie_intake_calc(177.97,207.64,23,'M',0.43,'L')

def test_case_10():
	cut = calorie_intake_calc(62.58,147.45,63,'F',-0.14,'V')
	cut.height = 217.34

def test_case_11():
	cut = calorie_intake_calc(206.81,214.12,26,'N',-0.17,'N')
	cut.age = 70

def test_case_12():
	cut = calorie_intake_calc(52.58,210.89,85,'N',-0.39,'V')

def test_case_13():
	cut = calorie_intake_calc(67.48,189.67,15,'M',0.03,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_14():
	cut = calorie_intake_calc(212.73,211.58,19,'F',0.3,'V')

def test_case_15():
	cut = calorie_intake_calc(95.49,187.57,48,'F',-0.45,'N')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 204.84
	cut.gender = 'F'

def test_case_16():
	cut = calorie_intake_calc(92.53,197.54,18,'M',0.06,'M')
	cut.bodyfat = -0.48
	cut.age = 20

def test_case_17():
	cut = calorie_intake_calc(182.07,222.03,27,'M',0.72,'N')
	cut.bodyfat = 0.38
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_18():
	cut = calorie_intake_calc(204.34,207.9,5,'F',0.18,'S')
	cut.age = 72
	cut.weight = 59.62
	cut.gender = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_19():
	cut = calorie_intake_calc(117.79,217.92,57,'N',-0.27,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 205.24

def test_case_20():
	cut = calorie_intake_calc(81.34,147.03,21,'M',-0.16,'V')
	cut.height = 167.75
	cut.age = 52
	cut.amount_exercise = 'E'
	result_tdee_calculation = cut.tdee_calculation()

def test_case_21():
	cut = calorie_intake_calc(139.48,215.68,69,'N',-0.34,'E')
	cut.gender = 'M'
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 21
	cut.bodyfat = 0.19

def test_case_22():
	cut = calorie_intake_calc(177.71,224.04,74,'M',0.67,'S')
	cut.gender = 'M'

def test_case_23():
	cut = calorie_intake_calc(134.88,215.91,63,'N',0.12,'S')
	cut.amount_exercise = 'N'
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 160.46
	result_tdee_calculation = cut.tdee_calculation()

def test_case_24():
	cut = calorie_intake_calc(114.4,218.4,21,'M',0.14,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'M'

