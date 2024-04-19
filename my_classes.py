class Person():
    def __int__ (self, first_name, last_name, sex, age_years, __dict__):
        self.first_name= first_name
        self.last_name= last_name
        self.sex = sex
        self.age_years= age_years
        self.__dict__= dict

    def estimate_max_hr(self):
        if self.sex =="m":
            max_hr_bpm = 223 -0.9 * self.age
        elif self.sex == "f":
            max_hr_bpm = 226 -1.0 *self.age
        else:
            max_hr_bpm = input("Gib deine maxHr ein:")
        return int(max_hr_bpm)
    
    def save(self,filename):
        data= self.__dict__
        with open (filename, "w") as file:
            json.dump(data,file)

class Experiment():
    def __int__ (self,experiment_name, date, supervisor, subject, __dict1__):
        self.experiment_name = experiment_name
        self.date = date
        self.supervisor = supervisor
        self.subjct = subject
        self.__dict1__ = __dict1__
    
    def save(self,filename):
        data= self.__dict__
        with open (filename, "w") as file:
            json.dump(data,file)