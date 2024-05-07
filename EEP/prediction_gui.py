try:
    import tkinter as tk
    from tkinter import PhotoImage, StringVar
    from tkinter import filedialog
    import requests
    from PIL import Image, ImageTk
except Exception as e:
    print('Error loading module in prediction_gui.py: ', e)

form_to_string = lambda data: '\n'.join([f"label {entry['label']} score: {entry['score']*100:.2f}%" for entry in data])

class PredictionsWindow(tk.Tk):

    def __init__(self):
        
        super().__init__()
        self.title("Medical cases prediction")
        self.configure(bg="white")
        self.create_widgets()

    
    def create_widgets(self):
        self.button_cancer_pred = tk.Button(self, text="Breast cancer prediction", command=self.cancer_pred, fg="red", bg="white", font=("Arial", 14))
        self.button_fracture_pred = tk.Button(self, text="Fractured bone prediction", command=self.fracture_pred, fg="red", bg="white", font=("Arial", 14))
        self.button_pneumo_pred = tk.Button(self, text="Pneumonia prediction", command=self.pneumo_pred, fg="red", bg="white", font=("Arial", 14))
        
        self.label_cancer_pred = tk.Label(self)
        self.image_cancer_pred = Image.open("breast_cancer.jpg")
        self.image_cancer_pred = self.image_cancer_pred.resize((300, 300))
        self.photo_cancer_pred = ImageTk.PhotoImage(self.image_cancer_pred)
        self.label_cancer_pred.config(image=self.photo_cancer_pred)
        self.label_cancer_pred.image = self.photo_cancer_pred

        self.label_fracture_pred = tk.Label(self)
        self.image_fracture_pred = Image.open("Fracture-ankle.jpg")
        self.image_fracture_pred = self.image_fracture_pred.resize((300, 300))
        self.photo_fracture_pred = ImageTk.PhotoImage(self.image_fracture_pred)
        self.label_fracture_pred.config(image=self.photo_fracture_pred)
        self.label_fracture_pred.image = self.photo_fracture_pred

        self.label_pneumo_pred = tk.Label(self)
        self.image_pneumo_pred = Image.open("pneumo.jpg")
        self.image_pneumo_pred = self.image_pneumo_pred.resize((300, 300))
        self.photo_pneumo_pred = ImageTk.PhotoImage(self.image_pneumo_pred)
        self.label_pneumo_pred.config(image=self.photo_pneumo_pred)
        self.label_pneumo_pred.image = self.photo_pneumo_pred

        self.text_var_cancer_pred = StringVar(value="Breast cancer prediction")
        self.text_var_fracture_pred = StringVar(value="Fractured bone prediction")
        self.text_var_pneumo_pred = StringVar(value="Pneumonia prediction")

        self.label_text_cancer_pred = tk.Label(self, textvariable=self.text_var_cancer_pred, fg="blue", bg="white", font=("Arial", 16))
        self.label_text_fracture_pred = tk.Label(self, textvariable=self.text_var_fracture_pred, fg="blue", bg="white", font=("Arial", 16))
        self.label_text_pneumo_pred = tk.Label(self, textvariable=self.text_var_pneumo_pred, fg="blue", bg="white", font=("Arial", 16))

        self.button_cancer_pred.grid(row=0, column=0, padx=10, pady=10)
        self.button_fracture_pred.grid(row=0, column=1, padx=10, pady=10)
        self.button_pneumo_pred.grid(row=0, column=2, padx=10, pady=10)

        self.label_cancer_pred.grid(row=1, column=0, padx=10, pady=10)
        self.label_fracture_pred.grid(row=1, column=1, padx=10, pady=10)
        self.label_pneumo_pred.grid(row=1, column=2, padx=10, pady=10)

        self.label_text_cancer_pred.grid(row=2, column=0, padx=10, pady=10)
        self.label_text_fracture_pred.grid(row=2, column=1, padx=10, pady=10)
        self.label_text_pneumo_pred.grid(row=2, column=2, padx=10, pady=10)

    
    def cancer_pred(self):
        try:
            file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
            if file_path:
                with open(file_path, 'rb') as file:
                    
                    files_js = {'filename':file}
                    response = requests.post('http://127.0.0.1:8000/query_cancer', files=files_js)
                    if response.status_code == 200:
                        if "error" in response.json():
                            self.text_var_cancer_pred.set("error, try again")
                            self.label_text_cancer_pred.fg = "red"
                        else:
                            self.text_var_cancer_pred.set(form_to_string(response.json()))
                            self.label_text_cancer_pred.fg = "blue"
                    else:
                        print("Failed to upload image.")
        except Exception as e:
            print("error in function cancer_pred: ", e)

    
    def fracture_pred(self):
        try:
            file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
            if file_path:
                with open(file_path, 'rb') as file:
                    files_js = {'filename':file}
                    response = requests.post('http://127.0.0.1:8000/query_fracture', files=files_js)
                    if response.status_code == 200:
                        if "error" in response.json():
                            self.text_var_fracture_pred.set("error, try again")
                            self.label_text_fracture_pred.fg = "red"
                        else:
                            self.text_var_fracture_pred.set(form_to_string(response.json()))
                            self.label_text_fracture_pred.fg = "blue"
                    else:
                        print("Failed to upload image.")
        except Exception as e:
            print("error in function fracture_pred: ", e)

    
    def pneumo_pred(self):
        try:
            file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
            if file_path:
                with open(file_path, 'rb') as file:
                    files_js = {'filename':file}
                    response = requests.post('http://127.0.0.1:8000/query_pneumo', files=files_js)
                    if response.status_code == 200:
                        if "error" in response.json():
                            self.text_var_pneumo_pred.set("error, try again")
                            self.label_text_pneumo_pred.fg = "red"
                        else:
                            self.text_var_pneumo_pred.set(form_to_string(response.json()))
                            self.label_text_pneumo_pred.fg = "blue"
                    else:
                        print("Failed to upload image.")
        except Exception as e:
            print("error in function pneumo_pred: ", e)


if __name__ == "__main__":
    app = PredictionsWindow()
    app.mainloop()
