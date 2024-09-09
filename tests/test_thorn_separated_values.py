import main

item_list = ['JESUS DE LA CRUZ - LYNN, MASSACHUSETTS', 'ViCAP Missing Persons, Murder', '']

def test_thorn_separated_values(capsys) -> None:
    main.print_thorn_separated_data(item_list)
    captured = capsys.readouterr()
    
    assert captured.out == 'JESUS DE LA CRUZ - LYNN, MASSACHUSETTSþViCAP Missing Persons, Murderþ\n', "Test case failed for printing thorn separated values"

    print("All test cases passed!")


# test_thorn_separated_values()