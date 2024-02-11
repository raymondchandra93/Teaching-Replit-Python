import random, calendar
from time import sleep

months = []

fortunes = [
    'You will be very successful this year.',
    'Next year will bring great things.',
    'You will come into a large fortune.',
    'This will be a very bad year for you.',
    'You will not be successful this year.',
    'You will lose something very dear to you this year.'
]


#fill the months array with Month names from the calendar library
def fill_months():
  global months

  #Iterates through the months skipping over the empty string at calendar.month_name[0]
  for month in calendar.month_name[1:]:
    #This will make string comparisons easier later on
    months.append(month.lower())


def gather_information():
  question_num = 1
  while True:
    if question_num == 1:
      birth_month = input('What month were you born in?\n')
      if birth_month.lower() in months:
        question_num += 1
      else:
        print('Please enter a real month.')

    elif question_num == 2:
      initial = input("What is your first initial?\n")
      if len(initial) == 1 and initial.isalpha():
        question_num += 1
      else:
        print('That is not a letter')

    else:
      try:
        age = int(input('How old are you?\n'))
      except ValueError:
        print('Please enter a number')
      else:
        print('Calculating fortune...')
        sleep(2)
        generate_fortune(birth_month.lower(), initial, age)
        return


def main():
  fill_months()
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
  main()
