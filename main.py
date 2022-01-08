from ArgHelper import arg_helper
from OpenCVBuilder import OpenCVBuilder

if __name__ == "__main__":
    args = arg_helper()
    image_path = args["image"]
    model_path = args["model"]
    if image_path is not None:
        person_detector = OpenCVBuilder(model_path, image_path)
        person_detector.process()
