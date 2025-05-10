import argparse
import os

def generate_3d_from_text(prompt):
    from diffusers import ShapEPipeline
    import torch

    print(f"Generating 3D model for text prompt: '{prompt}'")
    
    try:
        pipe = ShapEPipeline.from_pretrained("openai/shap-e").to("cpu")
    except Exception as e:
        print("❌ Error loading Shap-E pipeline:", e)
        return None

    try:
        result = pipe(prompt, num_inference_steps=64)
        print("Result keys:", result.keys())  # Debug print
        if 'samples' not in result:
            print("❌ 'samples' key missing in result. Generation failed or model not fully loaded.")
            return None
        mesh = result['samples'][0]
    except Exception as e:
        print("❌ Error during generation:", e)
        return None

    os.makedirs("outputs", exist_ok=True)
    out_path = os.path.join("outputs", "text_output.obj")

    try:
        mesh.save(out_path)
        print(f"✅ 3D model saved to {out_path}")
        return out_path
    except Exception as e:
        print("❌ Failed to save mesh:", e)
        return None

def visualize_3d(path):
    import trimesh
    print(f"Opening 3D viewer for: {path}")
    mesh = trimesh.load(path)
    mesh.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate 3D model from text prompt")
    parser.add_argument("--text", type=str, help="Text prompt for 3D model")
    parser.add_argument("--view", action='store_true', help="View the 3D model")

    args = parser.parse_args()

    if args.text:
        out_model = generate_3d_from_text(args.text)
    else:
        print("Please provide --text input.")
        exit(1)

    if args.view and out_model:
        visualize_3d(out_model)
    elif args.view and not out_model:
        print("⚠️ Skipping visualization due to failed model generation.")
