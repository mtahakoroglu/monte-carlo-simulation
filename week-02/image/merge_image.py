import cv2
img1 = cv2.imread('meeting-probability.png')
img2 = cv2.imread('meeting_plot_n_1000.png')

# Get dimensions
r1, c1, _ = img1.shape
r2, c2, _ = img2.shape

# Resize images to have the same height
target_height = min(r1, r2)  # or use max(r1, r2) if you prefer
img1_resized = cv2.resize(img1, (int(c1 * target_height / r1), target_height))
img2_resized = cv2.resize(img2, (int(c2 * target_height / r2), target_height))

# Concatenate the resized images horizontally
merged_image = cv2.hconcat([img1_resized, img2_resized])

# save the merged image
cv2.imwrite('merged_image.png', merged_image)
# display the merged image
cv2.imshow('Merged Image', merged_image)
cv2.waitKey(0)
cv2.destroyAllWindows()