{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "ee7077da-4525-4e86-bbc5-c41abff0fce1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Results for y1:\n",
      "Coefficients: [-1.99789814]\n",
      "Intercept: 0.0077711545704195195\n",
      "Mean Squared Error: 0.21779068106461094\n",
      "\n",
      "\n",
      "Results for y2:\n",
      "Coefficients: [1.99863883]\n",
      "Intercept: 0.005692899286316069\n",
      "Mean Squared Error: 0.2153464483311835\n",
      "\n",
      "\n",
      "Results for y3:\n",
      "Coefficients: [0.99962825]\n",
      "Intercept: -0.0016468939664569283\n",
      "Mean Squared Error: 0.07463349799297608\n",
      "\n",
      "\n",
      "Results for y4:\n",
      "Coefficients: [0.00138676]\n",
      "Intercept: 0.012702145351320113\n",
      "Mean Squared Error: 0.1064460532489211\n",
      "\n",
      "\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "\n",
    "class LeastSquaresRegression:\n",
    "    def fit(self, X, y):\n",
    "        # Add a column of ones for the intercept term\n",
    "        X = np.c_[np.ones(X.shape[0]), X]\n",
    "        \n",
    "        # Calculate coefficients using normal equation\n",
    "        coefficients = np.linalg.inv(X.T @ X) @ X.T @ y\n",
    "        \n",
    "        return coefficients[1:], coefficients[0]  # Return coefficients and intercept\n",
    "\n",
    "def calculate_least_squares(X, y):\n",
    "    model = LeastSquaresRegression()\n",
    "\n",
    "    # Fit the model to the data\n",
    "    coefficients, intercept = model.fit(X, y)\n",
    "\n",
    "    # Predict Y values using the fitted model\n",
    "    y_pred = X @ coefficients + intercept\n",
    "\n",
    "    # Calculate the mean squared error\n",
    "    mse = np.mean((y - y_pred) ** 2)\n",
    "\n",
    "    return coefficients, intercept, mse\n",
    "\n",
    "def main():\n",
    "    training_data = pd.read_csv('train.csv')\n",
    "\n",
    "    # Assuming X column in the training data\n",
    "    X_train = training_data[['x']].values\n",
    "\n",
    "    # List of Y columns in the training data\n",
    "    y_columns = ['y1', 'y2', 'y3', 'y4']\n",
    "\n",
    "    # Dictionary to store results for each Y column\n",
    "    results = {}\n",
    "\n",
    "    # Calculate Least-Squares Regression for each Y column\n",
    "    for y_col in y_columns:\n",
    "        Y_train = training_data[y_col].values\n",
    "\n",
    "        # Calculate Least-Squares Regression for the current Y column\n",
    "        coefficients, intercept, mse = calculate_least_squares(X_train, Y_train)\n",
    "\n",
    "        # Store the results in the dictionary\n",
    "        results[y_col] = {'Coefficients': coefficients,\n",
    "                          'Intercept': intercept,\n",
    "                          'Mean Squared Error': mse}\n",
    "\n",
    "    # Print the results\n",
    "    for y_col, result in results.items():\n",
    "        print(f\"Results for {y_col}:\")\n",
    "        print(\"Coefficients:\", result['Coefficients'])\n",
    "        print(\"Intercept:\", result['Intercept'])\n",
    "        print(\"Mean Squared Error:\", result['Mean Squared Error'])\n",
    "        print(\"\\n\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bda74c87-3b82-4e10-a44f-8cd560569ab0",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}