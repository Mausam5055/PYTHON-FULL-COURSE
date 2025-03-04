# import numpy as np
# import matplotlib.pyplot as plt

# # Data
# x = np.array([1, 2, 3, 4])
# y = np.array([16, 19, 23, 26])

# # Calculate the coefficients of the line of best fit
# # np.polyfit calculates the polynomial coefficients. Here, we use degree 1 for a linear fit.
# a, b = np.polyfit(x, y, 1)

# # Generate the line of best fit
# y_fit = a + b * x

# # Plotting the data and the line of best fit
# plt.scatter(x, y, color='blue', label='Data points')
# plt.plot(x, y_fit, color='red', label=f'Best fit line: y = {a:.2f} + {b:.2f}x')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Best Fit Line')
# plt.legend()
# plt.grid(True)
# plt.show()

# # Print the coefficients
# print(f'The line of best fit is: y = {a:.2f} + {b:.2f}x')



# import numpy as np
# import matplotlib.pyplot as plt

# # Data
# x = np.array([1, 2, 3, 4])
# y = np.array([16, 19, 23, 26])

# # Calculate the coefficients of the line of best fit
# # np.polyfit calculates the polynomial coefficients. Here, we use degree 1 for a linear fit.
# a, b = np.polyfit(x, y, 1)

# # Generate the line of best fit
# y_fit = a + b * x

# # Plotting the data and the line of best fit
# plt.scatter(x, y, color='blue', label='Data points')
# plt.plot(x, y_fit, color='red', label=f'Best fit line: y = {a:.2f} + {b:.2f}x')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Best Fit Line')
# plt.legend()
# plt.grid(True)
# plt.show()

# # Print the coefficients
# print(f'The line of best fit is: y = {a:.2f} + {b:.2f}x')


# import matplotlib.pyplot as plt
# import math

# x = [50,450,780,1200,4400,4800,5300]
# y = [28,30,32,36,51,58,69]

# a = len(x)

# xy = 0
# xx = 0
# for i in range(a):
#   xy +=x[i]* math.log(y[i])
#   xx +=x[i]*x[i]

# print(xy)
# print(xx)

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Data
altitude = np.array([50, 450, 780, 1200, 4400, 4800, 5300])
dose_of_radiation = np.array([28, 30, 32, 36, 51, 58, 69])

# Transform the data for linear fitting
Y = np.log(dose_of_radiation)  # ln(y)
X = altitude  # x

# Define the linear model
def linear_model(x, C, M):
    return C + M * x

# Fit the linear model to transformed data
params, _ = curve_fit(linear_model, X, Y)

# Extract parameters
C = params[0]
M = params[1]

# Compute a and b
a = np.exp(C)
b = np.exp(M)

# Print the parameters
print(f'Obtained values:')
print(f'a = {a:.2f}')
print(f'b = {b:.2f}')

# Predict the mean radiation dose at an altitude of 3000 feet
altitude_to_predict = 3000
predicted_ln_dose = C + M * altitude_to_predict
predicted_dose = np.exp(predicted_ln_dose)

# Print the prediction
print(f'Predicted mean radiation dose at an altitude of 3000 feet: {predicted_dose:.2f}')

# Plotting the data and the fit
plt.scatter(altitude, dose_of_radiation, color='blue', label='Data points')

# Generate fitted line
fit_dose = a * np.exp(b * altitude)
plt.plot(altitude, fit_dose, color='red', label=f'Best fit line: y = {a:.2f} * {b:.2f}^x')

plt.xlabel('Altitude')
plt.ylabel('Dose of Radiation')
plt.title('Best Fit Curve for Radiation Dose vs. Altitude')
plt.legend()
plt.grid(True)
plt.show()


print(sumx)
print(sumy)
print(xy)
print(xx)