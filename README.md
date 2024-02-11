# handwritten digit classifier

#### model_training.py:
 Using the mnist dataset to train a model.
 
#### model_evaluation.py:
 Evaluation of the trained model.
 
#### main.py: 
<p>
 Creating a interface so we can draw digits that the model then tries to predict. <br>
 The canvas to draw on has a size of 280x280, but the image is scaled down to 28x28 to fit the input-size of the model.
</p>

## Example
<img src="https://github.com/leondorian/handwritten_digit_classifier/assets/154075579/27423930-5a70-4d09-8c51-8bf1c527b36d" alt="digit_8_gif" width="450" height="auto">

<p>
 While drawing the interface shows the current prediction and its confidence. 
</p>

<table>
  <tr>
    <th scope="col">Pred: 1 (99.43% confidence)</th>
    <th scope="col">Pred: 8 (99.92% confidence)</th>
    <th scope="col">Pred: 7 (98.06% confidence)</th>
  </tr>
  <tr>
    <td><img src="https://github.com/leondorian/handwritten_digit_classifier/assets/154075579/ccbfc0ef-8439-4092-bf8f-4808b709e0fb" alt="digit_1" width="220" height="auto"></td>
    <td><img src="https://github.com/leondorian/handwritten_digit_classifier/assets/154075579/7657fe18-e1ab-492f-b903-765590569c23" alt="digit_8" width="220" height="auto"></td>
    <td><img src="https://github.com/leondorian/handwritten_digit_classifier/assets/154075579/7d7017b4-4b41-4775-bb60-ab457c2c7834" alt="digit_7" width="220" height="auto"></td>
  </tr>
</table>
