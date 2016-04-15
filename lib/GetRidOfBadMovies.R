################################
#We summarized "bad" movie list.
################################
#The criteria for defining "bad" movies are based on the pattern of the customenr ratings on Amazon website. 
#The so called "pattern" is the distribution of all 5 levels of rating of a particular movie. 
#We set 3 types of movies that should be deleted from the recommendation system: pattern of shape "C", "b" and "L". 
#For example, the shape "b" means that most of people give 3 and 1 for a particular movie; 
#the shape "L" means that most of the people give 1 for a particular movie. 
#This criteria is resonable because it get rid of some movie that may have not too low average rating but in fact it doesn't deserve to be called a "good" movie. 
#################################
#One more interesting pattern that we found is the shape of "F". 
#There are some movie whose ratings follow the shape of "F", which means that most people give 5 and 4, 
#however, they receive pretty low rating of freshness on rottentomates. 
#We decide to keep these kind of movies since many blockbusters nowadays do receive low rating on rottentomates but also interest many movie seekers at the same time.

setwd("F:/CU Textbooks And Related Stuff/STAT W4249/Project4")
library(rvest)
library(tidyr)
library(devtools)
library(omdbapi)
library(pbapply)
library(dplyr)
library(data.table)

movie<-fread("moviescsv.csv")
attach(movie)
reviewscore5=ifelse(review_score==5, 1,0)
reviewscore4=ifelse(review_score==4, 1,0)
reviewscore3=ifelse(review_score==3, 1,0)
reviewscore2=ifelse(review_score==5, 2,0)
reviewscore1=ifelse(review_score==1, 1,0)
movie<-cbind(movie,reviewscore1,reviewscore2,reviewscore3,reviewscore4,reviewscore5)

movie_pytransaction=movie%>%
    group_by(product_productid)%>%
    summarize(
        reviewCt=n(),
        reviewAvg=mean(review_score, na.rm=T),
        reviewscore1ct=sum(reviewscore1),
        reviewscore5ct=sum(reviewscore5)
        )%>%
    mutate(reviewscore1per=reviewscore1ct/reviewCt)%>%
    mutate(reviewscore5per=reviewscore5ct/reviewCt)%>%
    filter(reviewscore1per<0.45)%>%
    filter(reviewscore1per>0.3)%>%
    filter(reviewscore5per<0.5)%>%
    filter(reviewscore5per>0.3)%>%
    arrange(desc(reviewCt))

movie_littlsuck=movie%>%
    group_by(product_productid)%>%
    summarize(
        reviewCt=n(),
        reviewAvg=mean(review_score, na.rm=T),
        reviewscore3ct=sum(reviewscore3),
        reviewscore1ct=sum(reviewscore1)
    )%>%
    mutate(reviewscore3ct=reviewscore3ct/reviewCt)%>%
    mutate(reviewscore1ct=reviewscore1ct/reviewCt)%>%
    filter(reviewscore3ct<0.45)%>%
    filter(reviewscore3ct>0.3)%>%
    filter(reviewscore1ct<0.45)%>%
    filter(reviewscore1ct>0.3)%>%
    arrange(desc(reviewCt))


movie_worst=movie%>%
    group_by(product_productid)%>%
    summarize(
        reviewCt=n(),
        reviewAvg=mean(review_score, na.rm=T),
        reviewscore1ct=sum(reviewscore1)
    )%>%
    mutate(reviewscore1ct=reviewscore1ct/reviewCt)%>%
    filter(reviewscore1ct>0.5)%>%
    arrange(desc(reviewCt))
