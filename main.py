# digits/main.py

import questionary
from solver.strategy import Strategy
from solver.operations import operations

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

        print(f"\t-> options given: {numbers}")

        solve = operations(target, numbers, Strategy[str(strategy.upper())])
        print(f"\t-> Strategy {strategy}")
        print(f"\t-> Solution {solve}")
    except ValueError:
        print("Invalid input. Please enter only integer values.")

if __name__ == "__main__":
    main()
