import random
from time import sleep

# Phase 1

fortunes = [
    'You will be very successful this year.',
    'Next year will bring great things.',
    'You will come into a large fortune.',
    'This will be a very bad year for you.',
    'You will not be successful this year.',
    'You will lose something very dear to you this year.'
]

# Phase 2

def main():
  answer = input('Would you like your fortune told?\n')
  while answer.lower() != 'no':
    if answer.lower() == 'yes':
      print('Calculating fortune...')
      sleep(2)
      print(random.choice(fortunes))

      answer = input('\nWould you like another fortune?\n')

    else:
      answer = input(
          'Sorry I do not understand {}.\n Please enter "yes" or "no".\n'.
          format(answer))

  print('Ok, goodbye then.')


if __name__ == '__main__':
  main()
