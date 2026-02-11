class RideSharingSystem:

    def __init__(self):
        self.riders = []
        self.drivers = []
        
    def addRider(self, riderId: int) -> None:
        self.riders.append(riderId)

    def addDriver(self, driverId: int) -> None:
        self.drivers.append(driverId)

    def matchDriverWithRider(self) -> List[int]:
        if self.drivers and self.riders:
            driver = self.drivers[0]
            self.drivers = self.drivers[1:]
            rider = self.riders[0]
            self.riders = self.riders[1:]
            return [driver,rider]
        else: return [-1,-1]

    def cancelRider(self, riderId: int) -> None:
        if riderId in self.riders:
            self.riders.remove(riderId)
