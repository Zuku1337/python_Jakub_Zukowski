from ArgHelper import arg_helper
from OpenCVBuilder import OpenCVBuilder
from os import walk


def directory_photos(directory: str) -> []:
    correction = []
    for i in next(walk(directory), (None, None, []))[2]:
        if i.endswith('.jpg') or i.endswith('.png'):
            correction.append("{}".format(i))
    return ["{}\{}".format(directory, file) for file in correction]


if __name__ == "__main__":
    args = arg_helper()
    image_path = args["image"]
    model_path = args["model"]
    directory_path = args["directory"]
    if image_path is not None:
        person_detector = OpenCVBuilder(model_path, image_path)
        person_detector.process()
    elif directory_path is not None:
        print(directory_photos(directory_path))
        for image_path in directory_photos(directory_path):
            person_detector = OpenCVBuilder(model_path, image_path)
            person_detector.process()
