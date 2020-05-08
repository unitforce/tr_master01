def extract_skills(resume_text,fname,country,lname):
    import os
    import spacy
    import pandas as pd

    from rank_bm25 import BM25Okapi
    import csv

    from pymongo import MongoClient
    nlp = spacy.load('en_core_web_sm')
    nlp_text = nlp(resume_text)

    # removing stop words and implementing word tokenization

    # reading the csv file


    client=MongoClient("localhost",27017)
    db=client.Project
    #col=db.JD
    posts=db.post
    skill=[]
    for post in posts.find():
        skill.append(post)
    sh=[]
    for i in posts.find():
        des=i["skils"]
        sh.append(des)
    exp=[]
    i=0
    while (i<len(skill)):
        num=skill[i]["ExpRange"]
        e=num.split("-")[0]
        ae=num.split("-")[1]
        if (float(e)-1<float(lname)) and   (float(ae[1])>=float(lname)):
            exp.append(i)
        i+=1
    s=[]
    for i in exp:
        s.append(sh[i])
    sh=s
    def extract_skills(resume_text):
        nlp_text = nlp(resume_text)

        # removing stop words and implementing word tokenization
        tokens = [token.text for token in nlp_text if not token.is_stop]

        # reading the csv file
        with open(r"F:\skills_talentrecruit.csv", newline='') as f:
            reader = csv.reader(f)
            data = list(reader)
        skills=data[0]

        # extract values


        skillset = []

        # check for one-grams (example: python)
        for token in tokens:
            if token.lower() in skills:
                skillset.append(token)

        # check for bi-grams and tri-grams (example: machine learning)
        for token in nlp_text.noun_chunks:
            token = token.text.lower().strip()
            if token in skills:
                skillset.append(token)

        return [i.capitalize() for i in set([i.lower() for i in skillset])]
    skillset=extract_skills(resume_text)

    bmr=BM25Okapi(sh)
    result_jd=bmr.get_top_n(skillset,sh,n=3)
    result=bmr.get_scores(skillset)
    result=list(result)
    result1=result.copy()
    ra=result.index(max(result))
    result1.pop(ra)
    ra1=result1.index(max(result1))
    result1.pop(ra1)
    ma=max(result1)
    raaa=result.index(max(result1))
    import re
    r=re.compile(r"[\w\.-]+@[\w\.-]+")

    resume_email=r.findall(resume_text)
    skillset=",".join(skillset)


    raa={}
    raa["result"]=[{"description":skill[ra]["description"],"ApplicationURI":skill[ra]["ApplicationURI"],"id":skill[ra]["ID"],"match":result[ra]/result[ra],"jobtitle":skill[ra]["JobTitle"]},{"description":skill[ra1]["description"],"ApplicationURI":skill[ra1]["ApplicationURI"],"id":skill[ra1]["ID"],"jobtitle":skill[ra1]["JobTitle"],"match":result[ra1]/result[ra]},{"description":skill[raaa]["description"],"ApplicationURI":skill[raaa]["ApplicationURI"],"id":skill[raaa]["ID"],"match":ma/result[ra],"jobtitle":skill[raaa]["JobTitle"]}]
    raa["in"]=[{"name":fname,"loccati":country,"skills":skillset}]
    raa["em"]=[resume_email]
    return raa
