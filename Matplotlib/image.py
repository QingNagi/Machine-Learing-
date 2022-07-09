import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

img = plt.imread(r'test.jpg')
plt.imshow(img)
print(img)
print(img.shape)    # y x轴
fig = plt.figure(2, figsize=(1.5, 1))   # 2为绘制的第二张图片
small = img[200:250, 450:540, :]    # 截取部分图片

plt.imshow(small)
plt.imsave(r'test1.jpg', small)

plt.figure(3, figsize=(6.6, 6.5))
plt.subplot(2, 2, 1)
plt.title('0')
plt.imshow(img)
plt.subplot(222)
plt.title('Y')
img_r = img[:, :, 0]   # 伪彩色r
plt.imshow(img_r, cmap="hot")
plt.colorbar()
plt.subplot(223)
img_r1 = img[:, :, 1]
plt.imshow(img_r1, cmap="winter")
plt.colorbar()
plt.subplot(224)
img_r2 = img[:, :, 2]
plt.imshow(img_r2, plt.cm.gray)

plt.figure(4, figsize=(10, 4))
plt.subplot(131)
plt.hist(img_r2.ravel(), bins=256, range=(0.1, 1), facecolor='k', edgecolor='k')

plt.subplot(132)
plt.imshow(img, clim=(0.1, 0.2))    # 在x轴上获取0.1 - 0.7 的特征
plt.subplot(133)
plt.imshow(img, clim=(0.8, 1))

fig = plt.figure(5)
img1 = plt.imread('test.jpg')
ax = fig.add_subplot(121)
im = plt.imshow(img1)
patch = patches.Circle(xy=(500, 225), radius=225, transform=ax.transData)
im.set_clip_path(patch)   # 用上面提供的剪切图形来剪切一个圆
ax.axis('off')


ax1 = fig.add_subplot(122)
im1 = plt.imshow(img1)
patch1 = patches.Rectangle((300, 25), 446, 500, transform=ax1.transData)
im1.set_clip_path(patch1)
ax1.axis('off')

plt.show()
'''plt.figure(5, figsize=(10, 4))
plt.subplot(131)
plt.imshow(img)
img_a = img.copy()
line_length = img_a.shape[0]*img_a.shape[1]
aline_value = np.linspace(0, 2*np.pi, line_length, dtype='float32')  # 透明值
aline_sin_y = np.sin(aline_value)
img_a = np.place(img_a, img_a==1, aline_sin_y)     # 替换透明度的值
plt.subplot(132)
plt.imshow(img_a)
plt.subplot(133)
aline_cos_y = np.abs(np.cos(line_length))
y_normed = aline_cos_y / aline_cos_y.max()   # 归一化
img_a1 = img.copy()
np.place(img_a1, img_a1==1, y_normed)
plt.imshow(img_a1)'''







