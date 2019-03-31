import cv2
import numpy as np



if __name__ == "__main__":

    base_image_file = input("image name")
    template_name = input("template file name")

    detection_threshold = input("detection threshold")

    input_img1_grayscale = cv2.imread(base_image_file, cv2.IMREAD_GRAYSCALE)
    input_img1_full_color = cv2.imread(base_image_file, cv2.IMREAD_COLOR)

    rows_full_img, cols_full_img = input_img1_grayscale.shape

    target1_img1 = cv2.imread(template_name, cv2.IMREAD_GRAYSCALE)
    rows_target1, cols_target1 = target1_img1.shape

    mm_height = rows_full_img - rows_target1 + 1
    mm_width = cols_full_img - cols_target1 + 1

    matching_map = np.zeros((mm_height,mm_width))


    for i in range(0, mm_height):
        for j in range(0, mm_width):

            test = input_img1_grayscale[i:i+rows_target1,j:j+cols_target1].copy()

            result = (test - target1_img1.copy())

            result = result**2

            result = result.sum()

            target_sum = target1_img1.sum()

            res = result/target_sum

            matching_map[i,j] = res * 255


    number_of_targets = 0

    for i in range(0, mm_height):
        for j in range(0, mm_width):

            if matching_map[i,j] < float(detection_threshold):
                number_of_targets +=1


    print(number_of_targets)

    if number_of_targets == 0:
        # Create a black image
        imgFound = np.zeros((40, 245, 3), np.uint8)

        # Write the text
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(imgFound, "TARGET NOT FOUND", (5,30), font, 1, (0,255,255),2)

        # Display the image
        cv2.imshow("Result", imgFound)

    for i in range(0,number_of_targets):
        # Create a black image
        imgFound = np.zeros((40, 245, 3), np.uint8)

        # Write the text
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(imgFound, "TARGET FOUND", (5,30), font, 1, (0,255,0),2)

        # Display the image
        cv2.imshow("Result", imgFound)

    cv2.imshow("Original",np.uint8(input_img1_full_color))
    cv2.imshow("matching map",np.uint8(matching_map))

    cv2.waitKey(0)
