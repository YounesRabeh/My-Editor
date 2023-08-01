from PIL import Image, ImageTk

class ImageProcessing:
    def resize_image(self, image_path, width, height):
        original_image = Image.open(image_path)
        resized_image = original_image.resize((width, height), Image.ANTIALIAS)
        return ImageTk.PhotoImage(resized_image)
