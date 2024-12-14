from keras.models import load_model  # TensorFlow es necesario para Keras
from PIL import Image, ImageOps  # Pillow para manipulación de imágenes
import numpy as np

def get_class(model_path, labels_path, image_paht):
    np.set_printoptions(suppress=True)

    # Cargar el modelo y las etiquetas
    model = load_model(model_path, compile=False)
    class_names = open(labels_path, "r", encoding="utf-8").readlines()

    # Crear array con forma esperada por el modelo
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Procesar la imagen
    image = Image.open(image_paht).convert("RGB")
    size = (224, 224)  # Tamaño esperado por el modelo
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
    image_array = np.asarray(image)

    # Normalizar la imagen
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    # Validar dimensiones
    if normalized_image_array.shape != (224, 224, 3):
        raise ValueError(
            f"La imagen tiene un tamaño incorrecto: {normalized_image_array.shape}. Debe ser (224, 224, 3)."
        )

    data[0] = normalized_image_array  # Asignar al array de entrada

    # Realizar predicción
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # Retornar resultado como string
    return f"Clase: {class_name.strip()}, Confianza: {confidence_score:.2f}"