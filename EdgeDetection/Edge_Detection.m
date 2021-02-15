type sobel

im = imread('path.jpg');

image(im);

gray = (0.2989 * double(im(:,:,1)) + 0.5870 * double(im(:,:,2)) + 0.1140 * double(im(:,:,3)))/255;

edgeIm = sobel(gray, 0.7);

im3 = repmat(edgeIm, [1 1 3]);

image(im3);

fprint();