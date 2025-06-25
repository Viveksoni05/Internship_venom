import tkinter as tk
import joblib

# Set up the root window
root = tk.Tk()
root.title("House Price Predictor")
root.geometry("450x350")
root.configure(bg="#f0f0f0")  # Light gray background

def predict_price():
    try:
        area = float(area_entry.get())
        bedrooms = int(bedrooms_entry.get())

        # Load the model
        model = joblib.load('C:/Users/vivek/house_predictor.pkl')
        # Make prediction
        prediction = model.predict([[area, bedrooms]])
        result_label.config(text=f"Predicted Price: ${prediction[0]:,}", fg="green")
    except ValueError:
        result_label.config(text="Please enter valid numbers.", fg="red")

# Create title
title_label = tk.Label(root, text="House Price Predictor",
                      font=("Arial", 16, "bold"), bg="#f0f0f0")
title_label.pack(pady=20)

# Create input fields frame
input_frame = tk.Frame(root, bg="#f0f0f0")
input_frame.pack(pady=10)

# Area input with better alignment
area_label = tk.Label(input_frame, text="Area (sq ft):",
                     width=20, anchor="w", bg="#f0f0f0", font=("Arial", 10))
area_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

area_entry = tk.Entry(input_frame, width=30, font=("Arial", 10))
area_entry.grid(row=0, column=1, padx=10, pady=10)

# Bedrooms input with better alignment
bedrooms_label = tk.Label(input_frame, text="Number of Bedrooms:",
                         width=20, anchor="w", bg="#f0f0f0", font=("Arial", 10))
bedrooms_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

bedrooms_entry = tk.Entry(input_frame, width=30, font=("Arial", 10))
bedrooms_entry.grid(row=1, column=1, padx=10, pady=10)

# Button with improved styling
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=15)

predict_button = tk.Button(button_frame, text="Predict Price",
                          width=15, command=predict_price,
                          bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
predict_button.pack()

# Result frame
result_frame = tk.Frame(root, bg="#f0f0f0")
result_frame.pack(pady=15)


result_label = tk.Label(result_frame, text="Enter values and click Predict",
                       font=("Arial", 12), bg="#f0f0f0",
                       width=30, height=2)
result_label.pack()

# Run the application
root.mainloop()

