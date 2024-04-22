import json

class Person():
    def __init__ (self, first_name, last_name, sex, age_years):
        self.first_name= first_name
        self.last_name= last_name
        self.sex = sex
        self.age_years= int(age_years)
        self.max_hr_bpm = self.estimate_max_hr()

    def estimate_max_hr(self):
        if self.sex =="m":
            max_hr_bpm = 223 -0.9 * self.age_years
        elif self.sex == "f":
            max_hr_bpm = 226 -1.0 * self.age_years
        else:
            max_hr_bpm = input("Gib deine maxHr ein:")
        return int(max_hr_bpm)
    
    def save(self,filename):
        data= self.__dict__
        with open (filename, "w") as file:
            json.dump(data,file)

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