import cv2 as cv
import ffmpeg
from typing import Callable


def add_audio(inputVideo:str, outVideo:str) -> None:
    """
    Opens the orginal video and video only one
    It then combines them toghter 
    """
    orginal = ffmpeg.input(inputVideo)
    generated = ffmpeg.input(f"{outVideo}.mp4")

    orginal_audio = orginal.audio
    combined = ffmpeg.concat(generated, orginal_audio, v=1, a=1)

    out = combined.output(f"{outVideo}_audio.mp4")
    out.run()




def manipulate_vid(vid:str, out:str, fun:Callable) -> None:
    """
    - Handles the video stream and applies a given frame to a func
    - The new frame are then added togehter to one video
    """

    vid_capture = cv.VideoCapture(vid)

    # Obtain frame size information using get() method
    frame_width = int(vid_capture.get(cv.CAP_PROP_FRAME_WIDTH))
    frame_height = int(vid_capture.get(cv.CAP_PROP_FRAME_HEIGHT)) 
    frame_size = (frame_width,frame_height)
    fps = vid_capture.get(cv.CAP_PROP_FPS)

    # Define the codec and create VideoWriter object
    fourcc = cv.VideoWriter_fourcc(*'mp4v')
    output = cv.VideoWriter(f"{out}.mp4", fourcc, fps, frame_size)

    cap = cv.VideoCapture(vid)

    print("Detecting faces")
    while vid_capture.isOpened():
        ret, frame = vid_capture.read()
    
        # if frame is read correctly ret is True
        if ret:
            result = fun(frame)
            output.write(result)
        else:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        if cv.waitKey(1) == ord('q'):
            break


    cap.release()
    output.release()
    cv.destroyAllWindows()
    print("Adding audio")
    add_audio(vid, out)
