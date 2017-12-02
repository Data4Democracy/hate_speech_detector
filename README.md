# hate_speech_detector

## Data

We are currently working with the data collected by [Davidson et al.](https://aaai.org/ocs/index.php/ICWSM/ICWSM17/paper/view/15665) for their research on hate speech detection. The dataset contains tweets that are labeled as either hate speech, offensive language, or neither. The data were pulled from [Hatebase.org](https://www.hatebase.org/), an organization that collects instances of potential hate speech. The data were then labeled using [CrowdFlower](https://www.crowdflower.com/), which uses non-specialists to clean and label data. Each tweet was reviewed by three or more people and a majority-wins approach was taken when there was disagreement.

All data used in this analysis is stored in the [data](https://github.com/Data4Democracy/hate_speech_detector/tree/master/data) folder of [this repository](https://github.com/Data4Democracy/hate_speech_detector). The original source of the data is: https://github.com/t-davidson/hate-speech-and-offensive-language

The paper by Davidson et al. can be found here:
Thomas Davidson, Dana Warmsley, Michael Macy, Ingmar Weber. 2017. "[Automated Hate Speech Detection and the Problem of Offensive Language](https://aaai.org/ocs/index.php/ICWSM/ICWSM17/paper/view/15665)". Proceedings of the 11th International AAAI Conference on Web and Social Media (ICWSM).

## Demo REST API

A REST API has been designed to demo the functionality of a basic model. 

### Installation

```shell
pip install -r requirements.txt
```

TODO: Docker, dockerhub. 

### Usage

To run, you must set the environment variable "TRAINING_DATA_LOCATION". Then, from the hate_speech_detector directory, type

```shell
python -m app.app
```
Then, use the configured IP displayed. One example usage is to call the /demo endpoint to see the model predicting on a held out test example. Real time predictions can be done via the /label endpoint.

```shell
curl -H "Content-Type: application/json" -X POST -d '{"text":"Text that might be offensive or hateful... or not."}' http://127.0.0.1:5000/label
```

## To Do:

### Classifier
There are currently two Jupyter Notebooks containing models to classify the data, but both could be greatly improved. Please feel free to take a look and let us know if you make any improvements!

### Data preprocessing
There is currently very little preprocessing done on this data. Would someone be interested in created some useful categories for machine learning and plugging them back into the models? My guess is feature engineering has the most potential to improve the model.


### Front End

A front end for the demo app which can demo random elements of the test set or allow the user to input their own text.

### Dataset
The Davidson et al. paper remarked on some possible mislabelings in the dataset. Is mislabeling common in the dataset? Fixing any labels would definitely improve our ability to create a classifier. How big a problem is this? Does someone want to look at some of the misclassifications and see if any are incorrectly labeled?

Also, there's a second data source, also containing labeled hate speech from Twitter, but we are yet to explore it. You can find the data here: https://github.com/zeerakw/hatespeech. If anyone wants to look into this dataset, and assess its value, it would be very useful. Something else to consider - can these datasets be combined?

### Strategy
What else do we want to do with this?
