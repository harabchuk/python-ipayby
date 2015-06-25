__author__ = 'aliaksei'

from ipayby import PaymentApi, PaymentApiHandlerBase

class TestHandler(PaymentApiHandlerBase):

    def get_service_info(self, service_info_request):
        return {
            'Amount': {
                'Debt': 1000
            },
            'Info': {

            }


        }

