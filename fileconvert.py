# Author: waturn
# Terminal script to convert images to different formats using Pillow lib

import os, sys, random
from PIL import Image, ImageFilter

OUTPUT_DIR = "out"

def output_path(infile, format):
    # Returns the output path for the converted image
    # Creates the output directory if it doesn't exist
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    filename = os.path.splitext(os.path.basename(infile))[0] + format
    return os.path.join(OUTPUT_DIR, filename)

def print_help():
    # Prints help message for the user
    
    print("Usage: python fileconvert.py <mode> <image1.format> <image2.format> ...\n")
    print("Valid modes:\n\tpng - convert images to PNG")
    print("\tjpg - convert images to JPG")
    print("\twebp - convert images to WEBP")
    print("\tpdf - convert images to PDF")
    print("\tgif - convert images to GIF")
    print("\tbmp - convert images to BMP")
    print("\ttiff - convert images to TIFF")
    print("\n\tthumbnail - create thumbnails of images (128x128)")
    print("\tjumble - jumble pixels in images")
    print("\tblur - blur images")

def convert_to_png():
    # Convert image in argv[2] to png
    # Usage: python fileconvert.py png image-in.png
    
    for infile in sys.argv[2:]:
        outfile = output_path(infile, ".png")
        
        try:
            with Image.open(infile) as im:
                im.convert("RGB").save(outfile, "PNG")
                print(f"Converted {infile} to {outfile}")
        except OSError:
            print("cannot convert", infile)

def convert_to_jpeg():
    # Convert image in argv[2] to jpg
    # Usage: python fileconvert.py jpg image-in.png
    
    for infile in sys.argv[2:]:
        outfile = output_path(infile, ".jpg")
        
        try:
            with Image.open(infile) as im:
                im.convert("RGB").save(outfile, "JPEG")
                print(f"Converted {infile} to {outfile}")
        except OSError:
            print("cannot convert", infile)

def convert_to_webp():
    # Convert image in argv[2] to webp
    # Usage: python fileconvert.py webp image-in.png
    
    for infile in sys.argv[2:]:
        outfile = output_path(infile, ".webp")
        
        try:
            with Image.open(infile) as im:
                im.convert("RGB").save(outfile, "WEBP")
                print(f"Converted {infile} to {outfile}")
        except OSError:
            print("cannot convert", infile)

def convert_to_pdf():
    # Convert image in argv[2] to pdf
    # Usage: python fileconvert.py pdf image-in.png
    
    for infile in sys.argv[2:]:
        outfile = output_path(infile, ".pdf")
        
        try:
            with Image.open(infile) as im:
                im.convert("RGB").save(outfile, "PDF")
                print(f"Converted {infile} to {outfile}")
        except OSError:
            print("cannot convert", infile)

def convert_to_gif():
    # Convert image in argv[2] to gif
    # Usage: python fileconvert.py gif image-in.png
    
    for infile in sys.argv[2:]:
        outfile = output_path(infile, ".gif")
        
        try:
            with Image.open(infile) as im:
                im.convert("RGB").save(outfile, "GIF")
                print(f"Converted {infile} to {outfile}")
        except OSError:
            print("cannot convert", infile)

def convert_to_bitmap():
    # Convert image in argv[2] to bmp
    # Usage: python fileconvert.py bmp image-in.png
    
    for infile in sys.argv[2:]:
        outfile = output_path(infile, ".bmp")
        
        try:
            with Image.open(infile) as im:
                im.convert("RGB").save(outfile, "BMP")
                print(f"Converted {infile} to {outfile}")
        except OSError:
            print("cannot convert", infile)

def convert_to_tiff():
    # Convert image in argv[2] to tiff
    # Usage: python fileconvert.py tiff image-in.png
    
    for infile in sys.argv[2:]:
        outfile = output_path(infile, ".tiff")
        
        try:
            with Image.open(infile) as im:
                im.convert("RGB").save(outfile, "TIFF")
                print(f"Converted {infile} to {outfile}")
        except OSError:
            print("cannot convert", infile)

def convert_to_thumbnail():
    # Create 128x128 thumbnail of image in argv[2]
    # Usage: python fileconvert.py thumbnail image-in.png
    
    size = (128, 128)
    for infile in sys.argv[2:]:
        outfile = output_path(infile, "_thumbnail.jpg")
        try:
            with Image.open(infile) as im:
                im.thumbnail(size)
                im.save(outfile, "JPEG")
                print(f"Created thumbnail for {infile} as {outfile}")
        except OSError:
            print("cannot create thumbnail for", infile)

def jumble():
    # Jumbles pixels in the image in argv[2]
    # Usage: python fileconvert.py jumble image-in.png
    
    for infile in sys.argv[2:]:
        outfile = output_path(infile, "_jumble.jpg")
        
        try:
            with Image.open(infile) as im:
                rand = random.randint(250, 750)
                im.effect_spread(rand).save(outfile, "JPEG")
                print(f"Converted {infile} to {outfile}")
        except OSError:
            print("cannot convert", infile)

def blur():
    # Blurs the image in argv[2]
    # Usage: python fileconvert.py blur image-in.png
    
    for infile in sys.argv[2:]:
        outfile = output_path(infile, "_blur.jpg")
        
        try:
            with Image.open(infile) as im:
                im.filter(ImageFilter.GaussianBlur(radius=20)).save(outfile, "JPEG")
                print(f"Converted {infile} to {outfile}")
        except OSError:
            print("cannot convert", infile)

if __name__ == "__main__":
    # User must define mode in argv[1]
    # Usage: python fileconvert.py <mode> <image>
    # Running python fileconvert.py with no arguments will print help message
    
    if len(sys.argv) < 3:
        print_help()
        sys.exit(1)
        
    mode = sys.argv[1]
    
    match mode:
        case "png":
            convert_to_png()
        case "jpg":
            convert_to_jpeg()
        case "webp":
            convert_to_webp()
        case "pdf":
            convert_to_pdf()
        case "gif":
            convert_to_gif()
        case "bmp":
            convert_to_bitmap()
        case "tiff":
            convert_to_tiff()
        case "thumbnail":
            convert_to_thumbnail()
        case "jumble":
            jumble()
        case "blur":
            blur()
        case _:
            print_help()
            sys.exit(1)