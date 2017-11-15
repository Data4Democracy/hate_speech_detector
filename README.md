# hate_speech_detector

## Data

We are currently working with the data collected by Davidson et al. for their research on hate speech detection. The dataset contains tweets that are labeled as either hate speech, offensive language, or neither. The data were pulled from Hatebase.org, an organization that collects instances of potential hate speech. The data were then labeled using CrowdFlower which uses non-specialists to clean and label data. Each tweet was reviewed by three or more people and a majority-wins approach was taken when there way disagreement.

All data used in this analysis is stored in the data folder of this repository. The original source of the data is :https://github.com/t-davidson/hate-speech-and-offensive-language

The paper by Davidson et al. can be found here: https://arxiv.org/pdf/1703.04009.pdf





## To Do:

### Classifier 
There are currently two Jupyter Notebooks containing models to classify the data, but both could be greatly improved. Please feel free to take a look and let us know if you make any improvements!

### Data preprocessing
There is currently very little preprocessing done on this data. Would someone be interested in created some useful categories for machine learning and plugging them back into the models? My guess is feature engineering has the most potential to improve the model.

### Dataset
The Davidson et al. paper remarked on some possible mislabelings in the dataset. Is mislabeling common in the dataset? Fixing any labels would definitely improve our ability to create a classifier. How big a problem is this? Does someone want to look at some of the misclassifications and see if any are incorrectly labeled?

Also, there's a second data source, also containing labeled hate speech from Twitter, but we are yet to explore it. You can find the data here: https://github.com/zeerakw/hatespeech. If anyone wants to look into this dataset, and assess its value, it would be very useful. Something else to consider - can these datasets be combined?

### Strategy
What else do we want to do with this?