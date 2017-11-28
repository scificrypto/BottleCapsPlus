from jsonrpc import JSONRPCException, ServiceProxy

MaxProcessSum = 200000   # Maximum amount of coins to merge
MaxOutputSum = 500       # Maximum transaction value
MinInputSum = 50         # Minimum input value, inputs with lower size will be ignored

access = ServiceProxy("http://alex:12345@127.0.0.1:7702")   # http://username:password@host:port/

try:
    balance = access.getbalance()
    print 'Balance = ', balance

    if balance > MaxProcessSum:
        print 'Balance is above MaxProcessSum, setting amount to ', MaxProcessSum
        balance = MaxProcessSum

        if balance > MaxOutputSum:
            access.mergecoins(balance, MinInputSum, MaxOutputSum)
except JSONRPCException,e:
    print 'Error: %s' % e.error
