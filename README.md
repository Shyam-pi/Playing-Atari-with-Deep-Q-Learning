# Deep Q Learning for playing Atari

This repository consists of codes for Deep Q Learning implemented for playing Atari games, implemented as a part of my course ENPM667 - Control of Robotics Systems at UMD College Park in Fall 2022

Presentation for the same can be found in this [link](https://docs.google.com/presentation/d/1hrN37tCzoV1zJjXvaIwVWNeviku9rFVG/edit?usp=sharing&ouid=105774915274009785554&rtpof=true&sd=true)

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
