# regex module
import re


# Dev: Zach Baird
# Purpose:
#  This file's code is derived from Automate the Boring Stuff from the fantastic author Al Sweigart. 
#  The resource online can be found here: https://automatetheboringstuff.com :but I strongly encourage you to buy 
#  his book or Udemy course to support him. This file is Python code manipulating and testing regex.
#
# How to Use:
#  Each little example is encapsulated in its own function. To see an example in action, simply call the function
#  at the bottom of the page. Feel free to play with its code to change the results and see what regex can truly
#  do.
#

def isPhoneNumberSimple():
    # Assigns the regex object - NOTE: we include the r to tell the compiler that this is a raw string.
    # We want input like 123-456-7890
    phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

    # Will return None if the regex pattern is not found, and match if it is.
    mo = phoneNumRegex.search('My number is 607-437-9890.')

    # Group returns the actual matched text that we returned from .search().
    if(mo is not None):
        print('Phone number found: ' + mo.group())
    else:
        print('Phone number not found.')


def isPhoneNumberGrouping():
    # Assigns the regex object - NOTE: we use the ()'s to assign separate groups.
    # We want input like 123-456-7890
    phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

    # Search for the match.
    mo = phoneNumRegex.search('610-234-6973')

    # Output results to view.
    if(mo is not None):
        print(mo.group(1))
        print(mo.group(2))
        print('\n')
        print(mo.groups())
        # Multiple assignment trick wince mo.groups() returns a tuple.
        areaCode, mainNumber = mo.groups()
        print(areaCode)
        print(mainNumber)
    else:
        print("No match found.")


def isPhoneNumberParenEscape():
    # Assigns the regex object - NOTE: The parens are escaped so we can look for them in our regex.
    # We want input like (123) 456-2345
    phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')

    # Search for the match.
    mo = phoneNumRegex.search('My phone number is (415) 555-4242.')

    if(mo is not None):
        print(mo.group(1) + '\n' + mo.group(2))
    else:
        print('No match found.')


def simpleHeroRegex():
    # Assign the regex expression. We're looking for either Batman or Tina Fey.
    heroRegex = re.compile(r'Batman|Tina Fey')

    # What we're doing is saying that if EITHER Batman and Tina Fey show up return true, but if BOTH are found, return the first occurance of matched text. See output for clarity.
    mo1 = heroRegex.search('Batman and Tina Fey.')
    mo2 = heroRegex.search('Tina Fey and Batman.')
    mo3 = heroRegex.search('I\'m Batman!!')

    print('Mo1:  ' + mo1.group())
    print('Mo2:  ' + mo2.group())
    print('Mo3:  ' + mo3.group())


def searchBatGear():
    # Assign the regex expression. We're looking for any words included in the expression that start with 'Bat'
    batRegex = re.compile(r'Bat(man|mobile|copter|bat)')

    mo = batRegex.search('Batmobile lost a wheel.')

    print(mo.group())
    # Note that this pulls the second part of the word because it is the first group in the regex expression.
    print(mo.group(1))


def searchBatOptional():
    # Assign the regex expression. The (wo)? indicates a group which is optional.
    batRegex = re.compile(r'Bat(wo)?man')
    mo1 = batRegex.search('The Adventures of Batman')
    print(mo1.group())

    mo2 = batRegex.search('The Adventures of Batwoman')
    print(mo2.group())


def searchPhoneOptional():
    # Assign the regex expression. We are searching for a phone number which may or may not include an area code.
    phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')

    mo1 = phoneRegex.search('My phone number is 514-555-4242')
    print(mo1.group())

    mo2 = phoneRegex.search('My phone number is 534-2435')
    print(mo2.group())


def matchOneOrMore():
    # Assign the regex expression. We are looking for anything like Batwoman or Batwowowowowo...man. Batman does not fit.
    # NOTE: if we ever need to use an actual + sign in our regex string, we just need to escape it (/+)
    batRegex = re.compile(r'Bat(wo)+man')

    mo1 = batRegex.search('The Adventures of Batwoman')
    mo2 = batRegex.search('The Adventures of Batwowowowoman')
    mo3 = batRegex.search('The Adventures of Batman')

    print(mo1.group())
    print(mo2.group())
    if(mo3 == None):
        print('None')


def searchSpecificRepititions():
    # Assign the regex expression. We are looking for patterns that occur a specific number of times.
    haRegex = re.compile(r'(Ha){3}')
    haAdvancedRegex = re.compile(r'(Ha){3,5}')

    mo1 = haRegex.search('HaHaHa')
    mo2 = haRegex.search('hahahahaha')
    mo3 = haAdvancedRegex.search('HaHaHaHaHa')

    print(mo1.group())
    if(mo2 == None):
        print('None')

    if(mo3 is not None):
        print(mo3.group())


def greedyAndNonGreedyMatching():
    # Look up at func 'searchSpecificRepititions. Notice that haAdvancedRegex returns the highest match possible rather than 3 or 4 reps.
    #  This is because Python's regexs are 'greedy' by default, meaning that in ambiguous situations, they will match the longest string
    #  possible.  The non-greedy version of the curly brackets, which matches the shortest string possible, has the closing curly bracket
    #  followed by a question mark.
    haGreedyRegex = re.compile(r'(Ha){3,5}')
    haNonGreedyRegex = re.compile(r'(Ha){3,5}?')

    mo1 = haGreedyRegex.search('HaHaHaHaHa')
    mo2 = haNonGreedyRegex.search('HaHaHaHaHa')

    print(mo1.group())
    print(mo2.group())


