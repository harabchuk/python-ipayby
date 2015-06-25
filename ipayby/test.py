__author__ = 'aliaksei'
from xmltodict import parse, unparse
from untangle import parse as uparse
from pprint import pprint

xml = """<?xml version="1.0" encoding="windows-1251" ?>
<ServiceProvider_Request>
<Version>1</Version>
<RequestType>TransactionResult</RequestType>
<DateTime>20090124155800</DateTime>
<PersonalAccount>123</PersonalAccount>
<Currency>974</Currency>
<RequestId>9221</RequestId>
<Info xml:space="preserve">
<InfoLine>aaaaaaaaaa</InfoLine>
<InfoLine>vvvvvvvv</InfoLine>
<InfoLine>ddddddd</InfoLine>
</Info>
<TransactionResult>
<TransactionId>6180433</TransactionId>
<ServiceProvider_TrxId>8571502</ServiceProvider_TrxId>
</TransactionResult>
</ServiceProvider_Request>
"""


if __name__ == "__main__":
    o = uparse(xml)
    #print o.ServiceProvider_Request.Version.cdata
    req = parse(xml)
    pprint(req, indent=3)
    #xml = unparse(dict(ServiceProvider_Response='aa'))
    #print xml
    #print req['ServiceProvider_Request']['Version']

