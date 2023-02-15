from flask import Blueprint, request
from services.processor import Processor
from services.validator import Validator
import datetime

calculator = Blueprint('calculator', __name__)


@calculator.route('/calculate-total')
def total():
  args = request.args.to_dict()

  ip = request.headers.get('ip-client')
  v = Validator()
  p = Processor()
  try:
    v.validate(args, ip)
    total_amount = p.process_total(args)
    return {
      "total_amount": float(total_amount),
      "date_requested": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
  except Exception as e:
    status_code = 422
    if e.__str__() == "ip is not valid":
      status_code = 403

    request_error = {
      "error": {
        "description": e.__str__()
      }
    }
    return request_error, status_code
