import numpy as np
import matplotlib.pyplot as plt


# Generate linearly separable data points
def generate_data(num_samples):
    # Generate random data points for two classes
    class1 = np.random.normal(loc=[2, 2], scale=0.5, size=(num_samples, 2))
    class2 = np.random.normal(loc=[4, 4], scale=0.5, size=(num_samples, 2))

    # Concatenate the two classes
    X = np.concatenate((class1, class2), axis=0)

    # Create labels for the two classes
    y = np.concatenate((np.zeros(num_samples), np.ones(num_samples)))

    return X, y


# Visualize data points
def visualize_data(X, y):
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.coolwarm, marker='o')
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.title('Scatter plot of generated data points')
    plt.show()


# Implement least squares classification algorithm
def least_squares_classification(X, y):
    # Add bias term to X
    X_b = np.c_[np.ones((X.shape[0], 1)), X]

    # Calculate optimal parameters using least squares method
    theta = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)

    return theta


# Visualize the separating line
def visualize_separating_line(X, y, theta):
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.coolwarm, marker='o')
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.title('Separating line with generated data points')

    # Plot separating line
    x1_min, x1_max = X[:, 0].min(), X[:, 0].max()
    x1_range = np.array([x1_min, x1_max])
    x2_range = -(theta[0] + theta[1] * x1_range) / theta[2]
    plt.plot(x1_range, x2_range, color='black')

    plt.show()


# Main function
if _name_ == "_main_":
    # Number of samples for each class
    num_samples = 50

    # Generate data
    X, y = generate_data(num_samples)

    # Visualize data points
    visualize_data(X, y)

    # Implement least squares classification
    theta = least_squares_classification(X, y)

    # Visualize separating line
    visualize_separating_line(X, y, theta)