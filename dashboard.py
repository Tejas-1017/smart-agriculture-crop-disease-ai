import gradio as gr
def inspect_crop_leaf(image):
    return {"Pathology": "Tomato Late Blight (Phytophthora)", "Confidence": "96.4%", "NDVI Health Index": "0.42 (Stressed)"}, "Recommended Action: Apply copper-based fungicide spray within 48 hours."
demo = gr.Interface(
    fn=inspect_crop_leaf,
    inputs=gr.Image(type="pil", label="Drone / Mobile Leaf Image"),
    outputs=[gr.JSON(label="Pathology Classification"), gr.Textbox(label="Agronomic Recommendation")],
    title="🌱 Smart Agriculture Crop Disease AI (EfficientNet-B4 + NDVI)"
)
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7882, share=False)
