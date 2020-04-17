import pandas as pd
def add_del_skills(skills,skills2):  #skill is the skills from dic  #1st function from app py file
    from pymongo import MongoClient

    db=MongoClient("localhost",27017)
    skillset=db.skills #db
    add=skillset.add_del_skills  #table
    skills={}
    skills["id"]=1
    skills["add_skills"]=skills
    skills["delete_skills"]=skills2
    add.insert_one(skills) ##last execution     Finish of adding skill to db

def skilldoc(skills,skills2):   #first function used

    dataset=pd.read_csv(r"C:\Users\abc\Desktop\UFT\tr-master\tr-master\skills_tr.csv")  #dataframe
    for i in skill.split():
        dataset[i]=" "
    dataset.to_csv(r"C:\Users\abc\Desktop\UFT\tr-master\tr-master\skills_tr.csv",index=False)


    dataset2=pd.read_csv(r"C:\Users\abc\Desktop\UFT\tr-master\tr-master\skills_tr.csv")  #dataframe
    for i in skill2.split():

        dataset2.drop([i])
    dataset2.to_csv(r"C:\Users\abc\Desktop\UFT\tr-master\tr-master\skills_tr.csv",index=False)
