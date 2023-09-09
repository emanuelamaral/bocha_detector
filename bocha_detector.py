import cv2
import numpy as np


class BochaDetector:
    def __init__(self, image_path):
        self.img = cv2.imread(image_path)
        self.threshold_value = 127
        self.canny_threshold = 100
        self.gray_img = cv2.cvtColor(self.img.copy(), cv2.COLOR_RGB2GRAY)

    def on_trackbar_threshold(self, value):
        self.threshold_value = value

        _, binary_img_gray_scale = cv2.threshold(self.gray_img, self.threshold_value, 255, cv2.THRESH_TOZERO_INV)
        cv2.imshow('Imagem Binarizada em Escala de Cinza', binary_img_gray_scale)

        circles = self.detect_circles(binary_img_gray_scale)
        img_with_circles = self.draw_circles(self.img.copy(), circles)

        cv2.imshow("Circulos - Threshold", img_with_circles)

        # _, binary_img = cv2.threshold(self.img, self.threshold_value, 255, cv2.THRESH_BINARY)
        # cv2.imshow('Imagem Binarizada com todos os canais', binary_img)

    def on_trackbar_canny(self, value):
        self.canny_threshold = value

        # blurred_img = cv2.GaussianBlur(self.gray_img, (5, 5), 0)
        canny_img = cv2.Canny(self.gray_img, self.canny_threshold, self.canny_threshold * 2)

        cv2.imshow("Imagem com Filtro Canny", canny_img)

        circles = self.detect_circles(canny_img)
        img_with_circles = self.draw_circles(self.img.copy(), circles)
        #
        cv2.imshow("Circulos - Canny", img_with_circles)


    @staticmethod
    def detect_circles(binary_img):
        circles = cv2.HoughCircles(binary_img, cv2.HOUGH_GRADIENT, dp=1, minDist=20, param1=50, param2=30, minRadius=10, maxRadius=50)
        if circles is not None:
            return np.uint16(np.around(circles[0]))
        return []

    @staticmethod
    def draw_circles(img, circles):
        img_with_circles = img.copy()
        for circle in circles:
            x, y, r = circle
            cv2.circle(img_with_circles, (x, y), r, (0, 255, 0), 2)  # Desenhe o círculo
            cv2.circle(img_with_circles, (x, y), 2, (0, 0, 255), 3)  # Desenhe o centro
        return img_with_circles

    def run(self):
        cv2.imshow('Imagem Original', self.img)
        cv2.createTrackbar('Threshold', 'Imagem Original', self.threshold_value, 255, self.on_trackbar_threshold)
        cv2.createTrackbar('Canny Threshold', 'Imagem Original', self.canny_threshold, 200, self.on_trackbar_canny)

        while True:
            key = cv2.waitKey(1) & 0xFF

            if key == ord('q'):
                break

        cv2.destroyAllWindows()


if __name__ == '__main__':
    bocha_detector = BochaDetector('bocha.jpg')
    bocha_detector.run()