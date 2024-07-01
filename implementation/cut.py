class calorie_intake_calc:
    '''
    A class used to calculate the calorie intake of a person given a set of parameters

    Attributes
    ----------
    weight : float
        weight of the person in kg in the interval [40,200]
    height : float
        height of the person in cm in the interval [140,210]
    age : int
        age of the person in years in the interval [10,80]
    gender : str
        person gender, either male 'M' or female 'F'
    bodyfat : float
        bodyfat percentage of the person in the interval [0,0.3]
    amount_exercise : str
        amount of exercise the person does, either sedentary 'S', light 'L', moderate 'M', very active 'V' or extra active 'E'

    Methods
    -------
    mifflin_stjeor_equation()
        Calculates the calorie intake of a person using the Mifflin-St Jeor equation
        This equation calculates basic metabolic rate (BMR) which is the amount of energy expended while at rest

    katch_mcardle_equation()
        Calculates the calorie intake of a person using the Katch-McArdle equation (BMR)
        This equation calculates basic metabolic rate (BMR) which is the amount of energy expended while at rest

    tdee_calculation()
        Calculates the Total Daily Energy Expenditure (TDEE) of a person which is the amount of energy expended per day
        This is used to calculate the calorie intake of a person needed to maintain their current weight. It evaluates the amount of exercise a person does and multiplies the BMR by a factor
        to get the Total Daily Energy Expenditure (TDEE).

    determine_calorie_intake()
        Calculates the calorie intake of a person given their TDEE and the amount of weight they want to lose, maintain or gain per week.
    '''
    def __init__(self, weight, height, age, gender, bodyfat, amount_exercise):
        self.weight = weight
        self.height = height
        self.age = age
        self.gender = gender
        self.bodyfat = bodyfat
        self.amount_exercise = amount_exercise

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if height < 140 or height > 220:
            raise ValueError("Height cannot be below 140cm or above 210cm")
        self.__height = height

    @property
    def weight(self):
        return self.__weight
    
    @weight.setter
    def weight(self, weight):
        if weight < 40 or weight > 210:
            raise ValueError("Weight cannot be below 40kg or above 210kg")
        self.__weight = weight 

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        if age < 10 or age > 80:
            raise ValueError("Age cannot be below 10 or above 80")
        self.__age = age
    
    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender: str):
        self.__gender = gender

    @property
    def bodyfat(self):
        return self.__bodyfat

    @bodyfat.setter
    def bodyfat(self, bodyfat):
        if bodyfat > 0.3:
                raise ValueError('Bodyfat cannot be higher than 0.3')
        self.__bodyfat = bodyfat

    @property
    def amount_exercise(self):
        return self.__amount_exercise
    
    @amount_exercise.setter
    def amount_exercise(self, amount_exercise: str):
        self.__amount_exercise = amount_exercise
        
    '''
    A method used to calculate the calorie intake of a person using the Mifflin-St Jeor equation

    Parameters
    ----------
    weight : float
        weight of the person in kg
    height : float
        height of the person in cm
    age : int
        age of the person in years
    gender : str   
        person gender, either male 'M' or female 'F'

    Returns
    -------
    float
        calorie intake of the person in kcal/day
    '''
    def mifflin_stjeor_equation(self):
        if self.gender.upper() == 'F':
            return (10 * self.weight) + (6.25 * self.height) - (5 * self.age) - 161
        elif self.gender.upper() == 'M':
            return (10 * self.weight) + (6.25 * self.height) - (5 * self.age) + 5
        else:
            raise ValueError('Gender is not specified correctly')
        
    '''
    A method used to calculate the calorie intake of a person using the Katch-McArdle equation using the bodyfat percentage and
    the weight of the person
    '''
    def katch_mcardle_equation(self):
        return round(370 + (21.6 * ((1 - self.bodyfat) * self.weight)),2)
    
    '''
    A method used to calculate the Total Daily Energy Expenditure (TDEE) of a person which is the amount of energy expended per day
    This is used to calculate the calorie intake of a person needed to maintain their current weight. It evaluates the amount of exercise a person does and multiplies the BMR by a factor
    to get the Total Daily Energy Expenditure (TDEE).

    Attributes
    ----------
    bmr : float
        basic metabolic rate (BMR) of the person in kcal/day

    amount_exercise : str
        amount of exercise the person does, either sedentary 'S', light 'L', moderate 'M', very active 'V' or extra active 'E'
        sedentary (S)  = little or no exercise
        light (L) = light exercise/sports 1-3 days/week
        moderate (M) = moderate exercise/sports 3-5 days/week
        very active (V) = hard exercise/sports 6-7 days a week
        extra active (E) = very hard exercise/sports and physical job or 2x training

    Returns
    -------
    float which is the TDEE of the person in kcal/day
    '''
    def tdee_calculation(self): 
        # Bodyfat negative values are considered as the person does not know their bodyfat percentage
        if self.bodyfat < 0:
            bmr = self.mifflin_stjeor_equation()
        else:
            bmr = self.katch_mcardle_equation()

        if self.amount_exercise.upper() == 'S':
            return bmr * 1.2
        elif self.amount_exercise.upper() == 'L':
            return bmr * 1.375
        elif self.amount_exercise.upper() == 'M':
            return bmr * 1.55
        elif self.amount_exercise.upper() == 'V':
            return bmr * 1.725
        elif self.amount_exercise.upper() == 'E':
            return bmr * 1.9
        else:
            raise ValueError('Exercise amount not specified correctly. The amount of exercise must be either sedentary (S), light (L), moderate (M), very active (V) or extra active (E)')
        
    '''
    For a person to lose weight, they must be in a calorie deficit which means they must consume less calories than they expend which value recommend by the NHS is 600 kcal/day
    below the TDEE. This method calculates the calorie intake of a person given their TDEE and the amount of weight they want to lose per week.

    For a person to gain weight, they must be in a calorie surplus which means they must consume more calories than they expend which value recommend by the NHS is 600 kcal/day 
    above the TDEE. This method calculates the calorie intake of a person given their TDEE and the amount of weight they want to gain per week.

    The function uses the TDEE to calculate the calorie intake of a person to lose, mantain or gain weight. 
    
    The function returns a list of 3 values which are the calorie intake of a person to lose weight, maintain weight or gain weight respectively.

    Returns
    -------
    list of 3 floats which are the calorie intake of a person to lose weight, maintain weight or gain weight respectively.
    '''
    def determine_calorie_intake(self):
        tdee = self.tdee_calculation()
        return "Calories intake to lose weight = " + str(round(tdee - 600,2)) + " kcal/day" + "\n" + \
               "Calories intake to maintain weight = " + str(round(tdee,2)) + " kcal/day" + "\n" + \
               "Calories intake to gain weight = " + str(round(tdee + 600,2)) + " kcal/day"