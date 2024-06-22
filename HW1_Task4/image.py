# 200316032 Beyza Sungar

from PIL import Image
import matplotlib.pyplot as plt
 
 
 
original_image = Image.open("lighthouse.png")
grayscale_image = original_image.convert("L")
rotated_image = original_image.rotate(45)
histogram = grayscale_image.histogram()
 

fig, axs = plt.subplots(2, 2, figsize=(8,6))
 

axs[0, 0].imshow(original_image)
axs[0, 0].set_xticks([])
axs[0, 0].set_yticks([])
axs[0, 0].set_title('RGB')
 

axs[0, 1].imshow(grayscale_image, cmap='gray')
axs[0, 1].set_xticks([])
axs[0, 1].set_yticks([])
axs[0, 1].set_title('Grayscale')
 

axs[1, 0].imshow(rotated_image)
axs[1, 0].set_xticks([])
axs[1, 0].set_yticks([])
axs[1, 0].set_title('Rotated')
 

y_values = list(range(0,3001,1000)) 
x_values = list(range(0, 251, 50))
axs[1, 1].set_xticks(x_values)
axs[1, 1].set_yticks(y_values)
axs[1, 1].plot(histogram, color="blue")
axs[1, 1].fill_between(range(len(histogram)), histogram, color="blue") 

plt.tight_layout()
plt.show()
 