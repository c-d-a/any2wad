# Quake WAD2 Converter

Allows packing images or image folders into a .wad file, or unpacking a .wad/.bsp file into separate images. Accepts all common image formats.

## Usage: 
Drag'n'drop onto one of the executables:  
![dragndrop](https://user-images.githubusercontent.com/55441216/189548047-b06a4dd8-3445-4ad5-8edb-c056bb4dfe1e.gif)  
Or send it to an executable through the context menu:  
![sendto](https://user-images.githubusercontent.com/55441216/189548087-0505d59a-5e80-4552-9829-7dd094a3046b.gif)  

## Notes:  
For indexed images, the exact pixel indices will be preserved.

Other formats are converted to Quake palette without fullbright colors, with no dithering. The exception is '{'-prefixed textures that use color #255 as transparency, either by preserving the exact color (9f5b53), or by applying their alpha channel with 50% threshold.

Mip sub-levels use nearest resampling.
