from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Load the image
img = mpimg.imread("/content/ph2.jpeg")  # Replace with your image path

# Display the image
plt.imshow(img)
plt.axis('off')  # Hide axes for better view
plt.show()

def generate_caption(image_path):
    try:
        # Load the BLIP processor and model
        processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

        # Open the input image
        image = Image.open(image_path)

        # Preprocess the image and generate a caption
        inputs = processor(image, return_tensors="pt")
        outputs = model.generate(**inputs)
        caption = processor.decode(outputs[0], skip_special_tokens=True)

        return caption

    except Exception as e:
        return f"Error: {e}"

# Example usage
image_path = "/content/ph2.jpeg" # Replace with your image file path
caption = generate_caption(image_path)
print(f"Generated Caption: {caption}")
