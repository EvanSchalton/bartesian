from tensorflow.keras.models import Model
from tensorflow.keras.layers import (
    Dense,
    Reshape,
    Conv1D,
    Flatten,
    Dropout,
    Input,
    Concatenate,
)


def create_model(input_length):
    input_layer = Input(shape=(input_length, 1))

    # Create conv layers with different kernel sizes
    conv_layers = []
    for kernel_size in range(1, 6):  # Kernel sizes from 1 to 5
        conv_layer = Conv1D(
            filters=32, kernel_size=kernel_size, activation="relu", padding="same"
        )(input_layer)
        conv_layers.append(conv_layer)

    # Concatenate the outputs of the conv layers
    concatenated = Concatenate()(conv_layers)

    # Flatten before passing to the fully connected layers
    flattened = Flatten()(concatenated)

    # Fully connected layers

    dense = Dense(64, activation="relu")(flattened)
    dropout = Dropout(0.5)(dense)

    # final = Dense(20, activation='softmax')(dropout3)  # Assuming 20 units for output
    final = Dense(20, activation="sigmoid")(dropout)  # Assuming 20 units for output
    output = Reshape((5, 4))(final)

    # Create and compile the model
    model = Model(inputs=input_layer, outputs=output)
    # model.compile(optimizer='adam', loss='categorical_crossentropy', learning_rate=0.001)
    model.compile(optimizer="adam", loss="mean_squared_error")

    return model
