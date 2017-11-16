# Data Definitions

## `twitter-hate-speech.csv`
This file was copied from a [data.world](https://data.world/) repository: [crowdflower](https://data.world/crowdflower)/[Hate Speech Identification](https://data.world/crowdflower/hate-speech-identification/)/[twitter-hate-speech-classifier-DFE-a845520.csv](https://data.world/crowdflower/hate-speech-identification/workspace/file?filename=twitter-hate-speech-classifier-DFE-a845520.csv)

_Open Issue_: What do the columns mean?

## `twitter-hate-speech2.csv`
This file was copied from [Davidson et al.](https://aaai.org/ocs/index.php/ICWSM/ICWSM17/paper/view/15665)'s [labeled_data.csv](https://github.com/t-davidson/hate-speech-and-offensive-language/blob/master/data/labeled_data.csv). The same data is also in a [data.world](https://data.world/) repository: [thomasrdavidson](https://data.world/thomasrdavidson/)/[Hate Speech and Offensive Language](https://data.world/thomasrdavidson/hate-speech-and-offensive-language/)/[labeled_data.csv](https://data.world/thomasrdavidson/hate-speech-and-offensive-language/workspace/file?filename=labeled_data.csv)

The file contains 5 columns:

`count` = number of CrowdFlower users who coded each tweet (min is 3, sometimes more users coded a tweet when judgments were determined to be unreliable by CF).

`hate_speech` = number of CF users who judged the tweet to be hate speech.

`offensive_language` = number of CF users who judged the tweet to be offensive.

`neither` = number of CF users who judged the tweet to be neither offensive nor non-offensive.

`class` = class label for majority of CF users.
  0 - hate speech
  1 - offensive  language
  2 - neither
