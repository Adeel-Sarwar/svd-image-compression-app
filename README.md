# SVD Image Compression Web App (Flask + NumPy)

A **machine learning + web development** project demonstrating **Singular Value Decomposition (SVD)** for image compression.  
Users can upload any image, select a compression level (`k`), and instantly view the **compressed result** — powered by Flask and NumPy.

---

## Features

- Upload any image (JPG, PNG, etc.)
- Select compression level (`k`) dynamically
- Compare original vs compressed image side-by-side
- Built using Flask (backend) + Bootstrap (frontend)
- Save compressed images in modern **WebP** format
- Clean modular code (ready to deploy & expand)

---

## What is SVD Compression?

SVD (Singular Value Decomposition) decomposes an image matrix into three matrices:

A=UΣVT

By keeping only the **top k singular values**, we can reconstruct a close approximation of the original image with far fewer data points — reducing file size while maintaining most of the visual quality.

| `k` | Quality | Compression | 
|-----|----------|--------------|
| 20 | Low (blurry) | Very high |
| 50 | Balanced | Good |
| 100 | High | Moderate |
| 200 | Almost original | Low |

---

## Tech Stack

| Layer | Technology |
|-------|-------------|
| Backend | Flask |
| Math Engine | NumPy |
| Image Handling | Pillow (PIL) |
| Frontend | HTML5, Bootstrap 5 |
| Output Format | WebP |
| Deployment | Render / Railway / Localhost |

---

## Installation & Setup

### 1: Clone the Repository
git clone https://github.com/Adeel-Sarwar/svd-image-compression-app.git
cd svd-image-compression-app

### 2: Create a Virtual Environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

### 3: Install Dependencies
pip install -r r.txt

### 4: Run the Flask Server
python __init__.py

### 5: Open in Browser
http://127.0.0.1:5000/
