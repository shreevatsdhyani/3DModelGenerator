#3D Model Generator

This prototype converts a short text prompt (like "a red toy car") into a simple 3D model using OpenAI's Shap-E model. The model generates a `.obj` file, which can be loaded into 3D viewers or used for 3D printing.

## Features
- Converts text prompts to 3D models in `.obj` format.
- Option to view the generated 3D model using the `trimesh` library.
- Simple and lightweight implementation based on OpenAI's Shap-E.

## Setup

Follow these steps to set up the project on your machine:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/3d-text-generator.git
   cd 3d-text-generator
````

2. **Create a virtual environment**:

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:

   * On Windows:

     ```bash
     venv\Scripts\activate
     ```
   * On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Once the setup is complete, you can generate a 3D model from a text prompt by running the following command:

```bash
python main.py --text "a small red chair" --view
```

### Parameters:

* `--text "your prompt"`: The text description of the object you want to generate (e.g., "a red toy car").
* `--view`: If specified, the generated 3D model will automatically be visualized using `trimesh`.

### Output:

* The generated `.obj` file will be saved in the `outputs/` folder, named `text_output.obj`.
* If you specify the `--view` flag, the generated model will also be opened in an interactive 3D viewer.

Example:

```bash
python main.py --text "a small toy car" --view
```

This command will generate a 3D model of a "small toy car" and open it in a 3D viewer.

## Libraries Used

* **`diffusers`**: OpenAI’s Shap-E model to generate 3D models from text prompts.
* **`torch`**: Used to run the Shap-E model on your machine.
* **`trimesh`**: Used to visualize the 3D model in a simple 3D viewer.

## Thought Process

I chose to work on text-to-3D generation to explore AI capabilities in transforming simple text descriptions into 3D objects. OpenAI's Shap-E provides a powerful yet easy-to-use method for generating 3D models from text, which made it an ideal choice for this project. The use of `trimesh` for visualization ensures that the generated models can be quickly viewed and verified.

## Notes

* Make sure to have a stable internet connection, as the Shap-E model needs to be downloaded the first time you run the script.
* The generated `.obj` files can be used with any 3D software or for 3D printing.


