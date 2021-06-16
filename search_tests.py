from search import title_to_info, keyword_to_titles, search, article_info, article_length, title_timestamp, favorite_author, multiple_keywords, display_result
from search_tests_helper import print_basic, print_advanced, print_advanced_option, get_print
from wiki import article_metadata, title_to_info_map, keyword_to_titles_map
from unittest.mock import patch
from copy import deepcopy

# List of all available article titles for this search engine
# The benefit of using this is faster code - these functions will execute
# every time it gets called, but if the return value of it gets stored it into
# a variable, the function will not need to run every time the list of available
# articles is needed.
METADATA = article_metadata()
TITLE_TO_INFO = title_to_info_map()
KEYWORD_TO_TITLES = keyword_to_titles_map()

# Storing into a variable so don't need to copy and paste long list every time
DOG = ['Black dog (ghost)', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', 'Sun dog']

TRAVEL = ['Time travel']

MUSIC = ['List of Canadian musicians', 'French pop music', 'Noise (music)', '1922 in music', '1986 in music', 'Kevin Cadogan', '2009 in music', 'Rock music', 'Lights (musician)', 'Tim Arnold (musician)', 'Old-time music', 'Arabic music', 'Joe Becker (musician)', 'Richard Wright (musician)', 'Voice classification in non-classical music', '1936 in music', '1962 in country music', 'List of dystopian music, TV programs, and games', 'Steve Perry (musician)', 'David Gray (musician)', 'Alex Turner (musician)', 'List of gospel musicians', 'Indian classical music', '1996 in music', 'Traditional Thai musical instruments', '2006 in music', 'Tony Kaye (musician)', 'Texture (music)', '2007 in music', '2008 in music']

PROGRAMMING = ['C Sharp (programming language)', 'Python (programming language)', 'Lua (programming language)', 'Covariance and contravariance (computer science)', 'Personal computer', 'Ruby (programming language)']

SOCCER = ['Spain national beach soccer team', 'Will Johnson (soccer)', 'Steven Cohen (soccer)']

PHOTO = ['Digital photography']

SCHOOL = ['Edogawa, Tokyo', 'Fisk University', 'Annie (musical)', 'Alex Turner (musician)']

PLACE = ['2009 in music', 'List of dystopian music, TV programs, and games', '2006 in music', '2007 in music', '2008 in music']

DANCE = ['List of Canadian musicians', '2009 in music', 'Old-time music', '1936 in music', 'Indian classical music']

def test_example_title_to_info_tests():
    ''' Tests for title_to_info(), function #1. '''
    # Example tests, these do not count as your tests
    assert title_to_info(METADATA) == TITLE_TO_INFO

    # Create fake metadata to test
    fake_metadata = [['an article title', 'andrea', 1234567890, 103, ['some', 'words', 'that', 'make', 'up', 'sentence']],
                     ['another article title', 'helloworld', 987123456, 8029, ['more', 'words', 'could', 'make', 'sentences']]]

    # Expected value of title_to_info with fake_metadata
    expected = {'an article title': {'author': 'andrea', 'timestamp': 1234567890, 'length': 103}, 
                'another article title': {'author': 'helloworld', 'timestamp': 987123456, 'length': 8029}}
    assert title_to_info(deepcopy(fake_metadata)) == expected

def test_example_keyword_to_titles_tests():
    ''' Tests for keyword_to_titles(), function #2. '''
    # Function #2
    # assert keyword_to_titles(METADATA) == KEYWORD_TO_TITLES

    # # Create fake metadata to test
    
    fake_metadata = [['an article title', 'andrea', 1234567890, 103, ['some', 'words', 'that', 'make', 'up', 'sentence']],
                     ['another article title', 'helloworld', 987123456, 8029, ['more', 'words', 'could', 'make', 'sentences']]]
    
    # Expected value of keyword_to_titles with fake_metadata
    expected = {'some': ['an article title'], 'words': ['an article title', 'another article title'], 'that': ['an article title'], 'make': ['an article title', 'another article title'], 'up': ['an article title'], 'sentence': ['an article title'], 'more': ['another article title'], 'could': ['another article title'], 'sentences': ['another article title']}

    assert keyword_to_titles(deepcopy(fake_metadata)) == expected

def test_example_unit_tests():
    # Example tests, these do not count as your tests

    # Basic search, function #3
    assert search('dog') == DOG

    # Advanced search option 1, function #4
    expected = {'Black dog (ghost)': {'author': 'SmackBot', 'timestamp': 1220471117, 'length': 14746}, 'Mexican dog-faced bat': {'author': 'AnomieBOT', 'timestamp': 1255316429, 'length': 1138}, 'Dalmatian (dog)': {'author': 'J. Spencer', 'timestamp': 1207793294, 'length': 26582}, 'Guide dog': {'author': 'Sarranduin', 'timestamp': 1165601603, 'length': 7339}, 'Sun dog': {'author': 'Hellbus', 'timestamp': 1208969289, 'length': 18050}}
    assert article_info(deepcopy(DOG), TITLE_TO_INFO) == expected

    # Advanced search option 2, function #5
    expected = ['Mexican dog-faced bat', 'Guide dog']
    assert article_length(8000, deepcopy(DOG), TITLE_TO_INFO) == expected

    # Advanced search option 3, function #6
    expected = {'Black dog (ghost)': 1220471117, 'Mexican dog-faced bat': 1255316429, 'Dalmatian (dog)': 1207793294, 'Guide dog': 1165601603, 'Sun dog': 1208969289}
    assert title_timestamp(deepcopy(DOG), TITLE_TO_INFO) == expected

    # Advanced search option 4, function #7
    assert favorite_author('J. Spencer', deepcopy(DOG), TITLE_TO_INFO) == True
    assert favorite_author('Andrea', deepcopy(DOG), TITLE_TO_INFO) == False

    # Advanced search option 5, function #8
    expected = ['Black dog (ghost)', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', 'Sun dog', 'Spain national beach soccer team', 'Will Johnson (soccer)', 'Steven Cohen (soccer)']
    assert multiple_keywords('soccer', deepcopy(DOG)) == expected

# For all integration test functions, remember to put in patch so input() gets mocked out
@patch('builtins.input')
def test_example_integration_test(input_mock):
    keyword = 'dog'
    advanced_option = 2
    advanced_response = 8000

    # Output of calling display_results() with given user input
    output = get_print(input_mock, [keyword, advanced_option, advanced_response])

    # Expected print outs from running display_results() with above user input
    expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['Mexican dog-faced bat', 'Guide dog']\n"

    # Test whether calling display_results() with given user input equals expected printout
    assert output == expected

# TODO Write tests below this line. Do not remove.
def test_title_to_info():

    
    metadatax = [['Afro Music', 'Burnaboy', 212323224, 2879, ['ye', 'big', 'man', 'bad', 'good']], ['endSARS', 'Falz', 346870702, 900, ['bad', 'government', 'Nigeria', 'Good']]]
    metadataxx = [['Epic Race', 'Bolt', 347979034, 3500, ['run', 'sweat', 'wake', 'jump', 'race']], ['Marathon', 'Anderson Cooper', 34598347, 2500, ['Run', 'run', 'Walk']], ['Football', 'Ronaldo', 348607070, 7500, ['ball', 'GOAT', 'sweat', 'run']]]
    metadataxxx = [['Good Government', 'Dele', 567884583, 15000, ['peace', 'corruption', 'health']], ['Nigeria Independence', 'Obasanjo', 234676879, 20000, ['1960', 'britian', 'politician', 'nigerian', 'peace']]]
    # 1
    expected = {'Afro Music': {'author': 'Burnaboy', 'timestamp': 212323224, 'length': 2879}, 'endSARS': {'author': 'Falz', 'timestamp': 346870702, 'length': 900}}
    assert title_to_info(deepcopy(metadatax)) == expected
    # 2
    expected = {'Epic Race': {'author': 'Bolt', 'timestamp': 347979034, 'length': 3500}, 'Marathon': {'author': 'Anderson Cooper', 'timestamp': 34598347, 'length': 2500}, 'Football': {'author': 'Ronaldo', 'timestamp': 348607070, 'length': 7500}}
    assert title_to_info(deepcopy(metadataxx)) == expected
   # 3
    expected = {'Good Government': {'author': 'Dele', 'timestamp': 567884583, 'length': 15000}, 'Nigeria Independence': {'author': 'Obasanjo', 'timestamp': 234676879, 'length': 20000}}
    assert title_to_info(deepcopy(metadataxxx)) == expected
   
    
def test_keyword_to_titles():
    metadatax = [['Afro Music', 'Burnaboy', 212323224, 2879, ['ye', 'big', 'man', 'bad', 'good']], ['endSARS', 'Falz', 346870702, 900, ['bad', 'government', 'Nigeria', 'Good']]]
    metadataxx = [['Epic Race', 'Bolt', 347979034, 3500, ['run', 'sweat', 'wake', 'jump', 'race']], ['Marathon', 'Anderson Cooper', 34598347, 2500, ['Run', 'run', 'Walk']], ['Football', 'Ronaldo', 348607070, 7500, ['ball', 'GOAT', 'sweat', 'run']]]
    metadataxxx = [['Good Government', 'Dele', 567884583, 15000, ['peace', 'corruption', 'health']], ['Nigeria Independence', 'Obasanjo', 234676879, 20000, ['1960', 'britian', 'politician', 'nigerian', 'peace']]]
  
    # 1
    expected = {'ye': ['Afro Music'], 'big': ['Afro Music'], 'man': ['Afro Music'], 'bad': ['Afro Music', 'endSARS'], 'good': ['Afro Music'], 'government': ['endSARS'], 'Nigeria': ['endSARS'], 'Good': ['endSARS']}
    assert keyword_to_titles(deepcopy(metadatax)) == expected
    
    expected = {'run': ['Epic Race', 'Marathon', 'Football'], 'sweat': ['Epic Race', 'Football'], 'wake': ['Epic Race'], 'jump': ['Epic Race'], 'race': ['Epic Race'], 'Run': ['Marathon'], 'Walk': ['Marathon'], 'ball': ['Football'], 'GOAT': ['Football']}
    assert keyword_to_titles(deepcopy(metadataxx)) == expected
    # 3
    expected = {'peace': ['Good Government', 'Nigeria Independence'], 'corruption': ['Good Government'], 'health': ['Good Government'], '1960': ['Nigeria Independence'], 'britian': ['Nigeria Independence'], 'politician': ['Nigeria Independence'], 'nigerian': ['Nigeria Independence']}
    assert keyword_to_titles(deepcopy(metadataxxx)) == expected
    
def tests_functions():
    # function 3
    assert search('PLACE') == PLACE
    assert search('Travel') == TRAVEL
    assert search('school') == SCHOOL
    assert search('') == []
    # function 4
    assert article_info(deepcopy(TRAVEL), TITLE_TO_INFO) == {'Time travel': {'author': 'Thug outlaw69', 'timestamp': 1140826049, 'length': 35170}}
    assert article_info(deepcopy(PLACE), TITLE_TO_INFO) == {'2009 in music': {'author': 'SE KinG', 'timestamp': 1235133583, 'length': 69451}, 'List of dystopian music, TV programs, and games': {'author': 'Notinasnaid', 'timestamp': 1165317338, 'length': 13458}, '2006 in music': {'author': 'Suduser85', 'timestamp': 1171547747, 'length': 105280}, '2007 in music': {'author': 'Squilly', 'timestamp': 1169248845, 'length': 45652}, '2008 in music': {'author': 'Ba11innnn', 'timestamp': 1217641857, 'length': 107605}}
    assert article_info(deepcopy(PHOTO), TITLE_TO_INFO) == {'Digital photography': {'author': 'Mintleaf', 'timestamp': 1095727840, 'length': 18093}}
    # function 5
    assert article_length(8000, deepcopy(PROGRAMMING), TITLE_TO_INFO) == ['Lua (programming language)', 'Covariance and contravariance (computer science)']
    assert article_length(7000, deepcopy(TRAVEL), TITLE_TO_INFO) == []
    assert article_length(3000, deepcopy(''), TITLE_TO_INFO) == []
    # function 6
    assert title_timestamp(deepcopy(PHOTO), TITLE_TO_INFO) == {'Digital photography': 1095727840}
    assert title_timestamp(deepcopy(SCHOOL), TITLE_TO_INFO) == {'Edogawa, Tokyo': 1222607041, 'Fisk University': 1263393671, 'Annie (musical)': 1223619626, 'Alex Turner (musician)': 1187010135}
    assert title_timestamp(deepcopy(''), TITLE_TO_INFO) == {}
    # function 7
    assert favorite_author('Sarranduin', deepcopy(DOG), TITLE_TO_INFO) == True
    assert favorite_author('Godson', deepcopy(MUSIC), TITLE_TO_INFO) == False
    assert favorite_author('', deepcopy(MUSIC), TITLE_TO_INFO) == False
    assert favorite_author('Ciphers', deepcopy(SCHOOL), TITLE_TO_INFO) == True
    # function 8
    assert multiple_keywords('Nature', deepcopy(DOG)) == DOG
    assert multiple_keywords('travel', deepcopy(SCHOOL)) == ['Edogawa, Tokyo', 'Fisk University', 'Annie (musical)', 'Alex Turner (musician)', 'Time travel']
    assert multiple_keywords('place', deepcopy(PROGRAMMING)) == ['C Sharp (programming language)', 'Python (programming language)', 'Lua (programming language)', 'Covariance and contravariance (computer science)', 'Personal computer', 'Ruby (programming language)', '2009 in music', 'List of dystopian music, TV programs, and games', '2006 in music', '2007 in music', '2008 in music']

@patch('builtins.input')
def test_integration_1(input_mock):
    keyword = 'travel'
    advanced_option = 1 

    output = get_print(input_mock, [keyword, advanced_option])
    expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + "\n\nHere are your articles: {'Time travel': {'author': 'Thug outlaw69', 'timestamp': 1140826049, 'length': 35170}}\n"
    
    
@patch('builtins.input')
def test_integration_2(input_mock):
    keyword = 'nature'
    advanced_option = 5
    advanced_response = 'Dog'

    output = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['Black dog (ghost)', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', 'Sun dog']}\n"
        
    
    
# Write tests above this line. Do not remove.
# This automatically gets called when this file runs - this is how Python works.
# To make all tests run, call all test functions inside the if statement.
if __name__ == "__main__":
    # TODO Call all your test functions here
    # Follow the correct indentation as these two examples
    # As you're done with each function, uncomment the example test functions
    # and make sure they pass
    test_example_title_to_info_tests()
    test_example_keyword_to_titles_tests()
    test_example_unit_tests()
    test_example_integration_test()
    test_title_to_info()
    test_keyword_to_titles()
    tests_functions()
    test_integration_1()
    test_integration_2()
