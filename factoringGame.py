import sys
import math
import random
import numpy as np

base = 2
primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
logPrimes = [math.log(x, base) for x in primes]

probPrimes = [1/lp**2 for lp in logPrimes]
totalProb = sum(probPrimes)
probPrimes = [p/totalProb for p in probPrimes]
cumProbs = np.cumsum(probPrimes)


def generate(budget):
	nums = []
	while budget > 0:
		rn = random.random()
		index = int(np.sum(rn > cumProbs)) 
		nums.append(primes[index])
		budget -= logPrimes[index]
	return nums

def mul(factors):
	return int(np.prod(factors))

def isCorrect(ans, n):
	if ans.lower() == PASS:
		print("Skipped.")
		return True
	if ans.lower() == QUIT:
		print("Bye!")
		sys.exit(1)

	ans = [a for a in ans.split(" ") if len(a) > 0]
	try:
		ans = [int(a) for a in ans]
		correct = all([a in primes for a in ans]) and mul(ans) == n
		if not correct:
			print("Your factorization was not correct. Try again.\n")
		else:
			print("Correct!")
		return correct
	except:
		print("Oops, that was not a valid response.")
		return False

PASS = "pass"
QUIT = "quit"
instructions = """
Factor the following numbers. Use paper!
Type your response as a list of space separated values (e.g "2 3 5"). 
Type 'quit' to quit. Type 'pass' to skip a number.
"""

def play(budget=10):
	prevCorrect = True
	while True:
		if prevCorrect:
			factors = generate(budget)
			n = mul(factors)
			print("--------------------")
		ans = input("Factor " + str(n) + ": ")
		prevCorrect = isCorrect(ans, n)
		

if __name__ == "__main__":
	print(instructions)
	budget = input("Choose a level (default=10): ")
	try:
		budget = float(budget)
	except:
		budget = 10
	print("Playing level " + str(budget))
	play(budget)
