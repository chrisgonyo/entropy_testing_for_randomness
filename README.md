# Pursuit of Randomness

Encryption key security is based on the idea that the entropy source used to
generate your key is truly random. Unfortunately, the only method to collect truly
random entropy is to measure time intervals in radioactive decay.
Even then you have to trust that the Geiger counter is recording accurately.

## What if humans could generate random bits of entropy without using a computer?
Ideally, we figure out a way to generate entropy bits that are random
enough for cryptographic applications without using a computer.
I set out to create a system for doing just that.

## The Password Wheel

After several mockups I ended up using a CNC laser to create a spinning rotary
wheel with 60 password character landing spots. A D6 precision die was rolled to
determine how fast the user would spin the wheel and how hard to bring down the
stopper. A D12 die was used to represent the number of seconds the wheel would
spin before the stopper was brought down.

## Setting up the Experiment
I physically rolled 1000 D6 dice and 1000 D12 dice. These numbers were used to
eliminate user bias while spinning the wheel. Then I spun the wheel 1000 times and
recorded the results.

## The Testing Process
Once all results were gather and stored in a CSV file I wrote the python script
Entropy_Testing_For_Randomness to be run on a local system. The script uses the
Chi-Squared goodness of fit test and charts expected distribution vs observed.
This test alone won't prove if the entropy source is random but it does give us
a way to calculate the odds of this distribution occurring from a truly random sample.

## The Results
Our D12 die performed the best with a 0.9368 P-value. Our D6 'precision' die
also passed the test with 0.6234 P-value. Unfortunately, my password wheel
failed miserably. The p-value came in at 0.0011. That means that if my wheel was
truly random the character distribution observed would only occur 0.11% of the time.

## Run your own test
Included in the script Entropy_Testing_For_Randomness is a test to evaluate how
well you system is generating entropy. The secrets() method pulls entropy from
your local computer. Does your computer pass the test? Remember, it will change
each time you run the program. Also, a 'failed' test occurring 5 times out of 100
would be par for the course and wouldn't fully invalidate the hypothesis.

## Interesting in other tests for randomness?
Check out NIST standards for additional tests that can be run to evaluate
random number generators. Passing one test doesn't mean it's random, it just increases confidence.
