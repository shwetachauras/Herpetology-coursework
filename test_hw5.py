import hw5_herpetology as ssar

class TestSample:
    """
    Autograder - *DO NOT* alter this file
    It tests if your functions are working as expected.
    """
    pgh = {'U.S. Steel Tower': ['tower', '841 (256)', '64', '1970', '5th tallest in Pennsylvania. Has been the tallest building in the city since 1970.'], 'BNY Mellon Center': ['center', '725 (221)', '54', '1983', 'Formerly known as One Mellon Center during its period as corporate headquarters of Mellon Financial.'], 'One PPG Place': ['place', '635 (194)', '40', '1984', 'Corporate headquarters of PPG Industries and co-headquarters of Kraft Heinz.'], 'Fifth Avenue Place': ['place', '616 (188)', '32', '1987', 'Corporate headquarters of Highmark.'], 'One Oxford Centre': ['center', '615 (187)', '45', '1983', 'Corporate headquarters of Oxford Development.'], 'Gulf Tower': ['tower', '582 (177)', '44', '1932', "Name references structure's status as former headquarters of Gulf Oil"], 'Tower at PNC Plaza': ['plaza', '544 (166)', '33', '2015', 'Part of PNC Financial Services corporate headquarters.'], 'Cathedral of Learning': ['cathedral', '535 (163)', '42', '1936', 'Second-tallest university building in the world.'], '525 William Penn Place': ['place', '520 (158)', '41', '1951', 'Originally housed corporate headquarters of both U.S. Steel and Mellon Financial.'], 'K&L Gates Center': ['center', '511 (156)', '39', '1968', 'Originally known as One Oliver Plaza.']}
    def test_reading(self):
        """
        Test File Reading
        """
        assert ssar.csvToDictOfLists("pgh.csv") == self.pgh , "Make sure you're reading the right file and removing the first line"
        
    def test_filterKeys(self):
        """
        Test Filtering by Key
        """
        assert ssar.filterKeys(self.pgh,"Eiffel") == [], "This result should be empty list"
        assert ssar.filterKeys(self.pgh,"Tower") == ['U.S. Steel Tower', 'Gulf Tower', 'Tower at PNC Plaza'], "Don't check for an exact match"
        assert ssar.filterKeys(self.pgh,"tower") == ['U.S. Steel Tower', 'Gulf Tower', 'Tower at PNC Plaza'], "Capitalization should not matter"

    def test_columSet(self):
        """
        Test Colum to Set
        """
        assert isinstance(ssar.columnToSet(self.pgh,0), set) , "Make sure to return a set"
        assert ssar.columnToSet(self.pgh,0) == {'cathedral', 'center', 'plaza', 'tower', 'place'}, "Make sure you're adding to the set"

    def test_filterColumn(self):
        """
        Test Filtering by Column
        """
        assert ssar.filterByColumn(self.pgh,0,'centers') == [], "This result should be empty list"
        assert ssar.filterByColumn(self.pgh,0,'center') == ['BNY Mellon Center', 'One Oxford Centre', 'K&L Gates Center'], "Does not have to be exact match"
        assert ssar.filterByColumn(self.pgh,0,'Center') == ['BNY Mellon Center', 'One Oxford Centre', 'K&L Gates Center'], "Capitalization should not matter"