class PiggyBank:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def add_money(self, deposit_dollars, deposit_cents):
        self.dollars += deposit_dollars
        if self.cents + deposit_cents > 99:
            self.dollars += (self.cents + deposit_cents) // 100
            # print(self.dollars)
            self.cents = self.cents - self.cents + ((self.cents + deposit_cents) % 100)
            # print(self.cents)

        else:
            self.cents += deposit_cents

        return self.dollars, self.cents
