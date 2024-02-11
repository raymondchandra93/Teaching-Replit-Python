import random
from time import sleep

months = [
    'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august',
    'september', 'october', 'november', 'december'
]

fortunes = [
    'You will be very successful this year.',
    'Next year will bring great things.',
    'You will come into a large fortune.',
    'This will be a very bad year for you.',
    'You will not be successful this year.',
    'You will lose something very dear to you this year.'
]


#Generate the player's fortune based on their input
def generate_fortune(month):
  fortune_idx = (months.index(month) * random.randint(1, 3)) % len(fortunes)
  print(fortunes[fortune_idx])


def gather_information():
  while True:
    birth_month = input('What month were you born in?\n')
    if birth_month.lower() in months:
      print('Calculating fortune...')
      sleep(2)
      generate_fortune(birth_month.lower())
      return
    else:
      print('Please enter a real month.')


def main2():
  answer = input('Would you like your fortune told?\n')
  while answer.lower() != 'no':
    if answer.lower() == 'yes':
      gather_information()
      answer = input('\nWould you like another fortune?\n')
    else:
      answer = input(
          'Sorry I do not understand {}.\nPlease enter "yes" or "no".\n'.
          format(answer))
      print('Ok, goodbye then.')


if __name__ == '__main__':
  main2()
