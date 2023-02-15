import ipaddress

class Validator:

    ALLOWED_STATES = [
        'NY',
        'CA',
        'AZ',
        'TX',
        'OH'
    ]

    ALLOWED_ESTIMATION_TYPES = [
        'normal',
        'premium'
    ]

    MANDATORY_PARAMETERS = [
        'km',
        'type',
        'base_amount',
        'state',
    ]

    NUMBER_PARAMETERS = [
        'km',
        'base_amount'
    ]

    def validate(self, params, ip):
        self.validate_ip(ip)
        self.validate_params_integrity(params)
        self.validate_state(params['state'])
        self.validate_type(params['type'])
        self.validate_numbers(params)

    def validate_params_integrity(self, params):
        params_sent = list(params.keys())
        for param in self.MANDATORY_PARAMETERS:
            if param not in params_sent:
                raise Exception("param "+param+" is a mandatory")
            if params[param] == '':
                raise Exception("param "+param+" shouldn't be empty")

    def validate_state(self, state:str):
        if state.upper() not in self.ALLOWED_STATES:
            raise Exception('unsupported state')

    def validate_type(self, type:str):
        if type.lower() not in self.ALLOWED_ESTIMATION_TYPES:
            raise Exception('unsupported type')

    def validate_ip(self, ip):
        try:
            ipaddress.ip_address(ip)
        except ValueError:
            raise Exception("ip is not valid")

    def validate_numbers(self, params):
        for param in self.NUMBER_PARAMETERS:
            if not params[param].isnumeric():
                try:
                    float(params[param])
                except ValueError:
                    raise Exception("param "+param+" must be numeric")

