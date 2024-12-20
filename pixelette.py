from video_stream import manipulate_vid
import cv2 as cv
import numpy as np
import os
import argparse


model_path = os.path.join("model", "face_detection_yunet_2023mar.onnx")

detector = cv.FaceDetectorYN.create(model_path, "", (320, 320), 0.65, 0.3, 5000)


def process_pic(img, out):
    img = cv.imread(img, cv.IMREAD_COLOR)
    pixel = fun(img)
    cv.imwrite(f"{out}.jpg", pixel)

def pixelate_faces(img):
    width, height = img.shape[1], img.shape[0]
    detector.setInputSize((width, height))

    faces = detector.detect(img)
    copy_img = img.copy()

    if faces[1] is not None:
        for face in faces[1]:
            (x, y, w, h) = face[0:4].astype(np.int32)
            if x > 0 and y > 0:
                print(x, y, w, h)
                p = pixelate_image(img[y : y + h, x : x + w])
                copy_img[y : y + h, x : x + w] = p

    return copy_img


def pixelate_image(img):
    """
    Downsamples a picture and upsamples the picture
    """
    orginal_width, orginal_height = img.shape[0], img.shape[1]
    down_sample = cv.resize(img, None, fx=0.1, fy=0.1, interpolation=cv.INTER_NEAREST)
    scaled = cv.resize(
        down_sample, (orginal_height, orginal_width), interpolation=cv.INTER_NEAREST
    )
    return scaled


def main():
    parser = argparse.ArgumentParser(description="Process a video or an image.")

    parser.add_argument(
        "-v",
        "--video",
        help="Path to the video file (leave blank if processing an image)",
        type=str,
        nargs="?",
    )
    parser.add_argument(
        "-i",
        "--image",
        help="Path to the image file (leave blank if processing a video)",
        type=str,
        nargs="?",
    )
    parser.add_argument("-o", "--output", help="Output file path", type=str)

    args = parser.parse_args()

    if args.video:
        manipulate_vid(args.video, args.output, pixelate_faces)
    elif args.image:
        process_pic(args.image, args.output, pixelate_faces)
    else:
        print("Please provide either a video or image path for processing.")


if __name__ == "__main__":
    main()
