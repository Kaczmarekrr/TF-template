from dataclasses import dataclass
import tensorflow as tf


@dataclass
class TrainConfig:
    # model config
    model_architecture: str = "model_name"
    input_shape = (224, 224, 3)

    # training config
    epochs: int = 50
    lr: float = 5 * 10e-5
    batch_size: int = 32
    loss_fn: tf.keras.losses = tf.keras.losses.BinaryCrossentropy() # type: ignore
    optimizer: tf.keras.optimizers = tf.keras.optimizers.Adam() # type: ignore

