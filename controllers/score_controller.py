from flask import request,jsonify
from models.score_model import ScoreModel

score_model = ScoreModel()

def add_scores():
    data = request.get_json()
    stu_id = data.get("stu_id")
    subj_id = data.get("subj_id")
    marks = data.get("marks")
    grades = data.get("grades")

    scores = score_model.add_score(stu_id,subj_id,marks,grades)
    return jsonify(scores)

def get_scores():
    scores = score_model.get_all_scores()
    return jsonify(scores)

def get_sco_by_id(sco_id):
    score = score_model.get_score_by_id(sco_id)

    if score:
        return jsonify(score)
    else:
        return("Record not found")
    
def update_sco_by_id(sco_id):
    data = request.get_json()
    stu_id = data.get("stu_id")
    subj_id = data.get("subj_id")
    marks = data.get("marks")
    grades = data.get("grades")

    score = score_model.update_score_by_id(sco_id,stu_id,subj_id,marks,grades)

    if score:
        return jsonify(score)
    else:
        return("Record not found")
    
def delete_sco_by_id(sco_id):
    return score_model.delete_score_by_id(sco_id)