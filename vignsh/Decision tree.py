
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

# Training dataset
# Features: [Weather (0 = Sunny, 1 = Rainy), Temperature (0 = Cool, 1 = Hot)]
features = [[0, 0], [0, 1], [1, 0], [1, 1]]
labels = [1, 0, 1, 0]  # 1 = Play, 0 = Don't Play

# Initialize DecisionTreeClassifier
clf = DecisionTreeClassifier()

# Train the model
clf.fit(features, labels)

# Get user input
print("Enter the weather condition (0 for Sunny, 1 for Rainy):")
weather = int(input("Weather: "))

print("Enter the temperature condition (0 for Cool, 1 for Hot):")
temperature = int(input("Temperature: "))

# Predict using user input
user_data = [[weather, temperature]]
prediction = clf.predict(user_data)

# Output the result
if prediction[0] == 1:
    print("Decision: Play")
else:
    print("Decision: Don't Play")

# Visualize the decision tree
tree.plot_tree(clf, feature_names=["Weather", "Temperature"], class_names=["Don't Play", "Play"], filled=True)
