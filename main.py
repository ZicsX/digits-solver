# digits/main.py

import questionary
from guess.strategy import Strategy
from guess.operations import operations
from primes.primes import get_prime_factors, get_components

def main():
    try:
        target = int(questionary.text("What's the target value?", default="77").ask())
        numbers = questionary.text(
            "What are the given numbers? (enter comma separated list)", default="1,2,3,4,5,25"
        ).ask()
        numbers = [int(i) for i in numbers.split(',')]

        strategy = questionary.select(
            "Select a strategy",
            choices=[str(s) for s in Strategy.values()],
            default=str(Strategy.SHORTEST)
        ).ask()

        prime_factors = get_prime_factors(target)
        factors = get_components(target)

        print(f"\t-> options given: {numbers}")
        print(f"\t-> prime factors {prime_factors}")
        print(f"\t-> components {factors}")

        guess = operations(target, numbers, Strategy[str(strategy.upper())])
        print(f"\t-> strategy {strategy}")
        print(f"\t-> guess {guess}")
    except ValueError:
        print("Invalid input. Please enter only integer values.")

if __name__ == "__main__":
    main()