def simpleFindAll():
    # Assign the regex. Here we will use findall() rather than search(). Search() returns a Match object of the first matched text, findall returns every match.
    phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    groupedPhoneNumRegex = re.compile(
        r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')  # has groups

    mo1 = phoneNumRegex.search('Cell: 415-555-2345  Work: 212-555-0000')
    # findall returns a list.  .group() does not work on lists.
    mo2 = phoneNumRegex.findall('Cell: 415-555-2345  Work: 212-555-0000')
    # Since we have groups in this regex, it returns a tuple.
    mo3 = groupedPhoneNumRegex.findall(
        'Cell: 415-555-2345  Work: 212-555-0000')

    print(mo1.group())
    print(mo2)
    print(mo3)


def xmasShorthands():
    # Assign the regex. Here we use shorthand characters to look for more complicated patterns.
    xmasRegex = re.compile(r'\d+\s\w+')

    mo = xmasRegex.findall(
        '12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')

    print(mo)


def customCharClasses():
    # Assign the regex. Here we create our own shorthand regex to look for vowels
    # NOTE [a-zA-Z0-9] would look for all lowercase and uppercase letters, and all digits 0-9
    vowelRegex = re.compile(r'[aeiouAEIOU]')
    # Same shpeel looking for anything not vowels, see ^
    consonantRegex = re.compile(r'[^aeiouAEIOU]')

    mo1 = vowelRegex.findall('Robocop eats baby food. BABY FOOD.')
    mo2 = consonantRegex.findall('Robocop eats baby food. BABY FOOD.')

    print(mo1)
    print(mo2)


def caretAndDollarSign():
    # Assign the regex.  ^ at the beginning means the expression must come first. A $ at the end means the expression must come last.
    beginsWithHello = re.compile(r'^Hello')
    endsWithNumber = re.compile(r'\d$')
    # This basically says the string can contain any amount of numbers, but that it MUST be numbers.
    wholeStringIsNum = re.compile(r'^\d+$')

    mo1 = beginsWithHello.search('Hello world!')
    mo2 = beginsWithHello.search('He said hello.')

    print(mo1.group())
    if mo2 is None:
        print('None')

    mo3 = endsWithNumber.search('Your number is 42')
    print(mo3.group())

    mo4 = endsWithNumber.search('Your number is forty two.')
    if mo4 is None:
        print('None')

    mo5 = wholeStringIsNum.search('1234567890')
    print(mo5.group())

    mo6 = wholeStringIsNum.search('12345xyz67890')
    mo7 = wholeStringIsNum.search('12 34567890')

    if mo6 is not None:
        print(mo6.group())
    if mo7 is not None:
        print(mo7.group())


def searchWildcard():
    # Assign the regex. The . is the wildcard character, NOT *. Here we are looking for any patterns ending in -at.
    atRegex = re.compile(r'.at')

    mo = atRegex.findall('The cat in the hat sat on the flat mat')

    print(mo)


def dotStar():
    # Assign the regex. .* basically means 'anything' Star means 'any or more of the preceding character. We will test . by itself to see if it suffices for 'all' as well.
    nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
    testRegex = re.compile(r'(.)')

    nonGreedyRegex = re.compile(r'<.*?>')
    greedyRegex = re.compile(r'<.*>')

    # NOTE: This is a greedy regex so it will match as much as it can
    mo1 = nameRegex.search('First Name: Al Last Name: Sweigart')
    print(mo1.group(1))
    print(mo1.group(2))

    mo2 = testRegex.search('asdfoiasnfoiasnfa2..2353465oiaosifn#@#')
    mo3 = nonGreedyRegex.search('<To serve man> for dinner.>')
    mo4 = greedyRegex.search('<To serve man> for dinner.>')

    # So, the . by itself only pulls one character lol.
    if(mo2 is not None):
        print(mo2.group())
    else:
        print('Dudn\'t work')

    print(mo3.group())
    print(mo4.group())


def newLineRegex():
    # Does not detect endlines.
    noNewlineRegex = re.compile('.*')
    print(noNewlineRegex.search(
        'Serve the public.\nProtect the innocent.\nUphold the law.').group())

    # Detects endlines
    newlineRegex = re.compile('.*', re.DOTALL)
    print(newlineRegex.search(
        'Serve the public.\nProtect the innocent.\nUphold the law.').group())


def caseInsensitiveRoboCop():
    # Second argument specifies that we dont' care about case
    robocop = re.compile(r'robocop', re.I)

    print(robocop.search('Robocop is part man, part machine, all cop.').group())
    print(robocop.search('ROBOCOP protects the innocent.').group())
    print(robocop.search(
        'Al, why does your programming book talk about robocop so much?.').group())


def subStringsMethod():
    # We create our regex expression, and wherever there's a match we replace with CENSORED.
    namesRegex = re.compile(r'Agent \w+')
    print(namesRegex.sub(
        'CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))

    # We specify a regex that groups the first letter only, and then infinite letters after
    agentNamesRegex = re.compile(r'Agent (\w)\w*')

    # The \1 is the first group, which we keep. Think bash.
    print(agentNamesRegex.sub(r'\1****',
                              'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))


def firstComplexRegex():
    
