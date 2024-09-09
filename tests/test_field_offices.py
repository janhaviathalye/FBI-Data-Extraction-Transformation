import main

item = {
      "age_min": 6,
      "files": [
        {
          "url": "https://www.fbi.gov/wanted/vicap/missing-persons/jesus-de-la-cruz---lynn-massachusetts/delacruz.pdf",
          "name": "English"
        }
      ],
      "possible_states": None,
      "eyes_raw": "Brown",
      "title": "JESUS DE LA CRUZ - LYNN, MASSACHUSETTS",
      "images": [
        {
          "caption": "Photograph taken at Time of Disappearance",
          "large": "https://www.fbi.gov/wanted/vicap/missing-persons/jesus-de-la-cruz---lynn-massachusetts/@@images/image/large",
          "thumb": "https://www.fbi.gov/wanted/vicap/missing-persons/jesus-de-la-cruz---lynn-massachusetts/@@images/image/thumb",
          "original": "https://www.fbi.gov/wanted/vicap/missing-persons/jesus-de-la-cruz---lynn-massachusetts/@@images/image"
        },
        {
          "caption": "Photograph Age Progressed to 31 Years Old",
          "large": "https://www.fbi.gov/wanted/vicap/missing-persons/jesus-de-la-cruz---lynn-massachusetts/delacruzage.jpg/@@images/image/large",
          "thumb": "https://www.fbi.gov/wanted/vicap/missing-persons/jesus-de-la-cruz---lynn-massachusetts/delacruzage.jpg/@@images/image/thumb",
          "original": "https://www.fbi.gov/wanted/vicap/missing-persons/jesus-de-la-cruz---lynn-massachusetts/delacruzage.jpg"
        }
      ],
      "locations": None,
      "status": "na",
      "uid": "b166d627e11149aa82c02d1533e3b650",
      "path": "/wanted/vicap/missing-persons/jesus-de-la-cruz---lynn-massachusetts",
      "remarks": "<p>De la Cruz has a scar above his left eye, birthmarks on his left calf and the left side of his forehead, and has his left ear pierced.</p>",
      "aliases": None,
      "ncic": None,
      "details": "<p>Jesus de la Cruz was last seen on September 28, 1996, walking on Park Street near his residence in Lynn, Massachusetts. He was six years old at the time of his disappearance and has not been seen since. De la Cruz has a scar above his left eye, birthmarks on his left calf and the left side of his forehead, and his left ear is pierced. He was last seen wearing a white t-shirt, blue jeans, and brown and yellow boots.</p>\r\n<p>\u00a0</p>",
      "subjects": [
        "ViCAP Missing Persons",
        "Murder"
      ],
      "eyes": "brown",
      "publication": "2021-09-28T10:00:00",
      "complexion": None,
      "possible_countries": None,
      "race_raw": "White (Hispanic)",
      "person_classification": "Main",
      "dates_of_birth_used": None,
      "url": "https://www.fbi.gov/wanted/vicap/missing-persons/jesus-de-la-cruz---lynn-massachusetts",
      "warning_message": None,
      "reward_text": None,
      "age_max": 6,
      "field_offices": [
        "newyork",
        "florida"
      ],
      "height_min": 54,
      "weight_min": 60,
      "additional_information": None,
      "weight_max": 60,
      "build": None,
      "height_max": 54,
      "occupations": None,
      "nationality": None,
      "reward_max": 0,
      "poster_classification": "default",
      "scars_and_marks": None,
      "sex": "Male",
      "coordinates": [
        
      ],
      "hair_raw": "Brown",
      "hair": "brown",
      "race": "hispanic",
      "suspects": None,
      "caution": None,
      "reward_min": 0,
      "modified": "2024-09-08T00:05:41+00:00",
      "languages": None,
      "legat_names": None,
      "age_range": "6 years old (at time of disappearance)",
      "description": "September 28, 1996\r\nLynn, Massachusetts",
      "place_of_birth": None,
      "weight": "60 pounds (at time of disappearance)",
      "@id": "https://api.fbi.gov/@wanted-person/b166d627e11149aa82c02d1533e3b650"
    }

def test_field_offices_field() -> None:
    item_list = main.format_data(item)
    field_offices_result = item_list[2]
    assert field_offices_result == 'newyork, florida', "Test case failed for extracting field offices"

    print("All test cases passed!")


# test_field_offices_field()