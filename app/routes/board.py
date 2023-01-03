from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.board import Board

bp = Blueprint("board_bp", __name__, url_prefix="/board")


@bp.route("", methods=["POST"])
def create_board():
    request_body = request.get_json()
    new_board = Board.from_dict(request_body)

    db.session.add(new_board)
    db.session.commit()

    board_dict = new_board.to_dict()

    return make_response(jsonify({"board": board_dict}), 201)

    # add a try/except later for missing data