home work:
# player has jarsey number name ,runs,wicket ,team name, it has all get and set method for every attribute .create team RCB with minimum5 players in it


# task1:display aall,baters frm team who scored more than 1000
# task2:display all ballers who took more than 20 wickets
# task:display all players name whose name consist letter "r"


class Player:
    teamname="RCB"
    def __init__(self,n,jn,r,w):
        self.name=n
        self.jersey_no=jn
        self.runs=r
        self.wicket=w
    
    def getname(self):
        return self.name
    def setname(self,n):
        self.name=n

    def getjerseyno(self):
        return self.jersey_no
    def setjerseyno(self,jn):
        self.jersey_no=jn
        
    def getruns(self):
        return self.runs
    def setruns(self, r):
        self.runs = r
    
    def getwicket(self):
        return self.wicket
    def setwicket(self,w):
        self.wicket=w
    
    @classmethod
    def setteam(cls, tn):
        cls.teamname = tn
    def getteam(cls):
        return cls.teamname
    
    def __str__(self):
         return f"Name :{self.name} , Jersey_No :{self.jersey_no} , Total Runs :{self.runs} , Total Wickets :{self.wicket} , Team Name :{Player.teamname}"
ipl2025={
"RCB":[
Player("Virat Kohli",18,657,0),  
Player("Rajat Patidar",97,312,0), 
Player("Jitesh Sharma",55,0,1) ,
Player("devdutt padikkal",38,0,8), 
Player("Faf du plessis",13,245,2),
Player("Phil Salt", 21, 387, 0),
Player("Josh Hazlewood", 11, 0,21),
Player("Tim David", 25, 188, 0),
Player("Bhuvneshwar Kumar", 15, 0,15),
Player("Krunal Pandya", 24, 0,15),
Player("Yash Dayal", 96, 0, 12)],

"MI":[Player("Rohit Sharma",45,418,0),
    Player("Suryakumar Yadav",63,717,0),
    Player("Tilak Varma",9,343,0),
    Player("Ryan Rickelton",44,388,0),
    Player("Hardik Pandya",33,0,12),
    Player("Trent Boult",18,0,22),
    Player("Jasprit Bumrah",93,0,9),
    Player("Deepak Chahar",56,0,8),
    Player("Mitchell Santner",74,0,0),
    Player("Will Jacks",22,233,0),
    Player("Naman Dhir",19,0,0),],
"CSK": [
Player("MS Dhoni", 7, 196, 0),
Player("Ravindra Jadeja", 8, 301, 10),
Player("Noor Ahmad", 15, 0, 24),
Player("Shivam Dube", 25, 357, 0),
Player("Matheesha Pathirana", 81, 0, 13),
Player("Ravichandran Ashwin", 99, 33, 7),
Player("Sam Curran", 58, 0, 0),
Player("Deepak Hooda", 57, 0, 0),
Player("Devon Conway", 88, 0, 0),
Player("Jamie Overton", 10, 0, 0),
Player("Rachin Ravindra", 17, 0, 0),],

"DC": [
    Player("KL Rahul",1,539,0),
    Player("Faf du Plessis",13,202,0),
    Player("Abishek Porel",24,301,0),
    Player("Tristan Stubbs",30,300,0),
    Player("Axar Patel",20,263,5),
    Player("Kuldeep Yadav",23,0,15),
    Player("Mitchell Starc",56,0,14),
    Player("Mukesh Kumar",49,0,12),
    Player("Vipraj Nigam",28,0,11),
    Player("Ashutosh Sharma",77,204,0),
    Player("Donovan Ferreira",10,1,0),],  
"GT":[
    Player("Sai Sudharsan",6,759,0),
    Player("Shubman Gill",77,650,0),
    Player("Jos Buttler",63,0,0),
    Player("Prasidh Krishna",24,0,25),
    Player("Rashid Khan",19,0,0),
    Player("Rahul Tewatia",4,0,0),
    Player("Shahrukh Khan",17,0,0),
    Player("Washington Sundar",5,0,0),
    Player("Gerald Coetzee",62,0,0),
    Player("Mohammed Siraj",13,0,0),
    Player("Kusal Mendis",11,0,0),],
"KKR": [
    Player("Ajinkya Rahane",3,0,0),
    Player("Quinton de Kock",7,0,0),
    Player("Andre Russell",12,167,8),
    Player("Venkatesh Iyer",25,0,0),
    Player("Rinku Singh",35,206,0),
    Player("Sunil Narine",74,0,0),
    Player("Manish Pandey",9,92,0),
    Player("Angkrish Raghuvanshi",18,300,0),
    Player("Anrich Nortje",2,0,0),
    Player("Varun Chakravarthy",29,0,0),
    Player("Harshit Rana",22,0,0),],
"PBKS" : [
Player("Shreyas Iyer", 41, 604, 0),
Player("Prabhsimran Singh", 84, 599, 0),
Player("Priyansh Arya", 0, 545, 0),   
Player("Nehal Wadhera", 19, 369, 0),
Player("Shashank Singh", 28, 350, 0),
Player("Josh Inglis", 95, 278, 0),
Player("Marcus Stoinis", 17, 160, 0),
Player("Arshdeep Singh", 2, 0, 18),
Player("Azmatullah Omarzai", 23, 57, 0),
Player("Lockie Ferguson", 69, 4, 0),
Player("Yuzvendra Chahal", 3, 87, 0),],
"RR":
[Player("Yashasvi Jaiswal", 64, 559, 0),
    Player("Riyan Parag", 5, 393, 3),
    Player("Dhruv Jurel", 21, 333, 0),
    Player("Sanju Samson", 11, 285, 0),
    Player("Vaibhav Suryavanshi", 12, 252, 0),
    Player("Shimron Hetmyer", 14, 239, 0),
    Player("Nitish Rana", 10, 217, 0),
    Player("Maheesh Theekshana", 61, 10, 11),
    Player("Wanindu Hasaranga", 49, 9, 11),
    Player("Jofra Archer", 22, 63, 11),
    Player("Sandeep Sharma", 95, 6, 9)]
}
# Task1
print("Batsman with Runs below 1000 :" )
for t,p in ipl2025.items():
    for i in p:
        if i.getruns()<1000:
            print(f"Batsman Name: {i.getname()} , Team :{t} , Total Runs:{i.getruns()}")
print(" \n")
# Task2
print("Players who has taken wickets more than 20 :")
for t,p in ipl2025.items():
    for j in p:
        if j.getwicket()>20:
            print(f"Bowler Name:{j.getname()} , Team Name:{t} , Total wickets:{j.getwicket()}")
    

print(" \n")

# Task3
print("players having letter 'r' in there name :")
for t,p in ipl2025.items():
    for i in p:
        if "r" in i.getname():
            print(f"Name :{i.getname()} , Jersey_No :{i.getjerseyno()} , Total Runs :{i.getruns()} , Total Wickets :{i.getwicket()} , Team Name :{t}")
        