# handwritten digit classifier

### model_training.py:
 Using the mnist dataset to train a model.
 
### model_evaluation.py:
 Evaluation of the trained model.
 
##### Visualization:
 <img src="https://github.com/leondorian/handwritten_digit_classifier/assets/154075579/170585ff-6418-4481-87ce-5c40065d6e6a" alt="digit_8_gif" width="450" height="auto">
 
### main.py: 

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
    <td><img src="https://github.com/leondorian/handwritten_digit_classifier/assets/154075579/1dc1b3dc-6ffe-4c33-87a3-9d229507dbdd" alt="digit_1" width="220" height="auto"></td>
    <td><img src="https://github.com/leondorian/handwritten_digit_classifier/assets/154075579/fb371b85-664b-4f8e-a3a0-e8773b4b1713" alt="digit_8" width="220" height="auto"></td>
    <td><img src="https://github.com/leondorian/handwritten_digit_classifier/assets/154075579/74376d5e-0ca4-496d-8056-a101a78826a6" alt="digit_7" width="220" height="auto"></td>
  </tr>
</table>
