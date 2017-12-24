import cv2
import pygame

pygame.init()

desktopWidth, desktopHeight = pygame.display.Info().current_w, pygame.display.Info().current_h
display_width = 72 * int(desktopWidth/100)
display_height = 95 * int(desktopHeight/100)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('hsv_approximation')


def predict(img):

    length = len(img)
    width = len(img[0])

    (max_h, min_h, max_s, min_s, max_v, min_v) = (0, 255, 0, 255, 0, 255)

    for i in xrange(0, length):
        for j in xrange(0, width):
            (h, s, v) = (img[i][j][0], img[i][j][1], img[i][j][2])
            max_h = max(max_h, h)
            min_h = min(min_h, h)
            max_s = max(max_s, s)
            min_s = min(min_s, s)
            max_v = max(max_v, v)
            min_v = min(min_v, v)

    result = [(min_h, min_s, min_v), (max_h, max_s, max_v)]

    return result

def image_crop(pos, path):
    x_co = pos[0]
    y_co = pos[1]

    img = cv2.imread(path)

    # print path, img

    img_crop = img[y_co-20:y_co+20, x_co-20:x_co+20]

    # print img_crop

    # while True:
    #     cv2.imshow("Uncropped", img_crop)
    #
    #     key = cv2.waitKey(1) & 0xFF
    #     if key == ord('q'):
    #         break


    # cv2.imshow("Cropped", img_crop)

    return predict(img_crop)

def image_load(path):

    print "Image load called"

    frame_image = pygame.image.load(path)

    gameDisplay.blit(frame_image, (0, 0))

    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            return image_crop(pos, path)

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            raise SystemExit
        else:
            return None

    pygame.display.update()