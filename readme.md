# Bangla OCR


## Dataset Description:

### BanglaWriting
- [Dataset Manual](https://arxiv.org/pdf/2011.07499.pdf)
- [Download from here](https://data.mendeley.com/datasets/r43wkvdk4w/1)

## Process

### Preprocessing
The dataset is not processed and it needs further preprocessing. From the raw image folder the word images have been extracted using the provided json file. During the extraction process the cropped images are binarized using Otsu’s Binarization technique. The filename follows the configuration below.

"**পরিবার 18__225_15_1.jpg**" as "**label wordNumberOfThePage__uniquePersonNumber_age_gender.extension**"

### Model
- **CRNN** = CNN + BiDirectional GRU

### Loss Function
- CTC Loss

### Optimizer
- Adam


## Requirements
- python==3.7.0
- numpy=1.16.0
- scikit-learn==0.23.2
- opencv-python==4.4.0.46
- torch==1.7.0
- tqdm==4.53.0


## Further Improvement can be done through:
- Preprocessing such as skew correction, noise removal, thinning and skeletonization
- Gathering and/or generating synthetic data 
- Making the dataset balanced
- Using Focal CTC loss to overcome class imbalance problem
- Using Edit distance to predict neareast word
- Using better optimizer such as RAdam


## References
1. [Handwriting to Text Conversion using Time Distributed CNN and LSTM with CTC Loss Function](https://towardsdatascience.com/handwriting-to-text-conversion-using-time-distributed-cnn-and-lstm-with-ctc-loss-function-a784dccc8ec3
)

2. [Use PyTorch’s DataLoader with Variable Length Sequences for LSTM/GRU](https://www.codefull.net/2018/11/use-pytorchs-dataloader-with-variable-length-sequences-for-lstm-gru/
)

3. [Data Preparation for Variable Length Input Sequences](https://machinelearningmastery.com/data-preparation-variable-length-input-sequences-sequence-prediction/
)

4. [Captcha recognition using PyTorch (Convolutional-RNN + CTC Loss)](https://www.youtube.com/watch?v=IcLEJB2pY2Y&t=3799s)

5. [Image Text Recognition](https://medium.com/analytics-vidhya/image-text-recognition-738a368368f5
)

6. [Sequence Modeling: Recurrentand Recursive Nets](https://www.deeplearningbook.org/contents/rnn.html)
