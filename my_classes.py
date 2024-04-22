from datetime import datetime
import json

class Person():
    def __init__ (self, first_name, last_name):
        self.first_name= first_name
        self.last_name= last_name

    def save(self,filename):
        data= self.__dict__
        with open (filename, "w") as file:
            json.dump(data,file)

class Subject(Person):
    def __init__(self, first_name,last_name, sex, birthdate):
        super().__init__(first_name, last_name)
        self.__birthdate__ = birthdate
        self.sex = sex
        self.age_years = self.calculate_age()
        self.max_hr = self.estimate_max_hr()
    
    def calculate_age(self):
        today = datetime.today()
        birthdate = datetime.strptime(self.__birthdate__, "%d.%m.%Y").date()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return int(age)
    
    def estimate_max_hr(self):
        if self.sex =="m":
            max_hr_bpm = 223 -0.9 * self.age_years
        elif self.sex == "f":
            max_hr_bpm = 226 -1.0 * self.age_years
        else:
            max_hr_bpm = input("Gib deine maxHr ein:")
        return int(max_hr_bpm)

class Supervisor(Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)

class Experiment():
    def __init__ (self,experiment_name, date, supervisor, subject):
        self.experiment_name = experiment_name
        self.date = date
        self.supervisor = supervisor
        self.subject = subject
    
    def save(self,filename):
        data= self.__dict__
        with open (filename, "w") as file:
            json.dump(data,file)