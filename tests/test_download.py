import main

def test_download_data() -> None:
    data = main.download_data(2)
    assert data is not None, "Test case failed for page number"
    data = main.download_data('Resources/Test2.json')
    assert data is not None, "Test case failed for file name"

    print("All test cases passed!")


# test_download_data()


