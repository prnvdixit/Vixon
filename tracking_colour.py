from collections import deque
import numpy as np
import argparse
import cv2
import pygame
import sys
import imutils
import pyautogui
import os
from collections import Counter

import new_temp
import temp
import pyautogui_template

os.environ['SDL_VIDEO_WINDOW_POS'] = '{0},{1}'.format(0, 0)

ap = argparse.ArgumentParser()
ap.add_argument("-b", "--buffer", type=int, default=32, help="max buffer size")
args = vars(ap.parse_args())

crop_img_offset = 15

pts = deque(maxlen=args["buffer"])

keyboard_img = pygame.image.load("keyboard.png")


# def press_keyboard():
    # print pyautogui.position()


#
# gameDisplay = pygame.display.set_mode((640, 480))
# pygame.display.set_caption('hsv_approximation')

# desktopWidth, desktopHeight = pygame.display.Info().current_w, pygame.display.Info().current_h
# display_width = desktopWidth
# display_height = desktopHeight


def track():

    object_set_to_be_detected = 0
    prevent_object_set_to_be_detected = 0

    vector = np.zeros((2, 1), dtype=np.int)

    camera = cv2.VideoCapture(0)

    (grabbed, frame) = camera.read()
    frame = np.transpose(frame, (1, 0, 2))

    direction = ""

    pygame.init()
    game_display = pygame.display.set_mode(frame.shape[:2])
    pygame.display.set_caption('hsv_approximation')
    pygame.mouse.set_visible(False)

    result = []
    key_buffer = []

    while grabbed:
        # print pyautogui.position()
        (grabbed, frame) = camera.read()

        frame = cv2.flip(frame, 1)

        # cv2.imwrite("flag.jpg", frame)

        # frame_image = pygame.image.load("flag.jpg")
        # gameDisplay.blit(frame_image, (0, 0))

        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    x_co = pos[0]
                    y_co = pos[1]
                    # print "Mouse", pos

                    img = frame
                    # print path, img

                    img_crop = img[y_co - crop_img_offset:y_co + crop_img_offset,
                               x_co - crop_img_offset:x_co + crop_img_offset]
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

                if event.button == 3:
                    pos = pygame.mouse.get_pos()
                    x_co = pos[0]
                    y_co = pos[1]
                    # print "Mouse", pos

                    img = frame
                    # print path, img

                    img_crop = img[y_co - crop_img_offset:y_co + crop_img_offset,
                               x_co - crop_img_offset:x_co + crop_img_offset]
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

                    result_prevent = [(min_h, min_s, min_v), (max_h, max_s, max_v)]

                    img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)

                    prevent_object_set_to_be_detected = 1
            # print result

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    # print colour_upper, colour_lower
                    sys.exit(0)

                elif event.key == pygame.K_s:
                    # print "Key pressed"
                    pts.clear()
                    object_set_to_be_detected = 1 - object_set_to_be_detected
                    direction = ""

                elif event.key == pygame.K_k:
                    temp.mode = "virtual_keyboard"

                elif event.key == pygame.K_p:
                    temp.mode = "presentation"

                elif event.key == pygame.K_m:
                    temp.mode = "media"

                elif event.key == pygame.K_r:
                    temp.mode = "reading"

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # gameDisplay.blit(frame, (0, 0))
        # print "1", frame.shape
        frame = np.transpose(frame, (1, 0, 2))
        # print "2", frame.shape
        # print frame.shape
        # pygame.pixelcopy.array_to_surface(gameDisplay, frame)
        pygame.surfarray.blit_array(game_display, frame)
        # print "3", frame.shape
        frame = np.transpose(frame, (1, 0, 2))
        # print "4", frame.shape
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        if temp.mode == "virtual_keyboard":
            # print keyboard_img.get_rect().size
            # print "Frame", frame.shape[0], "Keyboard", keyboard_img.get_rect().size[1]
            # OpenCV's frame is of the numpy-form (y, x); But PyGame's loaded image is as (x, y)
            game_display.blit(keyboard_img, (0, frame.shape[0] - keyboard_img.get_rect().size[1]))
            # game_display.blit(keyboard_img, (0, 0))

        else:
            position_mouse = pygame.mouse.get_pos()
            pygame.draw.rect(
                game_display, (0, 0, 0), (position_mouse[0] - crop_img_offset,
                    position_mouse[1] - crop_img_offset,
                    2 * crop_img_offset,
                    2 * crop_img_offset), 2
            )


        if temp.mode == "reading":
            if direction == "West":
                action = "page_down"
            elif direction == "East":
                action = "page_up"
            elif direction == "North":
                action = "zoom_in"
            elif direction == "South":
                action = "zoom_out"
            else:
                action = None
            if action != None:
                pyautogui_template.reading_controls(action)
                pts.clear()
                direction = ""
                action = None

        elif temp.mode == "presentation":
            # print direction
            if direction == "West":
                action = "move_forward"
            elif direction == "East":
                action = "move_back"
            elif direction == "North":
                action = "start"
            elif direction == "South":
                action = "stop"
            else:
                action = None
            if action != None:
                pyautogui_template.presentation_controls(action)
                pts.clear()
                direction = ""
                action = None

        elif temp.mode == "media":
            # print direction
            if direction == "West":
                action = "move_forward"
            elif direction == "East":
                action = "move_back"
            elif direction == "North":
                action = "vol_up"
            elif direction == "South":
                action = "vol_down"
            else:
                action = None
            if action != None:
                pyautogui_template.media_controls(action)
                pts.clear()
                direction = ""
                action = None

        if prevent_object_set_to_be_detected:
            colour_lower_prevent = np.array([result_prevent[0][0], result_prevent[0][1], result_prevent[0][2]], dtype="uint8")
            colour_upper_prevent = np.array([result_prevent[1][0], result_prevent[1][1], result_prevent[1][2]], dtype="uint8")

            frame = imutils.resize(frame, width=640)
            blur_frame = cv2.GaussianBlur(frame, (11, 11), 0)
            hsv = cv2.cvtColor(blur_frame, cv2.COLOR_BGR2HSV)

            # print colour_lower, colour_upper
            mask = cv2.inRange(hsv, colour_lower_prevent, colour_upper_prevent)
            mask = cv2.erode(mask, None, iterations=2)
            mask = cv2.dilate(mask, None, iterations=2)


            # blur = cv2.medianBlur(mask, 15)
            # blur = cv2.GaussianBlur(blur, (5, 5), 0)
            # thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
            # contours = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)[1]


            cv2.imshow("Mask", mask)

            contours = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

            center = None

            if len(contours) > 0:
                pts.clear()
                object_set_to_be_detected = 0
            else:
                if result != []:
                    object_set_to_be_detected = 1

        if object_set_to_be_detected:
            colour_lower = np.array([result[0][0], result[0][1], result[0][2]], dtype="uint8")
            colour_upper = np.array([result[1][0], result[1][1], result[1][2]], dtype="uint8")

            frame = imutils.resize(frame, width=640)
            blur_frame = cv2.GaussianBlur(frame, (11, 11), 0)
            hsv = cv2.cvtColor(blur_frame, cv2.COLOR_BGR2HSV)

            # print colour_lower, colour_upper
            mask = cv2.inRange(hsv, colour_lower, colour_upper)
            mask = cv2.erode(mask, None, iterations=2)
            mask = cv2.dilate(mask, None, iterations=2)

            cv2.imshow("Mask", mask)

            contours = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

            center = None

            if len(contours) > 0:
                c = max(contours, key=cv2.contourArea)
                x, y, w, h = cv2.boundingRect(c)

                center = (x + w / 2, y + h / 2)
                # cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                pts.appendleft(center)

                if temp.mode == "virtual_keyboard":
                    pygame.draw.circle(game_display, (0, 120, 255), center, 10, 5)
                    pygame.draw.line(game_display, (0, 0, 0), (center[0]-50,center[1]), (center[0]+50,center[1]), 1)
                    pygame.draw.line(game_display, (0, 0, 0), (center[0],center[1]-50), (center[0],center[1]+50), 1)

                    key_buffer.append(new_temp.get_key(center))

                    max_occuring = Counter(key_buffer[-20:]).most_common(1)
                    print key_buffer, max_occuring

                    if len(key_buffer) > 20:
                        key_buffer = key_buffer[-20:]

                    if max_occuring != [] and max_occuring[0][1] > 15 and max_occuring[0][0] is not None:
                        pyautogui_template.key_press(max_occuring[0][0])
                        pygame.draw.circle(game_display, (0, 0,0), center, 15, 10)
                        key_buffer = []

                else:
                    pygame.draw.rect(game_display, (0, 255, 0), (x, y, w, h), 2)
                    pygame.draw.rect(game_display, (0, 0, 0), (center[0], center[1], 10, 10))

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
                #     d_x = pts[-8][0] - pts[i][0]
                #     d_y = pts[-8][1] - pts[i][1]
                #     (dir_x, dir_y) = ("", "")
                #
                #
                #     if np.abs(d_x) > 10:
                #         dir_x = "East" if np.sign(d_x) == 1 else "West"
                #     if np.abs(d_y) > 10:
                #         dir_y = "North" if np.sign(d_y) == 1 else "South"
                #
                #     if dir_x == "":
                #         direction = dir_y
                #     elif dir_y == "":
                #         direction = dir_x
                #     else:
                #         direction = dir_x if abs(d_y)/abs(d_x) >= 1 else dir_y
                #
                #     font = pygame.font.SysFont("timesnewroman", size=25, bold="False", italic="True")
                #     screen_text = font.render(direction, True, (0, 0, 0))
                #     text_position = screen_text.get_rect()
                #     text_position.center = (100, 100)
                #     gameDisplay.blit(screen_text, text_position)

                thickness = int(np.sqrt(args["buffer"] / float(i + 1)) * 1.5)
                # cv2.line(frame, pts[i - 1], pts[i], (0, 255, 0), thickness)
                pygame.draw.line(game_display, (0, 255, 0), pts[i - 1], pts[i], thickness)

            if np.linalg.norm(vector) > 200:
                # print "Direction", vector
                # print np.linalg.norm(vector)
                d_x = vector[0]
                d_y = vector[1]

                (dir_x, dir_y) = ("", "")

                if np.abs(d_x) > 150:
                    dir_x = "West" if np.sign(d_x) == 1 else "East"
                if np.abs(d_y) > 150:
                    dir_y = "South" if np.sign(d_y) == 1 else "North"

                if dir_x == "":
                    direction = dir_y
                elif dir_y == "":
                    direction = dir_x
                else:
                    direction = dir_x if abs(d_y) / abs(d_x) >= 1 else dir_y

                vector = np.zeros((2, 1), dtype=np.int)
                # print direction

            font = pygame.font.SysFont("timesnewroman", size=25, bold="False", italic="True")
            screen_text = font.render(direction, True, (0, 0, 255))
            text_position = screen_text.get_rect()
            text_position.center = (350, 450)
            game_display.blit(screen_text, text_position)

        pygame.display.update()

        key = cv2.waitKey(1) & 0xFF

        if key == ord('q'):
            # print colour_upper, colour_lower
            break

track()

