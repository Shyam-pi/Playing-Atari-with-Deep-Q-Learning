
## Usage

```
### Deep Q-Learning
* Training
```
python main.py --train_dqn --env_name=[ENV NAME] --folder_name=[YOUR NAME]
```
* Testing
```
python main.py --test_dqn --env_name=[ENV NAME] --model_path=[YOUR MODEL PATH]
```

### Others
* Plot training progress
```
python plot.py ./model/[folder_name]/plot.json
```
The trained model weights come close to 1.1 GB, so please follow the link if you want to download and run inference or continue training:
https://drive.google.com/drive/folders/1UyLMxfvAjJCc2ndwqULfMjysR2xPBVQb?usp=share_link