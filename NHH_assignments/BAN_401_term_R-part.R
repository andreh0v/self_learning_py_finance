#A dict looking r-option called named list
# BAN401 Problem 4 - Marketing Campaign Optimization

# Products
product <- c("wireless mouse", "smart speaker", "LED monitor", "USB hub",
             "keyboard", "power bank", "webcam", "gaming chair", "laptop stand")
# Promotion costs
promotion_cost <- c(12000, 18000, 30000, 6000, 10000, 8000, 11000, 25000, 9000)
# Expected returns
expected_return <- c(22000, 30000, 45000, 9000, 17000, 14000, 18000, 37000, 16000)
# Budget constraint
budget <- 100000
best_return <- 0
best_cost <- 0
best_combo <- c()


for(a in 0:1){
  for(b in 0:1){
    for(c in 0:1){
      for(d in 0:1){
        for(e in 0:1){
          for(f in 0:1){
            for(g in 0:1){
              for(h in 0:1){
                for(i in 0:1){
                  selected <- c(a, b, c, d, e, f, g, h, i)
                  total_cost <- sum(promotion_cost * selected)
                  total_return <- sum(expected_return * selected)
                  if(total_cost <= budget){
                    if(total_return > best_return){
                      best_return <- total_return
                      best_cost <- total_cost
                      best_combo <- selected
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}
for(j in 1:9){
  if(best_combo[j] == 1){
    cat("-", product[j], "\n")
  }
}
cat("The optimal combination of products:\n")
cat("Total promotion cost:", best_cost, "NOK\n")
cat("Total expected return:", best_return, "NOK\n")
