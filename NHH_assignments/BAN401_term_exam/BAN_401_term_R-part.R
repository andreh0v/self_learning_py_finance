#A dict looking r-option called named list
# BAN401 Problem 4 - Marketing Campaign Optimization
# This problem is solved with bruth force optimization. This is possible with smaller number of combinations. But larger sets yields problems.
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
                  if(total_cost <= budget){ #If oustide budget, continue looking
                    if(total_return > best_return){ #If less than best return, continue else update & continue
                      best_return <- total_return #The lines replaces best with new, if fits restrictions & is better
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
cat("The optimal combination of products:\n")
for(j in 1:9){ #Goes through all the products in line & prints only the products that are appart of best
  if(best_combo[j] == 1){
    cat("-", product[j], "\n")
  }
}
#Cat = py print()
cat("Total promotion cost:", best_cost, "NOK\n")
cat("Total expected return:", best_return, "NOK\n")
# R diffrencecs vs py:
#<- instead of = for assignment
#c() instead of [] for vectors
#for(x in 0:1) instead of for x in range(0,2)
#cat() instead of print()/f-strings
# if(condition){ instead of if condition:
##Problem 5 - comparing each day agains previous 3
set.seed(123)
sales <- round(runif(30, min = 80, max = 120))
labels <- c()

for(i in 4:30){
  avg <- mean(sales[(i-3):(i-1)])
  if (sales[i] >= avg * 1.2){
  label <- "high"
  }else if (sales[i] <= avg *0.8) {
     label <-"low"
  }else{
       label <- "normal"
  }
  labels <- c(labels,label)} #is after the code to store the data that has been decided.
cat("Labels for day 4 to day 10:\n")
for (j in 1:7){#A loop is necessary to gett a day outout
  cat("Day", j+3, ":", labels[j], "\n")
}
cat("")
cat("\n Total counts:\n")
print(table(labels))


