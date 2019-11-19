#Paint Wizard

class paint():
    def __init__ (self, volume, price, area):
        self.volume = volume
        self.price = price
        self.area = area

    def can_price(self):
        ''' returns can price per area £/m^2'''

        can_price = (self.volume*0.001/self.price)*(1/self.area) 

        return can_price

    def compare():
        pass


##CheapoMax = cheapest(20, 19.99, 10)
##AverageJoes = cheapest(15, 17.99, 11)
##DuluxourousPaints = cheapest(10, 25, 20)
##
##print(CheapoMax)
##print(AverageJoes)
##print(DuluxourousPaints)


    
