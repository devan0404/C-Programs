class RBI:
    def rate_of_interest(self):
        return 6.0
    
class ICICI(RBI):
    def rate_of_interest(self):
        return 6.3

class SBI(RBI):
    def rate_of_interest(self):
        return 6.5

class HDFC(RBI):
    def rate_of_interest(self):
        return 6.7

rbi = RBI()
icici = ICICI()
sbi = SBI()
hdfc = HDFC()

print("RBI Rate of Interest:  ", rbi.rate_of_interest(),"%")
print("ICICI Rate of Interest:", icici.rate_of_interest(),"%")
print("SBI Rate of Interest:  ", sbi.rate_of_interest(),"%")
print("HDFC Rate of Interest: ", hdfc.rate_of_interest(),"%")
