import pandas as pd
def add_del_skills(prskills,skills2):  #skill is the skills from dic  #1st function from app py file
    from pymongo import MongoClient

    db=MongoClient("localhost",27017)
    skillset=db.skills #db
    add=skillset.add_del_skills  #table
    skills={}
    skills["id"]=1
    skills["add_skills"]=prskills
    skills["delete_skills"]=skills2
    add.insert_one(skills) ##last execution     Finish of adding skill to db

def skilldoc(skills,skills2):   #first function used
    try:
        skill=[]
        skill.append(skills)
        skill.append(skills2)
        dataset=pd.read_csv(r"F:\skills_talentrecruit.csv")  #dataframe
        for i in skill[0].split(","):
           i=i.lower()
           dataset[i]=" "

        for k in skill[1].split(","):
            k=k.lower()
            dataset=dataset.drop(k,axis=1)
    except:
        return "error"
    dataset.to_csv(r"F:\skills_talentrecruit.csv",index=False)
    return "thanks"
