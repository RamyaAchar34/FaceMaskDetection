from tensorflow.keras.models import load_model

model = load_model("mask_no_mask.h5", compile=False)

print("=" * 60)
print("MODEL INPUT SHAPE :", model.input_shape)
print("MODEL OUTPUT SHAPE:", model.output_shape)
print("=" * 60)

model.summary()