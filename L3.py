from PIL import Image, ImageEnhance

# TODO 1: Buka gambar dengan pillow
img_path = 'D:\LOGO\JENO.jpeg'
image = Image.open(img_path)

# TODO 2: Ubah tingkat kecerahan (brightness) dan kontras (contrast)
enhancer = ImageEnhance.Brightness(image)
brightened_image = enhancer.enhance(1.5)

enhancer = ImageEnhance.Contrast(brightened_image)
final_image = enhancer.enhance(1.2)

# TODO 3: Simpan gambar hasil edit
save_path = r'D:\LOGO\hasil_edit.jpg'
final_image.save(save_path)

# TODO 4: Tampilkan
final_image.show()