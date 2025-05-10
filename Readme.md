# 3D Model Generator (Text or Image to .obj/.stl)

## 🔍 Overview
This tool generates a simple 3D model from either:
- A short **text prompt** (e.g., "a small toy car")
- An **image** (.jpg/.png of a single object)

It leverages **OpenAI's Shap-E** model for text-to-3D generation and **MiDaS** for depth estimation from images.

## 🛠️ Features
- **Text-to-3D Generation**: Converts text prompts to `.obj` 3D models using OpenAI Shap-E.
- **Image-to-3D Generation**: Generates 3D models from images using depth estimation (MiDaS).
- **Background Removal**: Optional background removal for image input using **rembg** (ideal for isolating objects).
- **3D Visualization**: Visualizes generated models using **trimesh**.
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

```bash
pip install -r requirements.txt
```

## 💻 How to Use

Once the environment is set up and dependencies are installed, you can generate a 3D model using either a text prompt or an image.

### 1. Text-to-3D Generation

To generate a 3D model from a text prompt:

```bash
python main.py --text "a small toy car" --view
```

* **Parameters**:

  * `--text "your prompt"`: Text description of the object to generate.
  * `--view`: Automatically view the generated 3D model (optional).

* **Example**:

  ```bash
  python main.py --text "a red toy car" --view
  ```

This will generate a 3D model of a "red toy car" and open it in a 3D viewer.

### 2. Image-to-3D Generation

To generate a 3D model from an image, ensure the image file is in `.jpg` or `.png` format.

```bash
python main.py --image path/to/image.jpg --view
```

* **Parameters**:

  * `--image "path/to/image.jpg"`: Path to the input image.
  * `--view`: Automatically view the generated 3D model (optional).

### 3. Output

* The generated 3D model will be saved in the `/outputs` directory as `text_output.obj` or `image_output.obj`.
* You can view the model in a 3D viewer if you specify the `--view` flag.

## 🧑‍💻 Code Explanation

* **Text-to-3D**: Utilizes OpenAI's Shap-E model to generate `.obj` files from text descriptions.
* **Image-to-3D**: Uses MiDaS for depth estimation and rembg for background removal, followed by generating 3D point clouds and converting them to `.obj` format.
* **Visualization**: The `trimesh` library is used to open and visualize the 3D models interactively.

## 📄 Libraries Used

* **`diffusers`**: For generating 3D models from text using Shap-E.
* **`torch`**: Deep learning framework required by the Shap-E model.
* **`rembg`**: Background removal tool for cleaning image input.
* **`MiDaS`**: Depth estimation for 3D reconstruction from images.
* **`trimesh`**: For 3D model visualization.
* **`argparse`**: To handle input arguments for the script.

