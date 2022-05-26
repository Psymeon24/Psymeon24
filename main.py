class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self,change_name, change_age, add_tracks, get_score):
        self.change_name = change_name
        self.change_age = change_age
        self.add_tracks = add_tracks
        self.get_score = get_score

        
def get_score(Bob, get_score):
    return Bob.get_score

Bob = Student("Peter", "34", "UI/UX", "()")

print('Name=',Bob.change_name)
print('Age=',Bob.change_age)
print('Tracks=',Bob.add_tracks)
print('Score=',Bob.get_score)

pass



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()


      
