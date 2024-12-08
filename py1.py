import requests as r

class Fetcher:
    def __init__(self):
        self.studentslist = r.get("https://cdn.ituring.ir/ex/users.json").json()
     
    def getst(self):
        return self.studentslist

    def nerds(self):
        return {students.get('name' , '') + " " + students.get('last_Name' , "")
                for students in self.studentslist
                if students.get('score') > 18.5}

    def sultans(self):
        maxscore = max(students.get('score')
                for students in self.studentslist)
        return(students.get('name', '') + " " + students.get('last_Name', '')
                for students in self.studentslist 
                if students.get('score') == maxscore
    )
    def mean(self):
        scores = [students.get('score')
       for students in self.studentslist]
        return sum(scores) / len(scores)
    
    def get_students(self):
          return [
            {dict: students[dict] 
            for dict in students
            if dict not in ['city', 'province', 'latitude']}
            for students in self.studentslist
        ]
f = Fetcher()

print(f.nerds())
print(f.sultans())
print(f.mean())
print(f.get_students())
