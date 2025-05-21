import cv2

import numpy as np

# Load reference and test images (grayscale)

ref_img = cv2.imread("real.jpg", 0) # Genuine note

test_img = cv2.imread("test.jpg", 0) # Note to test

# Check if images are loaded

if ref_img is None or test_img is None:

 print("❌

Error: Image files not found. Please check 'real.jpg' and 'test.jpg'.")

 exit()

# Create ORB detector

orb = cv2.ORB_create()

# Detect keypoints and descriptors

kp1, des1 = orb.detectAndCompute(ref_img, None)

kp2, des2 = orb.detectAndCompute(test_img, None)

# Create Brute Force matcher and match descriptors

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

matches = bf.match(des1, des2)

# Sort matches by distance (lower distance = better match)

matches = sorted(matches, key=lambda x: x.distance)
# Draw top 20 matches for visualization

result_img = cv2.drawMatches(ref_img, kp1, test_img, kp2, matches[:20], None, 

flags=2)

# Show results

cv2.imshow("Matched Keypoints", result_img)

cv2.waitKey(0)

cv2.destroyAllWindows()

# Authentication decision

print("🔍 Total matches found:", len(matches))

if len(matches) > 50:

 print("✅ The note is likely REAL.")

else:

 print("❌

The note may be FAKE.")
