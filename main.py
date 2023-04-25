import sys
from probability import Probability

if __name__ == "__main__":
    try:
        days = int(sys.argv[1])
        print("Number of days is {}".format(days))
    except IndexError:
        print("Please type 'days' argument in command line!!!")
    except ValueError:
        print("Days must be of integer type!!!")
    except Exception as e:
        print(e)
    else:
        prob = Probability(days)
        print("Number of ways to attend classes over {} days is {}".format(days, prob.number_of_ways_to_attend_classes()))
        print("probability of that student to miss graduation ceremony is {}".format(prob.probability_to_miss_gradution_ceremony()))
