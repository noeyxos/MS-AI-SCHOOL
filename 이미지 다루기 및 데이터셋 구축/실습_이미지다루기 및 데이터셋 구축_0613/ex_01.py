import cv2

# 이미지 2장 필요 ( 이미지 불러오기 )
img1 = cv2.imread("image1.jpg", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("image2.jpg", cv2.IMREAD_GRAYSCALE)

# 특징점 검출기 생성
orb = cv2.ORB_create()

# 특징점 검출과 디스크럽터 계산 
keypoint01, descriptor01 = orb.detectAndCompute(img1, None)
keypoint02, descriptor02 = orb.detectAndCompute(img2, None)

print(keypoint01, keypoint02, descriptor01, descriptor02)

# 매칭기 생성
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# 특징점 매칭
matches = bf.match(descriptor01, descriptor02)

# 매칭 결과 정렬 
matches = sorted(matches, key=lambda X: X.distance)

# 매칭 결과 그리기
result = cv2.drawMatches(img1, keypoint01, img2, keypoint02, matches[:10], None, flags =cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

cv2.imshow("Matches", result)
cv2.waitKey(0)


# 매칭 퍼센트 계산 
num_matches = len(matches)
print(num_matches)
num_good_matches = sum(1 for m in matches if m.distance < 50)  # 적절한 거리 임계값 설정
matching_percent = (num_good_matches / num_matches ) * 100
print("매칭 퍼센트: %.2f%%" % matching_percent) # 매칭 퍼센트 : 100.00%
