from flask import Blueprint
from controllers import score_controller

score_app = Blueprint("score_app", __name__)


@score_app.route("/addscores", methods = ['POST'])
def add_scores():
   return score_controller.add_scores()

@score_app.route("/getscores",methods = ['GET'])
def get_all_scores():
   return score_controller.get_scores()

@score_app.route("/getscore/<int:sco_id>",methods = ['GET'])
def get_score_by_id(sco_id):
   return score_controller.get_sco_by_id(sco_id)

@score_app.route("/updatescore/<int:sco_id>",methods = ['PUT'])
def update_score_by_id(sco_id):
   return score_controller.update_sco_by_id(sco_id)

@score_app.route("/deletescore/<int:sco_id>",methods = ['DELETE'])
def delete_score_by_id(sco_id):
   return score_controller.delete_sco_by_id(sco_id)
