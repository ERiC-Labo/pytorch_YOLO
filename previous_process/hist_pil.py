from PIL import Image, ImageOps

image_path = "/home/ericlab/tsuchida/2022_07/annotation/real_data_t_pipe_ano_again/images/7_14_4_2_48.jpg"
im = Image.open(image_path)
im = im.convert("YCbCr")
yy, cb, cr = im.split()

yy = ImageOps.equalize(yy);
im = Image.merge("YCbCr", (yy, cb, cr))

im = im.convert("RGB")
im.show()
# im.save(sys.argv[2])