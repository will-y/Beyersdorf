class Resource():
    '''Class resource takes in a type of resource and the amount it has to store'''
    def __init__(self,type,amount):
        self.type = type
        self.amount = amount
    def edit(self,theAmount):
        '''Edits the amount of the resource that it is currently holding'''
        self.amount+=theAmount
    def set(self ,theAmount):
        '''Overwrites the current # of resources ont he tile'''
        self.amount=theAmount