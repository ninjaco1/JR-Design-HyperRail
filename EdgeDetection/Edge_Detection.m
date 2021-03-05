type sobel
type gCodeReader

filename = input('enter file name:', 's');

im = imread(filename);

image(im);

gray = (0.2989 * double(im(:,:,1)) + 0.5870 * double(im(:,:,2)) + 0.1140 * double(im(:,:,3)))/255;
% gray = (0.2989 * double(im(:,:)) + 0.5870 * double(im(:,:)) + 0.1140 * double(im(:,:)))/255;
edgeIm = sobel(gray, 0.7);

im3 = repmat(edgeIm, [1 1]);

image(im3);

writematrix(im3, 'im3.xlsx');

[row,col] = size(im3);

fileID = fopen('gcode.txt','w');
fprintf(fileID, '%s\n','G90'); 
% fprintf(fileID, '%s\n','G0 X0 Y0');
rapide = 'G0';

% G-Code Generator
for i = 1:col
    for j = 1:row
        if (im3(i,j) == 0)|(j == 1)
            fprintf(fileID, 'T1\nM6\n');
            fprintf(fileID, '%s X%d Y%d\n','G0', i, j);
        elseif im3(i,j) == 255;
            fprintf(fileID, 'T0\nM6\n');
            fprintf(fileID, '%s X%d Y%d\n','G0', i, j);
        end
    end
end
