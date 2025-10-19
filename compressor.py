import numpy as np
from PIL import Image
import io

def compress_image(image_bytes, k):
    """
    Compress an image using SVD with top-k singular values.
    Args:
        image_bytes: uploaded image in bytes
        k: number of singular values to keep (int)
    Returns:
        compressed_image_bytes: compressed image as bytes (JPEG)
    """

    # Load image from bytes
    image = Image.open(io.BytesIO(image_bytes))
    image = image.convert('RGB')  # Ensure RGB format
    img_array = np.array(image, dtype=np.float64)

    # Split into R, G, B channels
    channels = []
    for i in range(3):
        U, S, Vt = np.linalg.svd(img_array[:, :, i], full_matrices=False)
        S = np.diag(S[:k])
        compressed_channel = np.dot(U[:, :k], np.dot(S, Vt[:k, :]))
        channels.append(np.clip(compressed_channel, 0, 255))

    # Stack channels back together
    compressed_img = np.stack(channels, axis=2).astype(np.uint8)
    compressed_pil = Image.fromarray(compressed_img)

    # Save to bytes
    compressed_bytes_io = io.BytesIO()
    compressed_pil.save(compressed_bytes_io, format='WEBP', quality=90, method=6)
    compressed_bytes_io.seek(0)
    return compressed_bytes_io
