library (MASS)
library (coefficientalpha)
library (psych)
library (GPArotation)

Original <- data.frame(Covid_NY)


Original1 <- subset(Original, Original$Count==1)
Original1 <- subset(Original1, select= c(23:36))

#for alfa
Original2 <- subset(Original1, select= c(1,2,3,5,6))
Original3 <- subset(Original1, select= c(7,8,9))
Original4 <- subset(Original1, select= c(10, 11))


#Original1 <- subset(Original, select= c(22:46))
#Original1 <- subset(Original1, select= -c(1:3,6,8,10:13,17,19,20,22:25))


alpha(Original1,check.keys=TRUE)           #Total

alpha(Original2,check.keys=TRUE)           #Total
alpha(Original3,check.keys=TRUE)           #Total
alpha(Original4,check.keys=TRUE)           #Total


# Correlation Matrix  (spearman correlation)

SpearmanCorr <- cor(Original1, method = "spearman")
#View(SpearmanCorr)

#write.table(SpearmanCorr, "H:/Factanalisis/Spear.txt", sep="\t")
#write.table(SpearmanCorr, file = "H:/Factanalisis/SpearmanCorr.csv", sep = ",", col.names = FALSE,row.names=FALSE) 

# Determinant of the correlation matrix r

det(SpearmanCorr)

#KMO

KMO.result <- KMO(SpearmanCorr)
KMO.result

# Barlett's test cortest.bartlett

bartlett <- cortest.bartlett(SpearmanCorr, n=439)
bartlett


# Principal Axis Factor Analysis

#Varimax rotation factors loading

solution2 <- fa(SpearmanCorr, nfactors= 2, rotate = "varimax", fm = "ml") 
solution2

solution3 <- fa(SpearmanCorr, nfactors=3,rotate = "varimax", fm = "pa") 
solution3

solution4 <- fa(SpearmanCorr, nfactors= 4,rotate = "varimax", fm = "pa") 
solution4

write.table(solution5, "H:/Factanalisis/solutionf.txt", sep="\t")


#Factor score coefficient matrix for each OBS
fscores.2<- factor.scores(Original1, solution2, method = c("Thurstone"))
fscores.2
Score2Matrix <- fscores.2$scores
View(Score2Matrix)


fscores.3<- factor.scores(Original1, solution3, method = c("Thurstone"))
fscores.3
Score3Matrix <- fscores.3$scores
View(Score3Matrix)

fscores.5<- factor.scores(Original, solution5, method = c("Thurstone"))
fscores.5
Score5Matrix <- fscores.5$scores
View(Score5Matrix)

#export table
write.table(Score2Matrix, "Desktop/Score2Matrix.txt", sep="\t",row.names = FALSE)

write.table(Score3Matrix, "Desktop/Score3Matrix.txt", sep="\t",row.names = FALSE)
