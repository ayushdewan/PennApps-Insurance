import io
import os

def localize_objects(path):
    """Localize objects in the local image.

    Args:
    path: The path to the local file.
    """
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    with open(path, 'rb') as image_file:
        content = image_file.read()
    image = vision.types.Image(content=content)

    objects = client.object_localization(
        image=image).localized_object_annotations


    import cv2
    import numpy as np
    from bounding_box import bounding_box as bb
    image = cv2.imread(path, cv2.IMREAD_COLOR)
    
    print('Number of objects found: {}'.format(len(objects)))
    for object_ in objects:
        print('\n{} (confidence: {})'.format(object_.name, object_.score))
        print('Normalized bounding polygon vertices: ')
        left = 1
        right = 0
        top = 1
        bottom = 0
        for vertex in object_.bounding_poly.normalized_vertices:
            print(' - ({}, {})'.format(vertex.x, vertex.y))
            left = min(left, vertex.x)
            right = max(right, vertex.x)
            top = min(top, vertex.y)
            bottom = max(bottom, vertex.y)
        start = (int(left * image.shape[1]), int(top * image.shape[0]))
        end = (int(right * image.shape[1]), int(bottom * image.shape[0]))
        cv2.rectangle(image, start, end, (255, 0, 0), 10)
    cv2.imwrite("annotated.jpg", image)

localize_objects("resources/desk3.jpg")