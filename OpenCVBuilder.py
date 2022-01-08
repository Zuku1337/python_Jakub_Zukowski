from DetectorAPI import DetectorAPI
import cv2 as opencv
import imutils


class OpenCVBuilder:

    def __init__(self, model_path: str, image_path: str) -> None:
        self._model_path = model_path
        self._image_path = image_path

    def __str__(self) -> None:
        return "Ścieżka do modelu:{}\nŚcieżka do zdjęcia:{}".format(self._model_path, self._image_path)

    @property
    def model_path(self) -> str:
        return self._model_path

    @model_path.setter
    def model_path(self, value: str) -> None:
        self._model_path = value

    @property
    def image_path(self) -> str:
        return self._image_path

    @image_path.setter
    def image_path(self, value: str) -> None:
        self._image_path = value

    def process(self) -> None:
        api = DetectorAPI(path_to_ckpt=self._model_path)
        threshold = 0.7
        image = opencv.imread(self._image_path)
        image = imutils.resize(image, width=min(800, image.shape[1]))
        boxes, scores, classes, num = api.process_frame(image)
        person = 1
        for i in range(len(boxes)):
            if classes[i] == 1 and scores[i] > threshold:
                box = boxes[i]
                opencv.rectangle(image, (box[1], box[0]), (box[3], box[2]), (124, 252, 0), 2)
                opencv.putText(image, f'person {person}', (box[1], box[0] - 8), opencv.FONT_HERSHEY_SIMPLEX, 0.5,
                               (0, 0, 255),
                               1)
                person += 1
        opencv.putText(image, f'Total Persons : {person - 1}', (300, 25), opencv.FONT_HERSHEY_DUPLEX, 0.8, (0, 0, 255),
                       2)
        opencv.imshow("Zuku Person Finder 1.0", image)
        opencv.waitKey(0)
        opencv.destroyAllWindows()
