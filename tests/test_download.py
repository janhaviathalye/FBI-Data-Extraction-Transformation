import main
from unittest.mock import patch
import json
import pytest

@pytest.fixture
def mock_api_response():
    return {
        "items": [
    {
      "files": [
        {
          "url": "https://www.fbi.gov/wanted/kidnap/hansel-quiroz/download.pdf",
          "name": "English"
        },
        {
          "url": "https://www.fbi.gov/wanted/kidnap/hansel-quiroz/quirozh-spanish-final.pdf/@@download/file/quirozh.Spanish.final.pdf",
          "name": "EN ESPAOL"
        }
      ],
      "age_range": None,
      "uid": "7604c7bbfce34754a6998f658aeb442c",
      "weight": None,
      "occupations": None,
      "field_offices": [
        "losangeles"
      ],
      "locations": None,
      "reward_text": None,
      "sex": "Male",
      "hair": None,
      "ncic": None,
      "dates_of_birth_used": [
        "September 6, 2015"
      ],
      "caution": None,
      "nationality": "American",
      "age_min": None,
      "age_max": None,
      "scars_and_marks": None,
      "subjects": [
        "Kidnappings and Missing Persons"
      ],
      "aliases": None,
      "race_raw": "White (Hispanic)",
      "suspects": None,
      "publication": "2024-08-13T10:31:00",
      "title": "HANSEL QUIROZ",
      "coordinates": [
        
      ],
      "hair_raw": None,
      "languages": None,
      "complexion": None,
      "build": None,
      "details": "<p>The Federal Bureau of Investigation's Los Angeles Field Office is seeking the public\u2019s assistance locating Hansel Quiroz.\u00a0On June 16, 2023, at approximately 4:00 p.m. in Ontario, California, Hansel was picked up by his father, <a data-urltype=\"/view\" data-val=\"https://www.fbi.gov/wanted/parental-kidnappings/felipe-de-jesus-quiroz-jimenez\" href=\"https://www.fbi.gov/wanted/parental-kidnappings/felipe-de-jesus-quiroz-jimenez\" data-linktype=\"external\">Felipe De Jesus Quiroz-Jimenez</a>, for a scheduled, unmonitored visit. At the end of the visit, Hansel was not returned to his mother, who shared legal custody of the child with his father at that time. It is alleged that Felipe De Jesus Quiroz-Jimenez drove Hansel to Mexico and has not returned, denying the child's mother her parental rights.\u00a0At the time of pick-up, Felipe De Jesus Quiroz-Jimenez was driving a 2002 silver two door Volkswagen GTI with California Plate 7PHT055.</p>\r\n<p>\u00a0</p>",
      "status": "na",
      "legat_names": None,
      "eyes": None,
      "person_classification": "Main",
      "description": "June 16, 2023\r\nOntario, California",
      "images": [
        {
          "large": "https://www.fbi.gov/wanted/kidnap/hansel-quiroz/@@images/image/large",
          "caption": None,
          "thumb": "https://www.fbi.gov/wanted/kidnap/hansel-quiroz/@@images/image/thumb",
          "original": "https://www.fbi.gov/wanted/kidnap/hansel-quiroz/@@images/image"
        },
        {
          "large": "https://www.fbi.gov/wanted/kidnap/hansel-quiroz/hanselcortezquiroz_2.jpg/@@images/image/large",
          "caption": "",
          "thumb": "https://www.fbi.gov/wanted/kidnap/hansel-quiroz/hanselcortezquiroz_2.jpg/@@images/image/thumb",
          "original": "https://www.fbi.gov/wanted/kidnap/hansel-quiroz/hanselcortezquiroz_2.jpg"
        },
        {
          "large": "https://www.fbi.gov/wanted/kidnap/hansel-quiroz/volkswagon-gti-ca.jpg/@@images/image/large",
          "caption": "",
          "thumb": "https://www.fbi.gov/wanted/kidnap/hansel-quiroz/volkswagon-gti-ca.jpg/@@images/image/thumb",
          "original": "https://www.fbi.gov/wanted/kidnap/hansel-quiroz/volkswagon-gti-ca.jpg"
        }
      ],
      "possible_countries": None,
      "weight_min": None,
      "additional_information": None,
      "remarks": "<p>Hansel Quiroz and his father, Felipe De Jesus Quiroz-Jimenez, are believed to be in Mexico City, Mexico, with the family of Quiroz-Jimenez.\u00a0 They also have ties to or may visit Guadalajara, Jalisco, Mexico, and Guerrero, Mexico.\u00a0</p>",
      "path": "/wanted/kidnap/hansel-quiroz",
      "eyes_raw": None,
      "weight_max": None,
      "reward_min": 0,
      "url": "https://www.fbi.gov/wanted/kidnap/hansel-quiroz",
      "possible_states": None,
      "modified": "2024-09-09T16:58:56+00:00",
      "reward_max": 0,
      "race": "hispanic",
      "height_max": None,
      "place_of_birth": "California",
      "height_min": None,
      "poster_classification": "kidnapping",
      "warning_message": None,
      "@id": "https://api.fbi.gov/@wanted-person/7604c7bbfce34754a6998f658aeb442c"
    }]
    }

def test_download_data(mock_api_response) -> None:
    with patch('requests.get') as mock_get:
        mock_response = mock_get.return_value
        mock_response.content = json.dumps(mock_api_response).encode('utf-8')
        data = main.download_data(2)
        assert data is not None, "Test case failed for page number"
        data = main.download_data('Resources/Test2.json')
        assert data is not None, "Test case failed for file name"

        print("All test cases passed!")


# test_download_data()


