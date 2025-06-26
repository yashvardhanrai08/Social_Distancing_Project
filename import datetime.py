import datetime

def get_birthday_wish(name):
  """Generates a personalized birthday wish."""

  today = datetime.date.today()
  birthday_wish = f"Happy Birthday, {name}!\n"
  birthday_wish += f"May this year be filled with joy, love, and all the best things life has to offer."

  return birthday_wish

if __name__ == "__main__":
  name = input("enter ur girlfriend name:")
  wish = get_birthday_wish(name)
  print(wish)