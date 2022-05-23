import cv2
import mediapipe as mp
import numpy as np
import time
mp_drawing = mp.solutions.drawing_utils
mp_selfie_segmentation = mp.solutions.selfie_segmentation


def SelfieSegmentation_video(videopath):
  # For static images:
  IMAGE_FILES = []
  BG_COLOR = (192, 192, 192) # gray
  MASK_COLOR = (255, 255, 255) # white
  with mp_selfie_segmentation.SelfieSegmentation(
      model_selection=0) as selfie_segmentation:

      time_start = time.time()

      # Start capturing the feed
      cap = cv2.VideoCapture(videopath)
      # Find the number of frames
      video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
      print ("Number of frames: ", video_length)
      idx = 0
      print ("Converting video..\n")
      # Start converting the video
      while cap.isOpened():
          # Extract the frame
          ret, image = cap.read()
          image_height, image_width, _ = image.shape
          # Convert the BGR image to RGB before processing.
          if idx%100==0:
            results = selfie_segmentation.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

            # Draw selfie segmentation on the background image.
            # To improve segmentation around boundaries, consider applying a joint
            # bilateral filter to "results.segmentation_mask" with "image".
            condition = np.stack((results.segmentation_mask,) * 3, axis=-1) > 0.1
            # Generate solid color images for showing the output selfie segmentation mask.
            fg_image = np.zeros(image.shape, dtype=np.uint8)
            fg_image[:] = MASK_COLOR
            bg_image = np.zeros(image.shape, dtype=np.uint8)
            bg_image[:] = BG_COLOR
            output_image = np.where(condition, fg_image, bg_image)
            # cv2.imwrite('./selfie_segmentation_output/' + str(idx) + '.png', output_image)

            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            # Draw selfie segmentation on the background image.
            # To improve segmentation around boundaries, consider applying a joint
            # bilateral filter to "results.segmentation_mask" with "image".

            # The background can be customized.
            #   a) Load an image (with the same width and height of the input image) to
            #      be the background, e.g., bg_image = cv2.imread('/path/to/image/file')
            #   b) Blur the input image by applying image filtering, e.g.,
            #      bg_image = cv2.GaussianBlur(image,(55,55),0)
            if bg_image is None:
              bg_image = np.zeros(image.shape, dtype=np.uint8)
              bg_image[:] = BG_COLOR
            output_image = np.where(condition, image, bg_image)
            cv2.imwrite('./selfie_segmentation_new_output' + str(idx) + '.png', output_image)

            # cv2.imshow('MediaPipe Selfie Segmentation', output_image)
                  
          if not ret:
              continue
          # Write the results back to output location.
          # cv2.imwrite(output_loc + "/%#05d.jpg" % (count+1), frame)
          idx = idx + 1
          # If there are no more frames left
          if (idx > (video_length-1)):
              # Log the time again
              time_end = time.time()
              # Release the feed
              cap.release()
              # Print stats
              print ("Done extracting frames.\n%d frames extracted" % idx)
              print ("It took %d seconds forconversion." % (time_end-time_start))
              break

  return ''

SelfieSegmentation_video(r'D:\Download\audio-visual\UCBBj-A2EqL5pNApsLhoeM6w\Youtube\ur\Can This Masterchef Finalist Make THAI GREEN CURRY (Nick DiGiovanni).mp4')
# import cv2
# import mediapipe as mp
# mp_drawing = mp.solutions.drawing_utils
# mp_drawing_styles = mp.solutions.drawing_styles
# mp_face_mesh = mp.solutions.face_mesh

# # For static images:
# IMAGE_FILES = []
# drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
# with mp_face_mesh.FaceMesh(
#     static_image_mode=True,
#     max_num_faces=1,
#     refine_landmarks=True,
#     min_detection_confidence=0.5) as face_mesh:
#   for idx, file in enumerate(IMAGE_FILES):
#     image = cv2.imread(file)
#     # Convert the BGR image to RGB before processing.
#     results = face_mesh.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

#     # Print and draw face mesh landmarks on the image.
#     if not results.multi_face_landmarks:
#       continue
#     annotated_image = image.copy()
#     for face_landmarks in results.multi_face_landmarks:
#       print('face_landmarks:', face_landmarks)
#       mp_drawing.draw_landmarks(
#           image=annotated_image,
#           landmark_list=face_landmarks,
#           connections=mp_face_mesh.FACEMESH_TESSELATION,
#           landmark_drawing_spec=None,
#           connection_drawing_spec=mp_drawing_styles
#           .get_default_face_mesh_tesselation_style())
#       mp_drawing.draw_landmarks(
#           image=annotated_image,
#           landmark_list=face_landmarks,
#           connections=mp_face_mesh.FACEMESH_CONTOURS,
#           landmark_drawing_spec=None,
#           connection_drawing_spec=mp_drawing_styles
#           .get_default_face_mesh_contours_style())
#       mp_drawing.draw_landmarks(
#           image=annotated_image,
#           landmark_list=face_landmarks,
#           connections=mp_face_mesh.FACEMESH_IRISES,
#           landmark_drawing_spec=None,
#           connection_drawing_spec=mp_drawing_styles
#           .get_default_face_mesh_iris_connections_style())
#     cv2.imwrite('/tmp/annotated_image' + str(idx) + '.png', annotated_image)
