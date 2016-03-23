'''
This is a program that generates HTML with content from a list.
'''

# function for making html markup
def generate_concept_HTML(concept_title, concept_description):

    # html
    html_text = '''
    <div class="concept">
        <div class="concept-title">
            ''' + concept_title + '''
        </div>
        <div class="concept-description">
            ''' + concept_description + '''
        </div>
    </div>
    '''

    return html_text

# function for adding the content
def make_HTML(concept):
    concept_title = concept[0]
    concept_description = concept[1]
    return generate_concept_HTML(concept_title, concept_description)

# function for making html for each concept
def make_HTML_for_many_concepts(list_of_concepts):
    n = 0
    for i in list_of_concepts:
        print generate_concept_HTML(list_of_concepts[n][0], list_of_concepts[n][1])
        n = n + 1

# list of concepts
myConcepts = [ ['Python'    , 'Python is a Programming Language.'],
               ['For Loop'  , 'For Loops allow you to iterate over lists.'],
               ['Lists'     , 'Lists are sequences of data.'] ]

print make_HTML_for_many_concepts(myConcepts)