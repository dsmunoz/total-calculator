class TestValidations:

    def test_param_integrity_missing_base_amount_key(self, client):
        headers = {'ip-client': '127.0.0.1'}
        response = client.get("/calculate-total?state=NY&type=normal&km=10", headers=headers)
        assert response.json['error']['description'] == "param base_amount is a mandatory"
        assert response.status_code == 422

    def test_param_integrity_missing_base_amount_value(self, client):
        headers = {'ip-client': '127.0.0.1'}
        response = client.get("/calculate-total?state=NY&type=normal&km=10&base_amount=", headers=headers)
        assert response.json['error']['description'] == "param base_amount shouldn't be empty"
        assert response.status_code == 422

    def test_valid_state(self, client):
        headers = {'ip-client': '127.0.0.1'}
        response = client.get("/calculate-total?state=NO&type=normal&km=10&base_amount=20", headers=headers)
        assert response.json['error']['description'] == "unsupported state"
        assert response.status_code == 422

    def test_valid_type(self, client):
        headers = {'ip-client': '127.0.0.1'}
        response = client.get("/calculate-total?state=CA&type=normal123&km=10&base_amount=20", headers=headers)
        assert response.json['error']['description'] == "unsupported type"
        assert response.status_code == 422

    def test_param_valid_number(self, client):
        headers = {'ip-client': '127.0.0.1'}
        response = client.get("/calculate-total?state=CA&type=normal&km=abc&base_amount=20", headers=headers)
        assert response.json['error']['description'] == "param km must be numeric"
        assert response.status_code == 422

    def test_invalid_ip(self, client):
        headers = {'ip-client': 'abc'}
        response = client.get("/calculate-total?state=CA&type=normal&km=10&base_amount=20", headers=headers)
        assert response.json['error']['description'] == "ip is not valid"
        assert response.status_code == 403

