import sys,re,random

while True:
      x = raw_input("Please ask a question: ")
      n = random.randint(1, 7) 
      if re.match("^exit$|^close$", x):
            print "GoodBye!"
            sys.exit()
      elif n == 1:
            print "The answer lies in your heart"
      elif n == 2:
            print "I do not know"
      elif n == 3:
            print "Almost certainly"
      elif n == 4:
            print "No"
      elif n == 5:
            print "Why do you need to ask?"
      elif n == 6:
            print "Go away. I do not wish to answer at this time."
      elif n == 7:
            print "Time will only tell"
