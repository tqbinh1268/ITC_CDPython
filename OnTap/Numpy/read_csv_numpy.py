"""Demo script that shows how to load CSV data with NumPy."""

from pathlib import Path
import numpy as np


def load_customers(csv_path: Path) -> np.ndarray:
    """Read the CSV file into a structured NumPy array."""
    return np.genfromtxt(
        csv_path,
        delimiter=",",
        names=True,
        dtype=None,
        encoding="utf-8",
    )


def main() -> None:
    data_path = Path(__file__).with_name("Data") / "customers-100.csv"
    customers = load_customers(data_path)

    print(
        f"Loaded {customers.size} rows with fields: "
        f"{', '.join(customers.dtype.names)}"
    )

    print("\nFirst five customers:")
    for row in customers[:5]:
        print(
            f" - {row['First_Name']} {row['Last_Name']} "
            f"({row['Country']}) subscribed on {row['Subscription_Date']}"
        )

    countries, counts = np.unique(customers["Country"], return_counts=True)
    top_idx = np.argsort(counts)[::-1][:5]
    print("\nMost common countries:")
    for idx in top_idx:
        print(f" - {countries[idx]}: {counts[idx]} customers")


if __name__ == "__main__":
    main()
