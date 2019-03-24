# hate_speech_detector

## Project Status

We have built a few fully working hate speech detection models. This project is currently in hibernation, in that there's not an active use case at the moment but the models are ready to go. Every once in a while we'll tweak the models a bit but in general, there is not active development on this project. If you know of a possible application, please reach out to us. Also, if you're interested in helping, we're always looking for help, whether more data, more models, or any other interesting component of hate speech detection. If you're interested in using or working on this model, feel free to reach out to the Slack channel (#p-hate-speech) or Julius Simonelli (jss367 in Slack).

## Data

We are currently working with the data collected by [Davidson et al.](https://aaai.org/ocs/index.php/ICWSM/ICWSM17/paper/view/15665) for their research on hate speech detection. The dataset contains tweets that are labeled as either hate speech, offensive language, or neither. The data were pulled from [Hatebase.org](https://www.hatebase.org/), an organization that collects instances of potential hate speech. The data were then labeled using [CrowdFlower](https://www.crowdflower.com/), which uses non-specialists to clean and label data. Each tweet was reviewed by three or more people and a majority-wins approach was taken when there was disagreement.

All data used in this analysis is stored in the [data](https://github.com/Data4Democracy/hate_speech_detector/tree/master/data) folder of [this repository](https://github.com/Data4Democracy/hate_speech_detector). The original source of the data is: https://github.com/t-davidson/hate-speech-and-offensive-language

The paper by Davidson et al. can be found here:
Thomas Davidson, Dana Warmsley, Michael Macy, Ingmar Weber. 2017. "[Automated Hate Speech Detection and the Problem of Offensive Language](https://aaai.org/ocs/index.php/ICWSM/ICWSM17/paper/view/15665)". Proceedings of the 11th International AAAI Conference on Web and Social Media (ICWSM).

## Demo REST API

A REST API has been designed to demo the functionality of a basic model. The code will train a basic model as defined in the data_science.py and use this model to make predictions. To get the current IP address, ask in the Data for Democracy #p-hate-speech Slack channel.

### Installation (Docker)

Navigate to the hate_speech_detector/ directory and build the container:

```shell
docker build -t [container-name] ./app
```

### Usage

When you run the container, you must also expose the port 8000. For example:


```shell
docker run -p 8000:8000 -t [container-name]
```

#### Labels

Labels are Hate = 0, Offensive = 1, Not Offensive = 2.

#### API Endpoints

- /label

Then, the API can be called to predict the label on new text data via:

```shell
curl -H "Content-Type: application/json" -X POST -d '{"text":"Text that might be offensive or hateful... or not."}' http://0.0.0.0:8000/label
```

Output Ex:

```shell
{
  "label": 2, 
  "text": "Text that might be offensive or hateful... or not."
}

```

In this case, "text" is the input text and label is the predicted label from the model.


- /demo

You may also see the model predict on held out test set values via:

```shell
curl http://0.0.0.0:8000/demo
```
Output Ex:

```shell
{
  "label": 2, 
  "text": "#stateoftheunion would last 15mins if they let the President talk all that standing up clapping is for the birds", 
  "true": 2
}
```

Here, "text" is the text input, "label" is the predicted label from the model, and "true" is the actual label given by a human. 

### Deploy with prebuilt containers via docker-compose


```shell
docker-compose -f docker-compose-prebuilt.yml up
```

At this point, if you set this up on AWS, then you could navigate to

```shell
[your aws ip]/demo
```

in your browser to see the demo.

## To Do:

### Classifier
There are currently two Jupyter Notebooks containing models to classify the data, but both could be greatly improved. Please feel free to take a look and let us know if you make any improvements!

### Data preprocessing
There is currently very little preprocessing done on this data. Would someone be interested in creating some useful categories for machine learning and plugging them back into the models? My guess is feature engineering has the most potential to improve the model.


### Front End

A front end for the demo app which can demo random elements of the test set or allow the user to input their own text.

### Dataset
The Davidson et al. paper remarked on some possible mislabelings in the dataset. Is mislabeling common in the dataset? Fixing any labels would definitely improve our ability to create a classifier. How big a problem is this? Does someone want to look at some of the misclassifications and see if any are incorrectly labeled?

Also, there's a second data source, also containing labeled hate speech from Twitter, but we are yet to explore it. You can find the data here: https://github.com/zeerakw/hatespeech. If anyone wants to look into this dataset and assess its value, it would be very useful. Something else to consider - can these datasets be combined?

### Strategy
What else do we want to do with this?
