# What to cook
This package provides recipe from 'Rwandan' cuisine.

It provides:

1. A pdf file that has the pdf includes the name, a picture, ingredients and method of a recipe
2. Random recipe
3. Random recipe based on the course
4. Random recipe based on the availability of the vegetables on current month
5. Random recipe based on current month and course


### Functions:
    def simple():

    def course_specific():

    def seasonal():

    def combined():


### example 1
    from whattocook import simple

    simple()


### example 2
    from whattocook import course_specific
    
    course_specific('breakfast')


### example 3
    from whattocook import seasonal
    
    seasonal()


### example 4
    from whattocook import combined
    
    combined('lunch')