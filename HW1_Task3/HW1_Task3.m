original_image = imread('lighthouse.png');
grayscale_image = rgb2gray(original_image);
rotated_image = imrotate(original_image, 45);



subplot(2, 2, 1);
imshow(original_image);
title('RGB');

subplot(2, 2, 2);
imshow(grayscale_image);
title('Grayscale');

subplot(2, 2, 3);
imshow(rotated_image);
title('Rotated');

subplot(2, 2, 4);

custom_binLocations = [0, 50, 100, 150, 200, 250];
custom_counts = [0, 1000, 2000, 3000];
[custom_counts,custom_binLocations] = imhist(grayscale_image);
bar(custom_binLocations, custom_counts);
title('Histogram');
xlabel('Pixel Values');
ylabel('Frequency');
