import datetime
import pytz

class Account:

  @staticmethod
  def _current_time():
    utc_time = datetime.datetime.utcnow()
    return pytz.utc.localize(utc_time)

  def __init__(self, name, balance):
    self._name = name
    self.__balance = balance
    self._transaction_list = []
    if balance > 0:
      self._transaction_list.append((Account._current_time(), balance))
    print("Account created for " + self._name)
    self.show_balance()

  def deposit(self, amount):
    if amount > 0:
      self.__balance += amount
      self.show_balance()
      self._transaction_list.append((Account._current_time(), amount))

  def withdraw(self, amount):
    if self.__balance >= amount > 0:
      self.__balance -= amount
      self.show_balance()
      self._transaction_list.append((Account._current_time(), -amount))
    else:
      print("The amount must be greater than 0 and lesser than {}".format(self.__balance))
  
  def show_balance(self):
    print("Balance is {}".format(self.__balance))

  def show_transactions(self):
    for date, amount in self._transaction_list:
      if amount > 0:
        tran_type = "deposited"
      else:
        tran_type = "withdrawn"
        amount *= -1
      print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))

if __name__ == "__main__":
  lucas = Account("Lucas", 0)
  lucas.show_balance()

  lucas.deposit(1000)
  lucas.withdraw(500)
  lucas.withdraw(2000)

  lucas.show_transactions()

  thi = Account("Thi", 800)
  thi.__balance = 200
  thi.deposit(100)
  thi.withdraw(200)
  thi.show_transactions()