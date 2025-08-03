from numpy import argsort
import tensorflow as tf

from clearml import Task
import tensorboard
from my_project.common import common_config
from my_project.common.train_config import TrainConfig
from my_project.common.common_config import CommonConfig
import datetime
from tf.keras.callbacks import (
    EarlyStopping,
    ModelCheckpoint,
    ReduceLROnPlateau,
    TerminateOnNaN,
)
import argparse


def arg_parser() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="ProgramName",
        description="What the program does",
        epilog="Text at the bottom of help",
    )

    parser.add_argument(
        "--log_clearml", default=False, help="Flag for reporting to ClearML"
    )  # option that takes a value

    args = parser.parse_args()

    return args


def train(args):
    train_config = TrainConfig()
    common_config = CommonConfig()

    model: tf.keras.Model = ...  # type: ignore

    train_dataloader = ...
    val_dataloader = ...

    # Callbacks and reporting

    if args.log_clearml:
        task = Task.init(
            project_name=common_config.clearml_project_name, task_name=args.task_name
        )

    log_dir = "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    tensorboard_callback = tf.keras.callbacks.TensorBoard(
        log_dir=log_dir, histogram_freq=1
    )

    callbacks = [
        EarlyStopping(patience=10, verbose=1),
        ReduceLROnPlateau(factor=0.1, patience=10, min_lr=0.0000001, verbose=1),
        ModelCheckpoint(
            "models\\new_yt\\{epoch:02d}-{val_loss:.4f}.hdf5",
            verbose=1,
            save_best_only=True,
            save_weights_only=False,
        ),
        TerminateOnNaN(),
        tensorboard_callback,
    ]

    # model training
    model_history = model.fit(
        x=train_dataloader,
        y=val_dataloader,
        batch_size=train_config.batch_size,
        epochs=train_config.epochs,
        callbacks=callbacks,
    )

    return model_history


if __name__ == "__main__":
    train(arg_parser)
