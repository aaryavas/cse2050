class Person():
    def __init__(self,name, netid):
        self.name = name
        self.netid = netid
    
    def __repr__(self):
        return f'Person: {self.name},{self.netid}'
class Employee(Person):
    def __init__(self, name, netid,office):
        #call previous class more mathemathical
        super().__init__(name,netid)
        #or but more simpleand more suceptibile to bugs 
        Person.__init__(self,name,netid)
        self.office = office
        
    