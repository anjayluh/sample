__author__ = 'ella'

class Borrower(object):
    def __init__(self, idNo, name, points = 0, movies_borrowed = [], movies_returned = []):
        self.idNo = idNo
        self.name = name
        self.points = points
        self.movies_borrowed = movies_borrowed
        self.movies_returned = movies_returned

class Movie(object):
    def __init__(self, movie_id, title, category, price):
        self.movie_id = movie_id
        self.title = title
        self.category = category
        self.price = price

class Rent(object):
    def __init__(self, days_agreed, days_taken, ):
        self.days_agreed = days_agreed
        self.days_taken = days_taken


if __name__ == '__main__':
     while True:

         borrowers = []
         allmovies = []

         choice = int(raw_input('Choose a number corresponding to what you intend to do \n1. Add a movie.\n2. Borrow a movie,\n3.Returning a movie \n4.Exit'))

         if choice == 1:
             print 'Adding a movie'
             admin = raw_input('Prove your an administraor, What\'s your admin username ')
             if admin == 'admin':

                 movie_id = raw_input('Enter movie ID')
                 title = raw_input('Enter movie title')
                 category = int(raw_input('Choose movie category number\n1. New release\n2. Regular\n3. Children\'s'))
                 if category == 1:
                     price = 1000
                 elif category == 2:
                     price = 500
                 elif category == 3:
                     price = 300
                 else:
                     print 'You have entered an invalid category'
                 movie = Movie(movie_id, title, category, price)
                 allmovies.append(movie)
                 for movie in allmovies:
                     print "You have successfully added \t"
                     print [(movie.title, movie.category) for movie in allmovies]

             else:
                 print 'You must be an administrator'
         elif choice == 2:

             print 'You are borrowing a movie'

             idNo = int(raw_input('Enter your borrower ID number'))
             name = raw_input('What is the borrower\'s name?')
             borrower = Borrower(idNo, name)
             borrowers.append(borrower)
             print 'Customer succesfully added \n'
             print [(borrower.name, borrower.idNo) for borrower in borrowers]
             print 'Now lets get the movie'
             idNo = raw_input('Enter your ID number')
             customer=[(customer.idNo) for customer in borrowers]

             for x in customer:

                 if customer == idNo:
                     movie_to_borrow = raw_input('Enter movie title')
                     for movie in allmovies:
                         if movie.title == movie_to_borrow:
                             allmovies.remove(movie)
                             Borrower.movies_borrowed.append(movie)
                             print 'You hve borrowed %s'%title
                 else:
                     print 'Please register with us first'

         elif choice == 3:
                 print 'You are returning a movie'


         elif choice == 4:
             print 'You are exiting'
