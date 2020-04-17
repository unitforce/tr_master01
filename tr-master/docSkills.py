import pandas as pd
def docSkills(skill):  #skill is the skills from dic  #1st function from app py file
    from pymongo import MongoClient

    db=MongoClient("localhost",27017)
    skillset=db.skills #db
    add=skillset.add_skills  #table
    skills={}
    skills["id"]=1
    skills["added_today"]=skill
    skills["total_skills_added"]=0
    add.insert_one(skills) ##last execution     Finish of adding skill to db

def skilldoc(skill):   #first function used

    dataset=pd.read_csv(r"C:\Users\abc\Desktop\UFT\tr-master\tr-master\skills_tr.csv")  #dataframe
    for i in skill.split():
        dataset[i]=" "

    dataset.to_csv(r"C:\Users\abc\Desktop\UFT\tr-master\tr-master\skills_tr.csv",index=False)

    
