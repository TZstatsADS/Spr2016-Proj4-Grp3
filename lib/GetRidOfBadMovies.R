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
