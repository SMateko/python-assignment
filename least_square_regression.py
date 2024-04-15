{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "250a44a2-db46-41ae-8303-d8c36cd6a83a",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "from sklearn.linear_model import LinearRegression\n",
    "\n",
    "class LeastSquaresRegression:\n",
    "    def __init__(self, x_values, y_values):\n",
    "        self.x_values = x_values\n",
    "        self.y_values = y_values\n",
    "\n",
    "    def fit(self, degree):\n",
    "        # Validate input data\n",
    "        if len(self.x_values) != len(self.y_values):\n",
    "            raise ValueError(\"Length of x_values must match the length of y_values.\")\n",
    "\n",
    "        coefficients = np.polyfit(self.x_values, self.y_values, degree)\n",
    "        return coefficients\n",
    "\n",
    "\n",
    "class LeastSquaresRegressionAlt:\n",
    "    def __init__(self):\n",
    "        self.model = None\n",
    "\n",
    "    def fit(self, x, y):\n",
    "        self.model = LinearRegression()\n",
    "        self.model.fit(x, y)\n",
    "\n",
    "    def predict(self, x):\n",
    "        return self.model.predict(x)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bb8cb302-0761-4f2b-8840-a42bfc7c4306",
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
