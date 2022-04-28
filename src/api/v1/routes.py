from flask import Blueprint, request, jsonify

from src.integration.house_canary import check_septic


blueprint = Blueprint("v1", __name__, url_prefix="/v1")
VALID_SEWER_RESPONSES = ["municipal", "storm", "septic", "none", "yes"]
VALID_SEPTIC_RESPONSES = ["septic"]
UNKNOWN_SEPTIC_RESPONSES = ["yes"]
NON_SEPTIC_RESPONSES = ["municipal", "storm", "none"]


@blueprint.route("/septic")
def septic():
    params = request.args.to_dict()

    if not params.get("address") or not params.get("zipcode"):
        return jsonify({"error": "Both the address and zipcode are required."}), 400

    data = check_septic(params.get("address"), params.get("zipcode"))

    if data not in VALID_SEWER_RESPONSES:
        return jsonify(data), 400

    if data in NON_SEPTIC_RESPONSES:
        return jsonify("No septic"), 200
    if data in UNKNOWN_SEPTIC_RESPONSES:
        return jsonify("Cannot determine septic"), 200

    return jsonify("Septic confirmed"), 200
