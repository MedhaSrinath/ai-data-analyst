"""Basic analysis entrypoint."""

import pandas as pd


def main() -> None:
    """Load dataset and print a quick summary."""
    df = pd.read_csv("data/dataset.csv")
    print(df.describe(include="all"))


if __name__ == "__main__":
    main()
