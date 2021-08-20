RandomWalk <- function(x, size=1827){
  # This function is used to generate random walk
  # x : the point that you want to reach
  # size : how large the sample size you want to have at one time. This has default value 1000
  
  # If the point is too large, try to choose larger sample size to shorten the time.
  set.seed(123) # To generate same result every time
  previous <- 0
  positions <- 0
  s<-1
  final <- 0
  continue <- TRUE
  while(continue){
    move <- sample(c(1,-1), size = size,TRUE)
    previous <- tail(final,1) +cumsum(move)
      if(!is.na(which(previous==x)[1])){
        position <- which(previous==x)[1]
        cat("The total steps by far is: ", position+(s-1)*size, "\n")
        continue <- FALSE
      }else{
        positions[s] <- previous[size]
        final<-tail(positions,1)
        s <- s+1
      }
  }
}
RandomWalk(50)

