def estimate_max_hr(age_years: int , sex: str) -> int:
 
  if sex == "m":
    max_hr_bpm =  223 - 0.9 * age_years
  elif sex == "f":
    max_hr_bpm = 226 - 1.0 *  age_years
  else:
    # der input() öffnet ein Eingabefenster für den Nutzer und speichert die Eingabe
    max_hr_bpm  = input("Enter maximum heart rate:")
  return int(max_hr_bpm)

def build_person(first_name, last_name, sex, age_years) -> dict:
    """Returns a dictionary of information about a supervisor or subject."""
    dict = { "first_name" : first_name,
             "last_name" : last_name,
             "sex": sex,
             "age_years" : age_years,
             "estimate_max_hr" : estimate_max_hr(age_years,sex)}
    return dict

def build_experiment(experiment_name, date, supervisor, subject) -> dict:
    """Returns a dictionary of information about an experiment."""
    dict1 = {"experiment_name" : experiment_name,
            "date" : date,
            "supervisor" :   supervisor,
            "subject" :   subject,
           
            }
    return dict1
