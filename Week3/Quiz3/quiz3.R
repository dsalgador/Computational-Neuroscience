#Author: Daniel Salgado Rojo

#################################
#Question 1. Plotting gaussians
#################################

par(mfrow = c(1,1))

mu1 = 5
mu2 = 7

s1 = 0.5
s2 = 1

x <- seq(6-5, 6+5, length=100)
ds1 <- dnorm(x, mu1, s1)
ds2 <- dnorm(x, mu2 ,s2)

## Graphical approach
  ### Without taking into account the loss information
  
  plot(x, ds1, type = 'l', col = "blue", lwd = 2,
       xlab = "", ylab = "")
  lines(x, ds2, col = "red", lwd = 2)
  title(ylab = "Probability")
  title(xlab = "s")
  
  abline(v = 5.667, col = "green")
  abline(v = 5.830, col = "orange")
  abline(v = 2.69, col = "brown")
  abline(v = 5.978, col = "black")
  
  legend("topright",
         c("5.667", "5.830", "2.69", "5.978"),
         col = c("green", "orange", "brown", "black"),
         bty = 'n',
         cex = 1,
         seg.len = 0.5,
         lwd = 2)
  
  legend("topleft",
         c( expression( "N(" ~ mu ~ "=5, "  ~sigma ~ "= 0.5"~")") , 
            expression( "N(" ~ mu ~ "=7, "  ~sigma ~ "= 1"~")") ),
         col = c("blue", "red"),
         bty = 'n',
         cex = 1,
         seg.len = 0.5,
         lwd = 2)
  
  ### Taking into account the loss information
  
  ds2 <- 0.5*ds2
  
  plot(x, ds1, type = 'l', col = "blue", lwd = 2, 
       xlab = "", ylab = "")
  lines(x, ds2, col = "red", lwd = 2)
  
  abline(v = 5.667, col = "green")
  abline(v = 5.830, col = "orange")
  abline(v = 2.69, col = "brown")
  abline(v = 5.978, col = "black")
  
  legend("topright",
         c("5.667", "5.830", "2.69", "5.978"),
         col = c("green", "orange", "brown", "black"),
         bty = 'n',
         cex = 1,
         seg.len = 0.5,
         lwd = 2)
  
  legend("topleft",
         c( expression( "N(" ~ mu ~ "=5, "  ~sigma ~ "= 0.5"~")") , 
            expression( "0.5 N(" ~ mu ~ "=7, "  ~sigma ~ "= 1"~")") ),
         col = c("blue", "red"),
         bty = 'n',
         cex = 1,
         seg.len = 0.5,
         lwd = 2)
  
  title(ylab = "Probability")
  title(xlab = "s")

## Numerical approach

 my_f <- function(x, loss_factor = 0.5){
         return(dnorm(x, mu1, s1)-loss_factor * dnorm(x, mu2, s2))
 }
 
 #Central root
 s_star <- uniroot(my_f, c (4,6))$root
 print( paste("s* is ", round(s_star,3) ))
 
 #Left root
 uniroot(my_f, c (1,4))$root
 #Right root
 uniroot(my_f, c (9,50))$root
 