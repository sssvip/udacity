# coding:utf-8
' a main module --the entrance of the program'
__author__ = 'David West : admin@dxscx.com'

# import movie module and fresh_tomatoes modle(output html and open it)
import media, fresh_tomatoes

# prepare my favorate movies
beautiful_mind = media.Movie("Beautiful Mind", "http://img0.imgtn.bdimg.com/it/u=3594748736,1413010706&fm=21&gp=0.jpg",
                             "https://www.youtube.com/watch?v=pZISJqJbQuU")
tricky_master = media.Movie("The Tricky Master 1999",
                            "http://img0.imgtn.bdimg.com/it/u=944861915,4092040625&fm=21&gp=0.jpg",
                            "https://www.youtube.com/watch?v=fujjR_Z6UCY")
fight_back_to_school = media.Movie("Fight Back To School 1991", "http://img32.ddimg.cn/83/8/8981462-1_w.jpg",
                                   "https://www.youtube.com/watch?v=fGrGLjNRolI")
my_heart_will_go_on = media.Movie("My Heart Will Go On", "http://img7.5sing.kgimg.com/m/T1jyY5BXDT1RXrhCrK.jpg",
                                  "https://www.youtube.com/watch?v=DNyKDI9pn0Q")
the_graduate = media.Movie("The Graduate", "http://img0.imgtn.bdimg.com/it/u=3632633118,930488686&fm=21&gp=0.jpg",
                           "https://www.youtube.com/watch?v=-MCQIOCem2I")

# construct movie arrays
movies = [beautiful_mind, tricky_master, fight_back_to_school, my_heart_will_go_on, the_graduate]

# output  movies to html and open it use default browser
fresh_tomatoes.open_movies_page(movies)
