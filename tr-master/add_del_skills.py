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

    dataset=pd.read_csv(r"F:\skills_talentrecruit.csv")  #dataframe
    for i in skills.split(" "):
        dataset[i]=" "
    dataset.to_csv(r"F:\skills_talentrecruit.csv",index=False)


    dataset2=pd.read_csv(r"F:\skills_talentrecruit.csv")  #dataframe
    for i in skills2.split(" "):
	
        dataset2.drop(i,axis=1)
    dataset2.to_csv(r"F:\skills_talentrecruit.csv",index=False)
