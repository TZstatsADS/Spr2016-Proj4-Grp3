library(rvest)
library(stringr)
library(tidyr)
library(dplyr)
movies.raw=read.csv("./moviescsv_review.csv")
#Amazon genres to our 10 categories
action_adv_war = "Action & Adventure Military & War"
sports = "Exercise & Fitness Sports "
family_ani = "Animation Kids & Family "
comedy = "Comedy"
mystery_drama = "Drama Mystery & Thrillers"
doc_bio_hist = "Documentary"
musical = "Music Videos & Concerts"
horror = "Horror Science Fiction"
romance = "Romance"
western = "Westerns"

#Input testing movie list and get the frequency table
movieList =cbind(c("B001OGWY1W","B001KZG99A","B004C3DLJ8","B0054NRPMO","B000XSEPYQ"),c(2,3,4,5,3))

freq_table = matrix(rep(0, 11*length(movieList[,1])), nrow = length(movieList[,1]), ncol = 11)
for (i in 1:length(movieList[,1])) {
  ASIN.inq = movieList[i,1]
  movie1<- read_html(paste("http://www.amazon.com/exec/obidos/ASIN/",
                      ASIN.inq, sep=""))
  categoryList = movie1 %>% html_node("#dv-center-features div td") %>% html_text() %>% strsplit(",")
  categoryList=lapply(categoryList, function(x) str_trim(x,side='both'))
  for (j in 1:length(categoryList[[1]])) {
    #Convert Amazon genres to our 10 genres
    #print(categoryList[[1]][j])
    if (grepl(categoryList[[1]][j],action_adv_war)) {freq_table[i,2] = 1}
    if (grepl(categoryList[[1]][j],sports)) {freq_table[i,3] = 1}
    if (grepl(categoryList[[1]][j],family_ani)) {freq_table[i,4] = 1}
    if (grepl(categoryList[[1]][j],comedy)) {freq_table[i,5] = 1}
    if (grepl(categoryList[[1]][j],mystery_drama)) {freq_table[i,6] = 1}
    if (grepl(categoryList[[1]][j],doc_bio_hist)) {freq_table[i,7] = 1}
    if (grepl(categoryList[[1]][j],musical)) {freq_table[i,8] = 1}
    if (grepl(categoryList[[1]][j],horror)) {freq_table[i,9] = 1}
    if (grepl(categoryList[[1]][j],romance)) {freq_table[i,10] = 1}
    if (grepl(categoryList[[1]][j],western)) {freq_table[i,11] = 1}
  }
}

#Input movies' frequency
input_f = colSums(freq_table[,2:11]) / sum(colSums(freq_table[,2:11]))

#Create frequency table
review.table = filter(movies.raw, action_adv_war_n != 0 & sports_n != 0 & family_ani_n != 0 &
                      comedy_n != 0 & mystery_drama_n != 0 & doc_bio_hist_n != 0 & musical_n != 0 &
                      horror_n != 0 & romance_n != 0 & western_n != 0)

review.table.join = review.table %>% 
                    group_by(product_productid) %>% 
                    summarize(review.count=n(),action_adv_war_f = mean(action_adv_war_n),
                              sports_f = mean(sports_n),family_ani_f = mean(family_ani_n),
                              comedy_f = mean(comedy_n),mystery_drama_f = mean(mystery_drama_n),
                              doc_bio_hist_f = mean(doc_bio_hist_n),musical_f = mean(musical_n),
                              horror_f = mean(horror_n),romance_f = mean(romance_n),
                              western_f = mean(western_n))
review.table.join.filter = filter(review.table.join, action_adv_war>input_f[1]-0.1 & 
                                  sports_f>input_f[2]-0.1 & family_ani_f>input_f[3]-0.1 & 
                                  comedy_f>input_f[4]-0.1 & mystery_drama_f >input_f[5]-0.1 & 
                                  doc_bio_hist_f >input_f[6]-0.1 & musical_f>input_f[7]-0.1 & 
                                  horror_f >input_f[8]-0.1 & romance_f >input_f[9]-0.1 & 
                                  western_f>input_f[10]-0.1)
review.table.index = review.table.join.filter[,1:2]
review.table.f = review.table.join.filter[,3:12]
####
similarity = vector()
for(i in 1:dim(review.table.f)[1]){
  a = as.numeric(1/dist(rbind(as.numeric(review.table.f[i,]),input_f)))
  similarity = cbind(similarity,a) 
}