import xmltodict

class PaymentApi:

    def payment_url(self):
        pass

    def parse(self):
        pass


class PaymentApiHandlerBase:

    def handle_ipay_request(self, request_body):
        req = xmltodict.parse(request_body).get('ServiceProvider_Request', {})
        request_type = req.get('RequestType')
        if request_type == 'ServiceInfo':
            response = self.get_service_info(req)
        full_response = dict(ServiceProvider_Response=response)
        return xmltodict.unparse(full_response, encoding='Windows-1251')

    def get_service_info(self, service_info_request):
        """
        Return a dictionary
        """
        return {}
