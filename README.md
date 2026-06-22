# ft_linear_regression

## Description

This project is an introduction to machine learning. The goal is to implement a simple linear regression algorithm from scratch.

The program predicts the price of a car based on its mileage. The model is trained using gradient descent and a single feature: `km`.

No machine learning libraries are used. The linear regression algorithm, prediction function, cost calculation and gradient descent update are implemented manually.

## Formula

The project uses the hypothesis required by the subject:

```text
estimatePrice(mileage) = theta0 + theta1 * mileage
```

Where:

```text
theta0  = intercept / bias
theta1  = slope
mileage = input feature
price   = predicted value
```

Before training, both parameters are initialized to zero:

```text
theta0 = 0
theta1 = 0
```

## Dataset

The dataset is stored in:

```text
data.csv
```

It contains two columns:

```text
km,price
```

Example:

```csv
km,price
240000,3650
139800,3800
150500,4400
```

## Project structure

```text
ft-linear-regression/
├── data.csv
├── train.py
├── predict.py
├── model.json
├── visualize.py
├── evaluate.py
├── linear_regression.png
├── requirements.txt
└── README.md
```

## Training

To train the model, run:

```bash
python3 train.py
```

The training program:

1. Reads the dataset from `data.csv`
2. Normalizes mileage values
3. Trains the model using gradient descent
4. Saves `theta0`, `theta1`, `min_mileage` and `max_mileage` into `model.json`

Example output:

```text
Data loaded successfully.
Total rows: 24
Min mileage: 22899.0
Max mileage: 240000.0
Initial MSE: 41761038.58
Final MSE: 445645.25
Theta0: 8008.43
Theta1: -4656.59
Model saved to model.json
```

## Prediction

To predict the price of a car for a given mileage, run:

```bash
python3 predict.py
```

Example:

```text
Enter mileage: 240000
Estimated price: 3351.85
```

If the entered mileage is outside the training data range, the program displays a warning because the prediction may not be reliable.

## Normalization

Mileage values are large, so they are normalized before training:

```text
normalized_mileage = (mileage - min_mileage) / (max_mileage - min_mileage)
```

The same normalization is also applied in `predict.py`.

For this reason, `model.json` stores:

```json
{
    "theta0": 8008.439832646783,
    "theta1": -4656.591444722055,
    "min_mileage": 22899.0,
    "max_mileage": 240000.0
}
```

## Visualization

To generate a graph of the dataset and the regression line, run:

```bash
python3 visualize.py
```

This creates:

```text
linear_regression.png
```

The graph shows:

1. The real data points from `data.csv`
2. The trained linear regression line

## Evaluation

To evaluate the model, run:

```bash
python3 evaluate.py
```

The evaluation program calculates:

```text
MAE
MSE
RMSE
R2 score
MAPE
Approximate precision
```

Example output:

```text
Model evaluation results
------------------------
MAE: 557.84
MSE: 445645.25
RMSE: 667.57
R2 score: 0.7330
MAPE: 9.65%
Approximate precision: 90.35%
```

Since this is a regression problem, regression metrics such as MAE, RMSE and R² are more meaningful than classification precision. An approximate precision value is calculated as:

```text
Approximate precision = 100 - MAPE
```

## Libraries

The core algorithm is implemented manually.

Used libraries:

```text
csv
json
math
matplotlib
```

Not used:

```text
sklearn
numpy.polyfit
scipy.stats.linregress
any ready-made linear regression model
```

## Installation

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

If `requirements.txt` does not exist yet, create it with:

```text
matplotlib
```

## Notes

The model is reliable mainly within the mileage range of the training data:

```text
22899 km - 240000 km
```

Predictions outside this range are extrapolations and may produce unrealistic results.
