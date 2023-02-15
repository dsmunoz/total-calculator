import json
import os.path


class TestSuccess:

  def test_ny_normal(self, client):
    headers = {'ip-client': '127.0.0.1'}
    response = client.get("/calculate-total?state=NY&type=normal&km=10&base_amount=10", headers=headers)
    comission_percentages = json.load(open(os.path.dirname(__file__) + '/../comission_percentages.json'))
    comission = float(10) * float(comission_percentages['NY']['normal'])
    base_with_comission = comission + float(10)
    total_amount = base_with_comission + (base_with_comission * .21)
    assert response.status_code == 200
    assert response.json['total_amount'] == total_amount
    assert list(response.json.keys())[0] == 'date_requested'

  def test_ny_premium_discount(self, client):
    headers = {'ip-client': '127.0.0.1'}
    response = client.get("/calculate-total?state=NY&type=premium&km=26&base_amount=10", headers=headers)
    comission_percentages = json.load(open(os.path.dirname(__file__) + '/../comission_percentages.json'))
    comission = float(10) * float(comission_percentages['NY']['premium'])
    base_with_comission = comission + float(10)
    total_amount = base_with_comission + (base_with_comission * .21)
    total_amount_discount = total_amount - (total_amount * .05)
    assert response.status_code == 200
    assert response.json['total_amount'] == total_amount_discount
    assert list(response.json.keys())[0] == 'date_requested'

  def test_ny_premium_no_discount(self, client):
    headers = {'ip-client': '127.0.0.1'}
    response = client.get("/calculate-total?state=NY&type=premium&km=25&base_amount=10", headers=headers)
    comission_percentages = json.load(open(os.path.dirname(__file__) + '/../comission_percentages.json'))
    comission = float(10) * float(comission_percentages['NY']['premium'])
    base_with_comission = comission + float(10)
    total_amount = base_with_comission + (base_with_comission * .21)
    assert response.status_code == 200
    assert response.json['total_amount'] == total_amount
    assert list(response.json.keys())[0] == 'date_requested'

  def test_ca_normal_no_discount(self, client):
    headers = {'ip-client': '127.0.0.1'}
    response = client.get("/calculate-total?state=CA&type=normal&km=25&base_amount=10", headers=headers)
    comission_percentages = json.load(open(os.path.dirname(__file__) + '/../comission_percentages.json'))
    comission = float(10) * float(comission_percentages['CA']['normal'])
    total_amount = comission + float(10)
    assert response.status_code == 200
    assert response.json['total_amount'] == total_amount
    assert list(response.json.keys())[0] == 'date_requested'

  def test_az_normal_discount(self, client):
    headers = {'ip-client': '127.0.0.1'}
    response = client.get("/calculate-total?state=AZ&type=normal&km=27&base_amount=10", headers=headers)
    comission_percentages = json.load(open(os.path.dirname(__file__) + '/../comission_percentages.json'))
    comission = float(10) * float(comission_percentages['AZ']['normal'])
    total_amount = comission + float(10)
    total_amount_discount = total_amount - (total_amount * .05)
    assert response.status_code == 200
    assert response.json['total_amount'] == total_amount_discount
    assert list(response.json.keys())[0] == 'date_requested'

  def test_ca_premium_discount(self, client):
    headers = {'ip-client': '127.0.0.1'}
    response = client.get("/calculate-total?state=CA&type=premium&km=26&base_amount=10", headers=headers)
    comission_percentages = json.load(open(os.path.dirname(__file__) + '/../comission_percentages.json'))
    comission = float(10) * float(comission_percentages['CA']['premium'])
    total_amount = comission + float(10)
    total_amount_discount = total_amount - (total_amount * .05)
    assert response.status_code == 200
    assert response.json['total_amount'] == total_amount_discount
    assert list(response.json.keys())[0] == 'date_requested'

  def test_az_premium_no_discount(self, client):
    headers = {'ip-client': '127.0.0.1'}
    response = client.get("/calculate-total?state=AZ&type=premium&km=10&base_amount=10", headers=headers)
    comission_percentages = json.load(open(os.path.dirname(__file__) + '/../comission_percentages.json'))
    comission = float(10) * float(comission_percentages['AZ']['premium'])
    total_amount = comission + float(10)
    assert response.status_code == 200
    assert response.json['total_amount'] == total_amount
    assert list(response.json.keys())[0] == 'date_requested'

  def test_tx_normal_no_discount(self, client):
    headers = {'ip-client': '127.0.0.1'}
    response = client.get("/calculate-total?state=TX&type=normal&km=10&base_amount=10", headers=headers)
    comission_percentages = json.load(open(os.path.dirname(__file__) + '/../comission_percentages.json'))
    comission = float(10) * float(comission_percentages['TX']['normal'])
    total_amount = comission + float(10)
    assert response.status_code == 200
    assert response.json['total_amount'] == total_amount
    assert list(response.json.keys())[0] == 'date_requested'

  def test_tx_normal_max_discount(self, client):
    headers = {'ip-client': '127.0.0.1'}
    response = client.get("/calculate-total?state=TX&type=normal&km=31&base_amount=10", headers=headers)
    comission_percentages = json.load(open(os.path.dirname(__file__) + '/../comission_percentages.json'))
    comission = float(10) * float(comission_percentages['TX']['normal'])
    total_amount = comission + float(10)
    total_amount_discount = total_amount - (total_amount * .05)
    assert response.status_code == 200
    assert response.json['total_amount'] == total_amount_discount
    assert list(response.json.keys())[0] == 'date_requested'

  def test_oh_premium_discount(self, client):
    headers = {'ip-client': '127.0.0.1'}
    response = client.get("/calculate-total?state=TX&type=premium&km=31&base_amount=10", headers=headers)
    comission_percentages = json.load(open(os.path.dirname(__file__) + '/../comission_percentages.json'))
    comission = float(10) * float(comission_percentages['TX']['premium'])
    total_amount = comission + float(10)
    total_amount_discount = total_amount - (total_amount * .05)
    assert response.status_code == 200
    assert list(response.json.keys())[0] == 'date_requested'
    assert response.json['total_amount'] == total_amount_discount
