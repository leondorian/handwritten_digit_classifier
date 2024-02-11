import math
import numpy as np
import tensorflow as tf
from tkinter import *


def calculate_rectangle(event):
    event.x, event.y = event.x - 5, event.y - 5
    if math.ceil(event.x / 10) == math.floor(event.x / 10) and math.ceil(event.y / 10) == math.floor(event.y / 10):
        x1, y1 = event.x, event.y
        x2, y2 = event.x + 10, event.y + 10
    elif math.ceil(event.x / 10) == math.floor(event.x / 10):
        x1, y1 = event.x, math.floor(event.y / 10) * 10
        x2, y2 = event.x + 10, math.ceil(event.y / 10) * 10
    elif math.ceil(event.y / 10) == math.floor(event.y / 10):
        x1, y1 = math.floor(event.x / 10) * 10, event.y
        x2, y2 = math.ceil(event.x / 10) * 10, event.y + 10
    else:
        x1, y1 = math.floor(event.x / 10) * 10, math.floor(event.y / 10) * 10
        x2, y2 = math.ceil(event.x / 10) * 10, math.ceil(event.y / 10) * 10
    return x1, y1, x2, y2


class DrawingApp:
    def __init__(self, master, model):
        self.img_array = np.zeros((28, 28))
        self.prediction = StringVar()
        self.eventCount = 0

        self.model = model

        self.master = master
        self.master.title("Digit Classifier")

        self.canvas = Canvas(self.master, width=280, height=280, bg="#262626", borderwidth=0)
        self.draw_border()
        self.canvas.pack(fill=BOTH, expand=True)

        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)

        self.clear_button = Button(self.master, text="Clear", command=self.clear_canvas)
        self.clear_button.pack(side=BOTTOM)

        self.label = Label(self.master, textvariable=self.prediction)
        self.label.pack(side=BOTTOM)

    def draw_border(self):
        self.canvas.create_rectangle(0, 0, 280, 28, fill="#1a1919", outline="#1a1919")
        self.canvas.create_rectangle(0, 280 - 28, 280, 280, fill="#1a1919", outline="#1a1919")
        self.canvas.create_rectangle(0, 0, 28, 280, fill="#1a1919", outline="#1a1919")
        self.canvas.create_rectangle(280 - 28, 0, 280, 280, fill="#1a1919", outline="#1a1919")

    def on_mouse_drag(self, event):
        x1, y1, x2, y2 = calculate_rectangle(event)

        if x1 // 10 < 28 and y1 // 10 < 28:
            x = x1 // 10
            y = y1 // 10
            self.img_array[y][x] = 1
            if y > 0:
                self.img_array[y-1][x] = 1
            if y < 27:
                self.img_array[y+1][x] = 1
            if x > 0:
                self.img_array[y][x-1] = 1
            if x < 27:
                self.img_array[y][x+1] = 1

        self.canvas.create_rectangle(x1 + 5, y1 + 5, x2 + 5, y2 + 5, fill="white", outline="white")
        self.canvas.create_rectangle(x1 + 5 -10, y1 + 5, x2 + 5+10, y2 + 5, fill="white", outline="white")
        self.canvas.create_rectangle(x1 + 5, y1 + 5-10, x2 + 5, y2 + 5+10, fill="white", outline="white")
        if self.eventCount % 10 == 0:
            self.predict_image()
        self.eventCount += 1

    def clear_canvas(self):
        self.canvas.delete("all")
        self.prediction.set('')
        self.img_array = np.zeros((28, 28))
        self.draw_border()

    def predict_image(self):
        img = np.array([self.img_array])
        prediction = self.model.predict(img)
        self.prediction.set(f'Prediction: {prediction.argmax()} ({prediction[0][np.argmax(prediction)] * 100:.2f}% '
                            f'confidence)')


def main():
    # Load model
    model = tf.keras.models.load_model('digit.model')

    root = Tk()
    root.resizable(width=False, height=False)
    app = DrawingApp(root, model)
    root.mainloop()


if __name__ == "__main__":
    main()
