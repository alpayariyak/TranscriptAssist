from transcriptassist.transcriptassist import TranscriptAssist


if __name__ == "__main__":

    ta = TranscriptAssist()

    # Transcribing an image from a path with no cropping
    # print(ta.transcribe(IMAGE_PATH))

    # Transcribing an image from a link with coordinates to crop
    link = "https://da2aiq810uha5.cloudfront.net/files/7cada965-71ba-47ad-9b04-f14f2f2d0d87_URVHBIR.jpg"
    all_points =  {"first": {"x": 548.4212962962963, "y": 250.41550925925927},
      "third": {"x": 884.9525462962963, "y": 301.4050925925926},
      "fourth": {"x": 548.4212962962963, "y": 301.4050925925926},
      "second": {"x": 884.9525462962963, "y": 250.41550925925927}
    }
    # Convert crop coordinates to format (x1, y1, x2, y2)
    coordinates = (all_points["first"]["x"], all_points["first"]["y"], all_points["third"]["x"], all_points["third"]["y"])

    print(ta.transcribe(link, coordinates, show_image=True))


