
## Usage

### Deep Q-Learning

In order to reproduce the model, clone the repository locally and install all the dependencies from the requirements.txt file

* For training use the following command :
```
python main.py --train_dqn --env_name=[ENV NAME] --folder_name=[YOUR NAME]
```
* For testing use the following command :
```
python main.py --test_dqn --env_name=[ENV NAME] --model_path=[YOUR MODEL PATH]
```

### Others
* In order to plot the training progress use the following command :
```
python plot.py ./model/[folder_name]/plot.json
```
The trained model weights come close to 1.1 GB, so please follow the link if you want to download and run inference or continue training:
https://drive.google.com/drive/folders/1UyLMxfvAjJCc2ndwqULfMjysR2xPBVQb?usp=share_link

The outputs from the trained model can be found in the outputs folder. The report contains a comprehensive summary and implementation of the paper, and the presentation contains a brief summary of the same.
