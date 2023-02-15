import json
import os.path


class Processor:
  def __init__(self):
    self.COMISSION_PERCENTAGES = json.load(open(os.path.dirname(__file__) + '/../comission_percentages.json'))
    self.total_amount = 0

  def process_discount_object(self, state: str, base_amount: float, km: float, discount_object_key: str) -> float:
    state_object = self.COMISSION_PERCENTAGES[state]
    if state_object[discount_object_key] != 'N/A':
      return self.calculate_discount(state_object[discount_object_key], km, base_amount)
    return float(base_amount)

  def calculate_discount(self, discount_object, km: float, base: float) -> float:
    keys = list(discount_object.keys())
    if keys[0] == 'between':
      if float(discount_object["between"][0]) <= km <= float(discount_object["between"][1]):
        return base - (base * float(discount_object["discount"]))
    if keys[0] == '=':
      if float(discount_object["="]) == km:
        return base - (base * float(discount_object["discount"]))
    if keys[0] == '>':
      if float(discount_object[">"]) < km:
        return base - (base * float(discount_object["discount"]))
    if keys[0] == '<':
      if float(discount_object["<"]) > km:
        return base - (base * float(discount_object["discount"]))
    return base

  def calculate_iva(self, total, state):
    return total * float(self.COMISSION_PERCENTAGES[state]['iva'])

  def process_total(self, args):

    base_with_discount = float(args["base_amount"])
    # discounts only apply for normal types
    if args["type"] == "normal":
      base_with_discount = self.process_discount_object(args['state'], float(args['base_amount']), float(args['km']),
                                                        'base_discount')
    comission = self.calculate_comission(base_with_discount, args['state'], args['type'])
    # calculation remains the same no matter the type
    self.total_amount = comission + base_with_discount
    iva = self.calculate_iva(self.total_amount, args['state'])
    self.total_amount = self.total_amount + iva

    # discounts only apply for normal types
    if args["type"] == "normal":
      self.total_amount = self.process_discount_object(args['state'], self.total_amount, float(args['km']),
                                                       'total_discount')
    if args["type"] == "premium" and float(args['km']) > 25:
      self.total_amount = self.total_amount - (float(self.total_amount) * .05)

    return self.total_amount

  def calculate_comission(self, base, state, type) -> float:
    return float(base) * float(self.COMISSION_PERCENTAGES[state][type])
