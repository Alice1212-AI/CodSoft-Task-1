#CodSoft-Task-1-Image-Captioning-
Image Captioning Using BLIP:
This project uses the BLIP (Bootstrapped Language-Image Pretraining) model to generate captions for images. It leverages the Hugging Face transformers library to process and analyze images, automatically producing descriptive text.

Features:
✅ Loads and displays images using matplotlib
✅ Generates captions using BLIP (BlipProcessor & BlipForConditionalGeneration)
✅ Supports various image formats
✅ Simple and easy-to-use script

Install dependencies:
pip install transformers pillow matplotlib

Usage:
Place your image in the working directory.
Update the image_path in generate_caption(image_path).
Run the script:
python script.py
The generated caption will be printed in the console.

Example Output:
Input Image:
(Displayed using Matplotlib)

Generated Caption:
"A dog sitting on the grass with a ball."

Dependencies:
* transformers
* PIL (Pillow)
* matplotlib
