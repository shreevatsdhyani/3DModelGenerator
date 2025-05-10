
# 3D Model Generator 

## 🔍 Overview
This tool generates a simple 3D model from a **text prompt** using **OpenAI's Shap-E** model.

You can use this script to:
- Generate `.obj` files from short text descriptions (e.g., "a small toy car").
- View the generated 3D model using a simple viewer.

## 🛠️ Features
- **Text-to-3D Generation**: Converts text prompts to `.obj` 3D models using OpenAI Shap-E.
- **3D Visualization**: Visualize generated models using **trimesh**.
- **Output**: Saves `.obj` files in the `/outputs` directory.

## 🔧 Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/3d-text-generator.git
cd 3d-text-generator
````

### 2. Create a Virtual Environment

* **On Windows**:

  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```

* **On macOS/Linux**:

  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. Install Dependencies

Ensure you have the necessary dependencies to run the script:

```bash
pip install -r requirements.txt
```

### 4. Download the Shap-E Model

The first time you run the script, it will automatically download the OpenAI Shap-E model, which is necessary for text-to-3D generation.

## 💻 How to Use

### 1. Generate 3D Model from Text

To generate a 3D model from a text prompt:

```bash
python main.py --text "a small toy car" --view
```

* **Parameters**:

  * `--text "your prompt"`: Text description of the object to generate (e.g., "a red toy car").
  * `--view`: Automatically view the generated 3D model after generation (optional).

#### Example:

```bash
python main.py --text "a red toy car" --view
```

This command will:

* Generate a 3D model based on the text prompt "a red toy car".
* Save the model in the `/outputs` folder as `text_output.obj`.
* Open the model in a 3D viewer using **trimesh**.

### 2. Output

* The generated 3D model will be saved in the `/outputs` directory as `text_output.obj`.
* You can visualize the model by passing the `--view` flag.

## 📄 Libraries Used

* **`diffusers`**: For generating 3D models from text using Shap-E.
* **`torch`**: Deep learning framework used by Shap-E for text-to-3D generation.
* **`trimesh`**: For 3D model visualization.
* **`Pillow`**: Image processing (although not used in the current version, could be for future enhancements like image input).
* **`numpy`**: Numerical operations, used for model generation and depth calculations.
* **`opencv-python`**: Image processing library (used in the original version for image-to-3D, now not needed).
* **`rembg`**: Used for background removal in image input (could be relevant if image-to-3D generation is added back).
* **`open3d`**: For 3D point cloud and mesh handling (again, not in the current version, but useful for further extensions).
* **`onnxruntime`**: For running models in ONNX format (installed for compatibility).

