from dis import dis
import numpy as np
import cv2
import time
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)
# Pega o valor aonde a mao esta localizada para calcular em cima disso
entradaDaDistanciaDaMao = 1
contador = 0
sair = 0
with mp_hands.Hands(
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5,
        max_num_hands=1,
        static_image_mode=False) as hands:
    while cap.isOpened():
        success, image = cap.read()

        if not success:
            continue
        image = cv2.flip(image, 1)
        image_RGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        image.flags.writeable = False

        results = hands.process(image_RGB)

        if results.multi_hand_landmarks:
            image_height, image_width, _ = image.shape
            annotated_image = image.copy()
            for hand_landmarks in results.multi_hand_landmarks:

                ###################################################################################
                # Ponto 4 do dedao
                dedao_x_4 = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x * image_width
                dedao_y_4 = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y * image_height
                dedao_4 = (int(dedao_x_4), int(dedao_y_4))
                # print(dedao_4)

                ######################################################################################
                # Ponto 3 do dedao
                dedao_x_3 = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].x * image_width
                dedao_y_3 = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].y * image_height
                dedao_3 = (int(dedao_x_3), int(dedao_y_3))
                dedao_3_ = (int(dedao_x_3) + int(dedao_y_3))
                # print(dedao_3)

                ######################################################################################
                # Ponto 2 do dedao
                dedao_x_2 = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].x * image_width
                dedao_y_2 = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].y * image_height
                dedao_2 = (int(dedao_x_2), int(dedao_y_2))
                # print(dedao_2)

                ######################################################################################
                # Ponto 1 do dedao
                dedao_x_1 = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_CMC].x * image_width
                dedao_y_1 = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_CMC].y * image_height
                dedao_1 = (int(dedao_x_1), int(dedao_y_1))
                # print(dedao_1)

                ######################################################################################
                # Ponto 0 mão
                mao_x_0 = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x * image_width
                mao_y_0 = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y * image_height
                mao_0 = (int(mao_x_0), int(mao_y_0))
                # print(mao_0)

                ######################################################################################
                # Ponto 8 indicador
                indicador_x_8 = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * image_width
                indicador_y_8 = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image_height
                indicador_8 = (int(indicador_x_8), int(indicador_y_8))
                # print(indicador_8)

                ######################################################################################
                # Ponto 7 indicador
                indicador_x_7 = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].x * image_width
                indicador_y_7 = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].y * image_height
                indicador_7 = (int(indicador_x_7), int(indicador_y_7))
                indicador_7_ = (int(indicador_x_7) + int(indicador_y_7))
                # print(indicador_7)

                ######################################################################################
                # Ponto 6 indicador
                indicador_x_6 = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].x * image_width
                indicador_y_6 = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].y * image_height
                indicador_6 = (int(indicador_x_6), int(indicador_y_6))
                # print(indicador_6)

                ######################################################################################
                # Ponto 5 indicador
                indicador_x_5 = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].x * image_width
                indicador_y_5 = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].y * image_height
                indicador_5 = (int(indicador_x_5), int(indicador_y_5))
                # print(indicador_5)

                ######################################################################################
                # Ponto 12 Medio
                indicador_x_12 = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x * image_width
                indicador_y_12 = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y * image_height
                indicador_12 = (int(indicador_x_12), int(indicador_y_12))
                # print(indicador_12)

                ######################################################################################
                # Ponto 11 Medio
                indicador_x_11 = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].x * image_width
                indicador_y_11 = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].y * image_height
                indicador_11 = (int(indicador_x_11), int(indicador_y_11))
                # print(indicador_11)

                ######################################################################################
                # Ponto 10 Medio
                indicador_x_10 = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].x * image_width
                indicador_y_10 = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y * image_height
                indicador_10 = (int(indicador_x_10), int(indicador_y_10))
                # print(indicador_10)

                ######################################################################################
                # Ponto 9 Medio
                indicador_x_9 = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].x * image_width
                indicador_y_9 = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y * image_height
                indicador_9 = (int(indicador_x_9), int(indicador_y_9))
                # print(indicador_9)

                ######################################################################################
                # Ponto 16 anelar
                indicador_x_16 = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].x * image_width
                indicador_y_16 = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y * image_height
                indicador_z_16 = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].z
                # print(indicador_z_16)
                indicador_16 = (int(indicador_x_16), int(indicador_y_16))
                # print(indicador_16)

                ######################################################################################
                # Ponto 15 anelar
                indicador_x_15 = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP].x * image_width
                indicador_y_15 = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP].y * image_height
                indicador_15 = (int(indicador_x_15), int(indicador_y_15))
                # print(indicador_15)

                ######################################################################################
                # Ponto 14 anelar
                indicador_x_14 = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].x * image_width
                indicador_y_14 = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].y * image_height
                indicador_14 = (int(indicador_x_14), int(indicador_y_14))
                # print(indicador_14)

                ######################################################################################
                # Ponto 13 anelar
                indicador_x_13 = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP].x * image_width
                indicador_y_13 = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP].y * image_height
                indicador_13 = (int(indicador_x_13), int(indicador_y_13))
                # print(indicador_13)

                ######################################################################################
                # Ponto 20 Mindinho
                indicador_x_20 = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].x * image_width
                indicador_y_20 = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y * image_height
                indicador_20 = (int(indicador_x_20), int(indicador_y_20))
                # print(indicador_20)

                ######################################################################################
                # Ponto 19 Mindinho
                indicador_x_19 = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP].x * image_width
                indicador_y_19 = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP].y * image_height
                indicador_19 = (int(indicador_x_19), int(indicador_y_19))
                # print(indicador_19)

                ######################################################################################
                # Ponto 18 Mindinho
                indicador_x_18 = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].x * image_width
                indicador_y_18 = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].y * image_height
                indicador_18 = (int(indicador_x_18), int(indicador_y_18))
                # print(indicador_18)

                ######################################################################################
                # Ponto 17 Mindinho
                indicador_x_17 = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].x * image_width
                indicador_y_17 = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].y * image_height
                indicador_17 = (int(indicador_x_17), int(indicador_y_17))
                # print(indicador_17)

                distancia_8_4 = int(np.sqrt((indicador_x_8 - dedao_x_4)
                                            ** 2+(indicador_y_8 - dedao_y_4)**2))

                distancia_7_3 = int(np.sqrt((indicador_x_7 - dedao_x_3)
                                            ** 2+(indicador_y_7 - dedao_y_3)**2))

                distancia_6_2 = int(np.sqrt((indicador_x_6 - dedao_x_2)
                                            ** 2+(indicador_y_6 - dedao_y_2)**2))

                distancia_5_1 = int(np.sqrt((indicador_x_5 - dedao_x_1)
                                            ** 2+(indicador_y_5 - dedao_y_1)**2))

                distancia_12_0 = int(np.sqrt((indicador_x_12 - mao_x_0)
                                             ** 2+(indicador_y_12 - mao_y_0)**2))

                distancia_16_0 = int(np.sqrt((indicador_x_16 - mao_x_0)
                                             ** 2+(indicador_y_16 - mao_y_0)**2))

                distancia_20_0 = int(np.sqrt((indicador_x_20 - mao_x_0)
                                             ** 2+(indicador_y_20 - mao_y_0)**2))

                if entradaDaDistanciaDaMao == 1:
                    # time.sleep(4)
                    marco_8_4 = distancia_8_4
                    # marco_7_3 = distancia_7_3
                    # marco_6_2 = distancia_6_2
                    # marco_5_1 = distancia_5_1
                    marco_12_0 = distancia_12_0
                    marco_16_0 = distancia_16_0
                    marco_20_0 = distancia_20_0
                    entradaDaDistanciaDaMao = 2
                COLOR = (0, 255, 0)
                COLOR2 = (0, 0, 0)
                COLOR3 = (0, 0, 0)
                COLOR4 = (0, 0, 0)
                COLOR5 = (0, 0, 0)
                COLOR6 = (0, 0, 0)
                # print("Distancia 12-0 : ", distancia_12_0)
                # print("Distancia 16-0 : ", distancia_16_0)
                # print("Distancia 20-0 : ", distancia_20_0)
                # print("Distancia 8-4 : ", distancia_8_4)
                # print("80% 8-4 : ", marco_8_4*0.80)
                # print("20% 8-4 : ", marco_8_4*0.20)

                # print("Distancia 7-3 : ", distancia_7_3)
                # print("80% 7-3 : ", marco_7_3*0.80)
                # print("20% 7-3 : ", marco_7_3*0.20)

                # print("Distancia 6-2 : ", distancia_6_2)
                # print("80% 6-2 : ", marco_6_2*0.80)
                # print("20% 6-2 : ", marco_6_2*0.20)

                # print("Distancia 5-1 : ", distancia_5_1)
                # print("80% 5-1 : ", marco_5_1*0.80)
                # print("20% 5-1 : ", marco_5_1*0.20)
                # angulo_minutos = (indicador_7_)
                # angulo_horas = (dedao_3_) + (indicador_7_/2)
                # print(angulo_horas - angulo_minutos)
                # print((dedao_y_4 - indicador_y_8))
                # angulo_minutos = (-5 * (dedao_x_4 - indicador_x_5))
                # angulo_horas = (0 * (dedao_y_4 - indicador_y_8) +
                #                 ((dedao_x_4 - indicador_x_5) / 2))
                # print(angulo_horas + angulo_minutos)
                f = (dedao_x_3 - indicador_x_6)
                g = (indicador_y_6 - dedao_y_4)
      
                if f < 20 and g > 0:
                    COLOR2 = (0, 255, 0)
                    contador = 1 + contador
                    # print("opa")
                    # print("t")
                if indicador_y_13 < indicador_y_16:
                    COLOR3 = (0, 255, 0)
                    contador = 1 + contador
                    # print("opa")
                    # print("t")
                if indicador_y_9 < indicador_y_12:
                    COLOR4 = (0, 255, 0)
                    contador = 1 + contador
                    # print("opa")
                    # print("t")
                if indicador_y_17 < indicador_y_20:
                    COLOR5 = (0, 255, 0)
                    contador = 1 + contador

                if indicador_y_5 < indicador_y_8:
                    COLOR6 = (0, 255, 0)
                    contador = 1 + contador

                if contador >= 5:
                    print("Letra A")
                    print("vc Acertou")
                    sair = 1
                    # cv2.destroyAllWindows()
                    break
                
                contador = 0
                # print("opa")
                # print("t")
                # if (distancia_12_0) > (marco_12_0 * 0.25) or (distancia_12_0) > (marco_12_0 * 0.45):
                #     COLOR4 = (0, 255, 0)
                # if distancia > (marco*0.80):
                #     COLOR = (255, 0, 0)
                #     print("ola")

                # else:
                #     if distancia < (marco*0.20):

                #         print("opa")
                #         COLOR = (0, 0, 255)
                #     else:
                #         print("e isso")
                #####################################################################
                # cv2.line(image, (dedao_4), (indicador_8),
                #          COLOR, 2, cv2.LINE_AA)
                # cv2.circle(image, indicador_8, 4,
                #            (255, 0, 255), 2, cv2.LINE_AA)
                # cv2.circle(image, dedao_4, 4, (255, 0, 0), 2, cv2.LINE_AA)
                #########################################################################
                cv2.line(image, (dedao_3), (indicador_6),
                         COLOR2, 2, cv2.LINE_AA)
                cv2.circle(image, indicador_6, 4,
                           (0, 0, 0), 2, cv2.LINE_AA)
                cv2.circle(image, dedao_3, 4, (0, 0, 0), 2, cv2.LINE_AA)
                ###################################################################
                cv2.line(image, (mao_0), (indicador_16),
                         COLOR5, 2, cv2.LINE_AA)
                cv2.circle(image, indicador_16, 4,
                           (0, 0, 0), 2, cv2.LINE_AA)
                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                ###################################################################
                cv2.line(image, (mao_0), (indicador_12),
                         COLOR4, 2, cv2.LINE_AA)
                cv2.circle(image, indicador_12, 4,
                           (0, 0, 0), 2, cv2.LINE_AA)
                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                ###################################################################
                cv2.line(image, (mao_0), (indicador_20),
                         COLOR6, 2, cv2.LINE_AA)
                cv2.circle(image, indicador_20, 4,
                           (0, 0, 0), 2, cv2.LINE_AA)
                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                ###################################################################
                cv2.line(image, (mao_0), (indicador_8),
                         COLOR3, 2, cv2.LINE_AA)
                cv2.circle(image, indicador_8, 4,
                           (0, 0, 0), 2, cv2.LINE_AA)
                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                mp_drawing.draw_landmarks(
                    image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                if sair == 1:
                    break
            if sair == 1:
                    break
        # if sair == 1:
        #             break                
        cv2.imshow('visioncompy', image)
        if cv2.waitKey(30) & 0xFF == 27:
            break
      
cap.release()
cv2.destroyAllWindows()
