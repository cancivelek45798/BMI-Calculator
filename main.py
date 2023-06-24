import tkinter

#functions
def bmi_classification(bmi):
    if bmi < 18.5:
        result_text = "You are Under Weight."

    elif 18.5 <= bmi < 24.9:
        result_text = "You are Normal."

    elif 24.9 <= bmi < 29.9:
        result_text = "You are Over Weight."

    elif 29.9 <= bmi < 34.9:
        result_text = "You are Obesity (Class 1)."

    elif 34.9 <= bmi < 39.9:
        result_text = "You are Obesity (Class 2)."

    else:
        result_text = "You are Extreme Obesity."
    return result_text

def calculate_bmi():
    weight = float(entry_weight.get())
    height = float(entry_height.get())
    bmi = int((weight/((height/100.0)**2.0))*10)/10
    return bmi
def result_bmi():
    try:
        result_labels = []

        for widget in window.winfo_children():
            if isinstance(widget, tkinter.Label) and widget != label_weight and widget != label_height:
                result_labels.append(widget)
                widget.pack_forget()

        bmi_label = tkinter.Label(text=f"Your BMI is {calculate_bmi()}.")
        bmi_label.pack()

        classification_label = tkinter.Label(text=bmi_classification(calculate_bmi()))
        classification_label.pack()

        for label in result_labels:
            label.destroy()

    except:
        result_label = tkinter.Label(text="Please enter the entered values as numbers!")
        result_label.pack()

#window
window = tkinter.Tk()
window.title("BMI Calculator")
window.minsize(width=300, height=200)
window.config(pady=40)

#weight
label_weight = tkinter.Label(text="Enter Your Weight (kg)")
label_weight.pack()

entry_weight = tkinter.Entry()
entry_weight.pack()

#height
label_height = tkinter.Label(text="Enter Your Height (cm)")
label_height.pack()

entry_height = tkinter.Entry()
entry_height.pack()


#button
calculate_button = tkinter.Button(text="Calculate", command=result_bmi)
calculate_button.pack()

window.mainloop()