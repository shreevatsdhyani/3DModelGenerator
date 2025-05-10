# 3D Model Generator (Text or Image to .obj/.stl)

## 🔍 Overview
This tool generates a simple 3D model from either:
- A short **text prompt** (e.g., "a small toy car")
- An **image** (.jpg/.png of a single object)

## 🛠️ Features
- Generates `.obj` file using OpenAI Shap-E (text) or MiDaS (image)
- Optional background removal (via rembg)
- Simple 3D visualization
- Outputs stored in `/outputs`

## ✅ How to Use

### 1. Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
