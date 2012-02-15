# tst class instance vs static vars
class Account(object):

    # class vars
    num_accounts = 0

    def __init__(self, name):
        self.name = name
        self.num_accounts += 1
        Account.num_accounts += 1
        


#  test code
    
if __name__ == '__main__':  
    
    print '>>> Begin <<<'
    a1 = Account('Fred')
    a2 = Account('Joe')
    print 'name: %s' % (a1.name)
    print 'name: %s' % (a2.name)
    print 'num accounts: %s' % (Account.num_accounts)
    print '>>> End <<<'
