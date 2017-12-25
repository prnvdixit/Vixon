from collections import deque
import numpy as np
import argparse
import cv2
import pygame
import sys
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-b", "--buffer", type=int, default=32, help="max buffer size")
global args
args = vars(ap.parse_args())

crop_img_offset = 15

pts = deque(maxlen=args["buffer"])

#
# gameDisplay = pygame.display.set_mode((640, 480))
# pygame.display.set_caption('hsv_approximation')

# desktopWidth, desktopHeight = pygame.display.Info().current_w, pygame.display.Info().current_h
# display_width = desktopWidth
# display_height = desktopHeight

def track():

    object_set_to_be_detected = 0

    vector = np.zeros((2, 1), dtype=np.int)

    camera = cv2.VideoCapture(0)

    (grabbed, frame) = camera.read()
    frame = np.transpose(frame, (1, 0, 2))

    direction = ""

    pygame.init()
    gameDisplay = pygame.display.set_mode(frame.shape[:2])
    pygame.display.set_caption('hsv_approximation')
    pygame.mouse.set_visible(False)

    while grabbed:
        (grabbed, frame) = camera.read()

        # cv2.imwrite("flag.jpg", frame)
	
        # frame_image = pygame.image.load("flag.jpg")
        # gameDisplay.blit(frame_image, (0, 0))

        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                x_co = pos[0]
                y_co = pos[1]
                # print "Mouse", pos

                img = frame
                # TODO : Compare the results with frame.copy()

                # print path, img

                img_crop = img[y_co - crop_img_offset:y_co + crop_img_offset, x_co - crop_img_offset:x_co + crop_img_offset]
                img = cv2.cvtColor(img_crop, cv2.COLOR_BGR2HSV)

                length = len(img)
                width = len(img[0])

                (max_h, min_h, max_s, min_s, max_v, min_v) = (0, 180, 0, 255, 0, 255)

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

                object_set_to_be_detected = 1

                img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
                # TODO : This won't be required if frame.copy() gave good results

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    # print colourUpper, colourLower
                    sys.exit(0)

                elif event.key == pygame.K_s:
                    # print "Key pressed"
                    pts.clear()
                    object_set_to_be_detected = 1 - object_set_to_be_detected

            else:
                pass

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # gameDisplay.blit(frame, (0, 0))
        # print "1", frame.shape
        frame = np.transpose(frame, (1, 0, 2))
        # print "2", frame.shape
        # print frame.shape
        # pygame.pixelcopy.array_to_surface(gameDisplay, frame)
        pygame.surfarray.blit_array(gameDisplay, frame)
        # print "3", frame.shape
        frame = np.transpose(frame, (1, 0, 2))
        # print "4", frame.shape
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        position_mouse = pygame.mouse.get_pos()
        pygame.draw.rect(gameDisplay, (0, 0, 0), (position_mouse[0] - crop_img_offset, position_mouse[1] - crop_img_offset, 2 * crop_img_offset, 2 * crop_img_offset), 2)

        if object_set_to_be_detected:
            colourLower = np.array([result[0][0], result[0][1], result[0][2]], dtype="uint8")
            colourUpper = np.array([result[1][0], result[1][1], result[1][2]], dtype="uint8")

            frame = imutils.resize(frame, width=640)
            blur_frame = cv2.GaussianBlur(frame, (11, 11), 0)
            hsv = cv2.cvtColor(blur_frame, cv2.COLOR_BGR2HSV)

            # print colourLower, colourUpper
            mask = cv2.inRange(hsv, colourLower, colourUpper)
            mask = cv2.erode(mask, None, iterations=2)
            mask = cv2.dilate(mask, None, iterations=2)

            cv2.imshow("Mask", mask)

            contours = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

            center = None

            if len(contours) > 0:
                c = max(contours, key=cv2.contourArea)
                x, y, w, h = cv2.boundingRect(c)

                center = (x + w / 2, y + h / 2)
                pygame.draw.rect(gameDisplay, (0, 255, 0), (x, y, w, h), 2)
                # cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                pts.appendleft(center)

                if len(pts) > 1:
                    center = np.array(center)
                    center = center.reshape((2, 1))
                    last_element = np.array(pts[1]).reshape((2, 1))
                    vector += (center - last_element)
                    # print vector

            for i in xrange(1, len(pts)):
                if pts[i - 1] is None or pts[i] is None:
                    continue

                # if len(pts) > 8 and i == 1 and pts[-8] is not None:
                #     dX = pts[-8][0] - pts[i][0]
                #     dY = pts[-8][1] - pts[i][1]
                #     (dirX, dirY) = ("", "")
                #
                #
                #     if np.abs(dX) > 10:
                #         dirX = "East" if np.sign(dX) == 1 else "West"
                #     if np.abs(dY) > 10:
                #         dirY = "North" if np.sign(dY) == 1 else "South"
                #
                #     if dirX == "":
                #         direction = dirY
                #     elif dirY == "":
                #         direction = dirX
                #     else:
                #         direction = dirX if abs(dY)/abs(dX) >= 1 else dirY
                #
                #     font = pygame.font.SysFont("timesnewroman", size=25, bold="False", italic="True")
                #     screen_text = font.render(direction, True, (0, 0, 0))
                #     text_position = screen_text.get_rect()
                #     text_position.center = (100, 100)
                #     gameDisplay.blit(screen_text, text_position)

                thickness = int(np.sqrt(args["buffer"] / float(i + 1)) * 3)
                # cv2.line(frame, pts[i - 1], pts[i], (0, 255, 0), thickness)
                pygame.draw.line(gameDisplay, (0, 255, 0), pts[i - 1], pts[i], thickness)

            if np.linalg.norm(vector) > 200:
                # print "Direction", vector
                # print np.linalg.norm(vector)
                dX = vector[0]
                dY = vector[1]

                (dirX, dirY) = ("", "")

                if np.abs(dX) > 150:
                    dirX = "West" if np.sign(dX) == 1 else "East"
                if np.abs(dY) > 150:
                    dirY = "South" if np.sign(dY) == 1 else "North"

                if dirX == "":
                    direction = dirY
                elif dirY == "":
                    direction = dirX
                else:
                    direction = dirX if abs(dY)/abs(dX) >= 1 else dirY

                vector = np.zeros((2, 1), dtype=np.int)
                # print direction

            font = pygame.font.SysFont("timesnewroman", size=25, bold="False", italic="True")
            screen_text = font.render(direction, True, (0, 0, 0))
            text_position = screen_text.get_rect()
            text_position.center = (100, 100)
            gameDisplay.blit(screen_text, text_position)

        pygame.display.update()

        key = cv2.waitKey(1) & 0xFF

        if key == ord('q'):
            # print colourUpper, colourLower
            break

track()