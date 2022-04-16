from PIL import Image, ImageCms, ImageEnhance

im_in = Image.open('./image.png').convert('RGB')

srgb_p = ImageCms.createProfile("sRGB")
lab_p = ImageCms.createProfile("LAB")

rgb2lab = ImageCms.buildTransformFromOpenProfiles(srgb_p, lab_p, "RGB", "LAB")
lab = ImageCms.applyTransform(im_in, rgb2lab)

l, a, b = lab.split()

lst_l = list(l.getdata())
lst_a = list(a.getdata())
lst_b = list(b.getdata())

lst_out = []

for i in range(len(lst_a)):
    lst_out.append((lst_l[i] + lst_a[i] + lst_b[i]) / 3)

im_out = Image.new('L', im_in.size)
im_out.putdata(lst_out)

enhancer = ImageEnhance.Contrast(im_out)

factor = 3
im_out = enhancer.enhance(factor)

im_in.show()
im_out.show()