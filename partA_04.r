whole_data <- read.csv('london_pollution.csv')

Bloomsbury <- whole_data[,'Bloomsbury']

N = 1827
x = Bloomsbury
# regression model for DVs
y = 100 + 3*x + rnorm(N,0,10)
## Build the JAGS model
mod_str = "
model{
    B.pred[1]~dnorm(0, 1.0E-3)
  for(i in 2:length(x)){
    # regression model on y, given x
    y[i] ~ dnorm( B.pred[i], tau.v )
    factor = i-1
    B.pred[i] <- dnorm(B.pred[factor],tau.w)
    
    # Stochastic model on x
    #x[i] ~ dnorm( B.pred[i], tau.w)
  }
  
  # priors for demonstration only
  tau.w ~ dgamma(1,0.01)
  sigma.w2 <- 1/tau.w
  tau.v ~ dgamma(1,0.01)
  sigma.v2 <- 1/tau.v
}
"
for_jags = list(x=x,y=y)

library(rjags)
## Compile the model
jmod = jags.model(file = textConnection(mod_str), data = for_jags)
## Sample from the posterior
#samples = coda.samples(jmod, c("y","x"), n.iter = 2)

