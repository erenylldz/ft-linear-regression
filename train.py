import csv

def load_data(filename):
    mileages = []
    prices = []

    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            mileages.append(float(row["km"]))
            prices.append(float(row["price"]))

    return mileages, prices

def estimate_price(mileage, theta0, theta1):
    return theta0 + theta1 * mileage

def calculate_error(prediction, real_price):
    return prediction - real_price

def calculate_mse(mileages, prices, theta0, theta1):
    total_error = 0
    m = len(mileages)

    for i in range(m):
        prediction = estimate_price(mileages[i], theta0, theta1)
        error = prediction - prices[i]
        total_error += error ** 2

    return total_error / m

def main():
    mileages, prices = load_data("data.csv")

    theta0 = 0
    theta1 = 0

    first_mileage = mileages[0]
    first_real_price = prices[0]

    first_prediction = estimate_price(first_mileage, theta0, theta1)
    first_error = calculate_error(first_prediction, first_real_price)

    mse = calculate_mse(mileages, prices, theta0, theta1)

    print("Data loaded successfully.")
    print("Total rows:", len(mileages))

    print("First mileage:", first_mileage)
    print("First real price:", first_real_price)
    print("First prediction:", first_prediction)
    print("First error:", first_error)

    print("MSE:", mse)

if __name__ == "__main__":
    main()