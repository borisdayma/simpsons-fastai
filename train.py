from fastai.vision import *
import wandb
from wandb.fastai import WandbCallback
import pathlib
import requests
import tarfile
import random

# Initialize W&B project
wandb.init(project="simpsons-fastai")

# Define hyper-parameters
config = wandb.config
config.img_size = random.choice([64, 100])
config.batch_size = 2**random.randrange(8)  # 1, 2, 4... 64, 128
config.epochs = 20
model = random.choice([models.resnet18, models.resnet34])
config.encoder = model.__name__
config.pretrained = random.choice(
    [True, False])  # use pre-trained model and train only last layers
config.dropout = random.uniform(0, 1)
config.one_cycle = random.choice(
    [True, False])  # "1cycle" policy -> https://arxiv.org/abs/1803.09820
config.learning_rate = 10 ** random.uniform(-5, -1)
print('Configuration:\n\n{}'.format(config))

# Download data
PATH_DATA = pathlib.Path('data/simpsons')
if not (PATH_DATA).exists():
    PATH_DATAFILE = pathlib.Path('simpsons.tar.gz')
    URL_DATA = 'https://storage.googleapis.com/wandb-production.appspot.com/mlclass/simpsons.tar.gz'
    r = requests.get(URL_DATA)
    PATH_DATAFILE.open("wb").write(r.content)
    with tarfile.open(PATH_DATAFILE) as archive:
        archive.extractall('data')
    PATH_DATAFILE.unlink()

# Load data
data = (ImageList.from_folder(PATH_DATA)
                 .split_by_folder(train='train', valid='test')
                 .label_from_folder()
                 .transform(get_transforms(), size=config.img_size)
                 .databunch(bs=config.batch_size).normalize())

# Create model
learn = cnn_learner(data,
                    model,
                    pretrained=config.pretrained,
                    ps=config.dropout,
                    metrics=accuracy,
                    callback_fns=WandbCallback)  # Log training in W&B

# Train
if config.one_cycle:
    learn.fit(config.epochs, lr=config.learning_rate)
else:
    learn.fit_one_cycle(config.epochs, max_lr=config.learning_rate)
