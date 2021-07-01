## Convert an image or a folder of images to a Quake WAD2 file.

Just drag'n'drop the input folder onto the executable. Accepts all common image formats (anything that is supported by Pillow). Subfolders are included.

For indexed images, the exact pixel indices will be preserved.

Other formats are converted to Quake palette without fullbright colors, with no dithering. The exception is '{'-prefixed textures that use color #255 as transparency, either by preserving the exact color (9f5b53), or by applying their alpha channel with 50% threshold.

TrueColor to indexed conversion is good enough, but not always perfect. I recommend only using it for quick iteration, then converting final textures manually and packing those into a .wad.

Mip sub-levels use nearest resampling (preserves exact colors, but can give blocky results and misses the point sub-mips have in the first place). GL ports do hardware mipmapping, so it doesn't matter at all. However, for software ports it does. With those in mind, you can run a .wad file you've made (or even the final .bsp) through ReMipDLX, a separate program available either as a standalone executable, or as a part of come other .wad managers. ReMip feature is beyond the scope of this script.

## wad2pcx

Also included is a converter back into separate indexed files.
