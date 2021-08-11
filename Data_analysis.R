library(ggpubr)
library(ggplot2)
library(gridExtra)
library(ggalluvial)
library(scales)
library(ggrepel)
library(reshape2)
library(dplyr)
library(tidyr)
library(likert)
library(gridExtra)


        datafirst <- data.frame(Models_Acclaim_4)
datafirst
# New facet label names for supp variable
Purp.labs <- c("Business trip", "Personal trip", "All purposes")
names(Purp.labs) <- c("bus", "pers","both")



dataCost <- datafirst[which(datafirst$Variable == "Cost"),]
citycol <- setNames( c('coral1','darkolivegreen3','cyan3', 'mediumorchid')
                     , levels(datafirst$City)  )

cityshap <- setNames( c(16, 17, 15,3)
                      , levels(datafirst$City)  )

ggplot(dataCost) +
  geom_pointrange( aes(x=Distance, y=Value, ymin=Value-Robust_Std_err, ymax=Value+Robust_Std_err ,colour=City,shape=City), alpha=0.9, size=0.7)+ 
  scale_color_manual(values = citycol) +
  scale_shape_manual(values =cityshap )+
  ggtitle("Fare") +
  theme_bw()+
  xlab("Flight distance") + ylab("Estimate (+/- SE)") +
  facet_wrap(~Purp, labeller = labeller(Purp = Purp.labs)) +  
  theme(plot.title = element_text(hjust = 0.5, face="bold")) + 
  theme(legend.title = element_text(face="bold")) +
  theme(strip.background =element_rect(fill="white"))  
  


datadeptime <- datafirst[which(datafirst$Variable == "Departure time"),]
citycol <- setNames( c('coral1','darkolivegreen3','cyan3', 'mediumorchid')
#citycol <- setNames( c('blue','coral1', 'cyan3', 'darkolivegreen3', 'mediumorchid')
                     , levels(datafirst$City)  )

cityshap <- setNames( c(16, 17, 15,3)
                      , levels(datafirst$City)  )
#cityshap <- setNames( c(18,16, 17, 15,3)
#                      , levels(datafirst$City)  )

ggplot(datadeptime) +
  geom_pointrange( aes(x=Distance, y=Value, ymin=Value-Robust_Std_err, ymax=Value+Robust_Std_err ,colour=City,shape=City), alpha=0.9, size=0.7)+ 
  scale_color_manual(values = citycol) +
  scale_shape_manual(values =cityshap )+
  ggtitle("Time at the departure airport") +
  theme_bw() +
  xlab("Flight distance") + ylab("Estimate (+/- SE)") +
  facet_wrap(~Purp, labeller = labeller(Purp = Purp.labs)) +  
  theme(plot.title = element_text(hjust = 0.5, face="bold")) + 
  theme(legend.title = element_text(face="bold")) +
  theme(strip.background =element_rect(fill="white")) 



dataarrtime <- datafirst[which(datafirst$Variable == "Arrival time"),]

ggplot(dataarrtime) +
  geom_pointrange( aes(x=Distance, y=Value, ymin=Value-Robust_Std_err, ymax=Value+Robust_Std_err ,colour=City,shape=City), alpha=0.9, size=0.7)+ 
  scale_color_manual(values = citycol) +
  scale_shape_manual(values =cityshap )+
  ggtitle("Time at the arrival airport") +
  theme_bw() +
  xlab("Flight distance") + ylab("Estimate (+/- SE)") +
  facet_wrap(~Purp, labeller = labeller(Purp = Purp.labs)) +  
  theme(plot.title = element_text(hjust = 0.5, face="bold")) + 
  theme(legend.title = element_text(face="bold")) +
  theme(strip.background =element_rect(fill="white")) 


datatransfer <- datafirst[which(datafirst$Variable == "Transfer"),]

ggplot(datatransfer) +
  geom_pointrange( aes(x=Distance, y=Value, ymin=Value-Robust_Std_err, ymax=Value+Robust_Std_err ,colour=City,shape=City), alpha=0.9, size=0.7)+ 
  #scale_color_manual(values = citycol) +
  #scale_shape_manual(values =cityshap )+
  ggtitle("Transfer") +
  theme_bw() +
  xlab("Flight distance") + ylab("Estimate (+/- SE)") +
  facet_wrap(~Purp, labeller = labeller(Purp = Purp.labs)) +  
  theme(plot.title = element_text(hjust = 0.5, face="bold")) + 
  theme(legend.title = element_text(face="bold")) +
  theme(strip.background =element_rect(fill="white")) 



datasocioecon <- subset(datafirst, Count >= 84 & Count <= 91 )

citycol <- setNames( c('coral1', 'darkolivegreen3', 'mediumorchid','cyan3')
                     , levels(datafirst$City)  )

cityshap <- setNames( c(16, 17, 3)
                      , levels(datafirst$City)  )

ggplot(datasocioecon) +
  geom_pointrange( aes(x=Variable, y=Value, ymin=Value-Robust_Std_err, ymax=Value+Robust_Std_err ,colour=City,shape=City), alpha=0.9, size=0.7)+ 
  ggtitle("Socioeconomic variables \n and virtual software use") +
  scale_color_manual(values = citycol) +
  scale_shape_manual(values =cityshap )+
  theme_bw() +
  xlab(element_blank()) + ylab("Estimate (+/- SE)") +
  #facet_wrap(~Purp, labeller = labeller(Purp = Purp.labs)) +  
  theme(plot.title = element_text(hjust = 0.5, face="bold")) + 
  theme(legend.title = element_text(face="bold")) +
  theme(axis.text.x = element_text(angle = 45,hjust = 1)) +
  theme(strip.background =element_rect(fill="white")) 


datalat <- subset(datafirst, Count == 92 | Count == 112 | Count == 123 | Count == 142 )

citycol <- setNames( c('coral1', 'darkolivegreen3', 'cyan3','mediumorchid')
                     , levels(datafirst$City)  )

cityshap <- setNames( c(16, 17, 15,3)
                      , levels(datafirst$City)  )

ggplot(datalat) +
  geom_pointrange( aes(x=Variable, y=Value, ymin=Value-Robust_Std_err, ymax=Value+Robust_Std_err ,colour=City,shape=City), alpha=0.9, size=0.7)+ 
  ggtitle("Latent safety perception") +
  scale_color_manual(values = citycol) +
  scale_shape_manual(values =cityshap )+
  theme_bw() +
  xlab(element_blank()) + ylab("Estimate (+/- SE)") +
  #facet_wrap(~Purp, labeller = labeller(Purp = Purp.labs)) +  
  theme(plot.title = element_text(hjust = 0.5, face="bold")) + 
  theme(legend.title = element_text(face="bold")) +
  theme(axis.text.x = element_text(angle = 45,hjust = 1)) +
  theme(strip.background =element_rect(fill="white")) 

#Worries of catching COVID-19
#Safety measures
#Quarantine issue


datalatafr <- subset(datafirst, Count >= 94 & Count <= 97 )
plot1<- ggplot(datalatafr) +
  geom_pointrange( aes(x=Variable, y=Value, ymin=Value-Robust_Std_err, ymax=Value+Robust_Std_err), alpha=0.9, size=0.7,colour="coral1")+ 
  ggtitle("SMC - Latent 'Afraid of \n catching COVID-19' (London)") +
  theme_bw() +
  xlab(element_blank()) + ylab("Estimate (+/- SE)") +
  #facet_wrap(~Purp, labeller = labeller(Purp = Purp.labs)) +  
  theme(plot.title = element_text(hjust = 0.5, face="bold")) + 
  #theme(legend.title = element_text(face="bold")) +
  theme(axis.text.x = element_text(angle = 45,hjust = 1)) +
  theme(strip.background =element_rect(fill="white")) 
plot1


datalatquar <- subset(datafirst, Count >= 114 & Count <= 117 )
plot2<- ggplot(datalatquar) +
  geom_pointrange( aes(x=Variable, y=Value, ymin=Value-Robust_Std_err, ymax=Value+Robust_Std_err), alpha=0.9, size=0.7,colour="mediumorchid", shape = 3)+ 
  ggtitle("SMC - Latent\n'Dislike of quarantine' (Shanghai)") +
  theme_bw() +
  xlab(element_blank()) + ylab("Estimate (+/- SE)") +
  #facet_wrap(~Purp, labeller = labeller(Purp = Purp.labs)) +  
  theme(plot.title = element_text(hjust = 0.5, face="bold")) + 
  #theme(legend.title = element_text(face="bold")) +
  theme(axis.text.x = element_text(angle = 45,hjust = 1)) +
  theme(strip.background =element_rect(fill="white")) 
plot2


datalatafr2 <- subset(datafirst, Count >= 125 & Count <= 127 )
plot3<- ggplot(datalatafr2) +
  geom_pointrange( aes(x=Variable, y=Value, ymin=Value-Robust_Std_err, ymax=Value+Robust_Std_err), alpha=0.9, size=0.7,colour= "cyan3", shape = 15)+ 
  ggtitle("SMC - Latent 'Afraid of \n catching COVID-19' (Sao Paulo)") +
  theme_bw() +
  xlab(element_blank()) + ylab(element_blank()) +
  #facet_wrap(~Purp, labeller = labeller(Purp = Purp.labs)) +  
  theme(plot.title = element_text(hjust = 0.5, face="bold")) + 
  #theme(legend.title = element_text(face="bold")) +
  theme(axis.text.x = element_text(angle = 45,hjust = 1)) +
  theme(strip.background =element_rect(fill="white")) 
plot3


datalatsaf <- subset(datafirst, Count >= 144 & Count <= 146 )
plot4<- ggplot(datalatsaf) +
  geom_pointrange( aes(x=Variable, y=Value, ymin=Value-Robust_Std_err, ymax=Value+Robust_Std_err), alpha=0.9, size=0.7,colour="darkolivegreen3", shape = 17)+ 
  ggtitle("SMC - Latent\n'Trust in safety measures' (New York)") +
  theme_bw() +
  xlab(element_blank()) + ylab(element_blank()) +
  #facet_wrap(~Purp, labeller = labeller(Purp = Purp.labs)) +  
  theme(plot.title = element_text(hjust = 0.5, face="bold")) + 
  #theme(legend.title = element_text(face="bold")) +
  theme(axis.text.x = element_text(angle = 45,hjust = 1)) +
  theme(strip.background =element_rect(fill="white")) 
plot4


grid.arrange(plot1,plot4,
             plot2, plot3, nrow=2, ncol=2)

grid.arrange(plot1,plot4,
             plot3, plot2, nrow=2, ncol=2)

############FreqAnalysis#################


datasecond1 <- data.frame(Covid_tot_forPlot)
datasecond <- datasecond1[which( datasecond1$Choice != -990  &  (datasecond1$ID != 1331 | datasecond1$Count != 3)),]
datasecond <- datasecond[which(datasecond$Count==5),]

Purpose <- as.numeric(datasecond$Purpose_SP > 1)
Flight <- as.numeric(datasecond$International == 1)

Choice2 <- as.numeric(datasecond$Old_Choice == 3)

Purpose <- recode(Purpose,"0" = "Personal", "1"= "Business")
Choice2.r <- recode(Choice2, "0"= "Yes", "1"= "No")
Flight.r <- recode(Flight, "0" = "Domestic", "1"= "International")

City.labs <- c("London \n (respondents=388)", "New York \n (respondents=228)", "Shanghai \n (respondents=414)", "Sao Paulo \n (respondents=439)")
#City.labs <- c("London \n (observations=2316)", "New York \n (observations=1368)", "Shanghai \n (observations=2484)", "Sao Paulo \n (observations=2634)")

					

names(City.labs) <- c("1", "2","3","4")


n_id <- length(datasecond$Count)

ggplot(as.data.frame(datasecond),
       aes(axis1 = Purpose, axis2 = Choice2.r)) +
  theme_bw() +
  geom_flow(aes(fill = Purpose, colour = Purpose), alpha = .5, width = 1/12) +
  geom_stratum(width = 1/7, fill = "grey", color = "white") +
  geom_text(stat = "stratum", aes(label = after_stat(stratum)), color = "black", size = 3, vjust = -0.15) + 
  geom_text(stat = "stratum",aes(label = percent(after_stat(prop), accuracy = .1)),color = "black",  size = 3, vjust = 1.05) +
  geom_text(stat = "flow",aes(label = percent(round(after_stat(prop), 3), accuracy = .1)), color = "white", size = 3, nudge_x = 0.15)+
  scale_x_discrete(limits = c("Purpose of \n the trip", "Type of \n flight"), expand = c(.05, .05)) +
  #scale_x_discrete(limits = c("Purpose of \n the trip", "SP travelling \n choice"), expand = c(.05, .05)) +
  scale_fill_brewer(type = "qual", palette = "Set1") +
  #ggtitle("Choice after Covid-19: travelling again or not?")+
  facet_wrap(~City, labeller = labeller(City = City.labs)) +  
  theme(strip.background = element_rect(fill="white")) +
  theme(strip.text=  element_text(face="bold", size = 11))+
  xlab(element_blank()) + ylab("Number of respondents") +
  #xlab(element_blank()) + ylab("Number of SP observations") +
  theme(legend.title = element_text(face="bold"))+ 
  theme(plot.title = element_text(hjust = 0.5, face="bold", size = 14))

#London
datalondon <- datasecond[which( datasecond$City ==1 ),]
Purpose <- as.numeric(datalondon$Purpose_SP > 1)
Choice2 <- as.numeric(datalondon$Old_Choice == 3)
Purpose <- recode(Purpose,"0" = "Personal", "1"= "Business")
Choice2.r <- recode(Choice2, "0"= "Yes", "1"= "No")


ggplot(as.data.frame(datalondon),
       aes(axis1 = Purpose, axis2 = Choice2.r)) +
  theme_bw() +
  geom_flow(aes(fill = Purpose, colour = Purpose), alpha = .5, width = 1/12) +
  geom_stratum(width = 1/12, fill = "grey", color = "black") +
  geom_text(stat = "stratum", aes(label = after_stat(stratum)), size = 3, vjust = -0.2) + 
  geom_text(stat = "stratum",aes(label = percent(after_stat(prop), accuracy = .1)), size = 3, vjust = 1.5) +
  geom_text(stat = "flow",aes(label = percent(after_stat(prop))), color = "white", size = 3, nudge_x = 0.08)+
  scale_x_discrete(limits = c("Purpose of \n the trip", "SP travelling \n choice"), expand = c(.05, .05)) +
  scale_fill_brewer(type = "qual", palette = "Set1") +
  ggtitle("Choice after Covid-19: travelling again or not?\n(London)")+
#  facet_wrap(~City, labeller = labeller(City = City.labs)) +  
#  theme(strip.background = element_rect(fill="white")) +
  theme(strip.text=  element_text(face="bold", size = 11))+
  xlab(element_blank()) + ylab("Number of SP choices") +
  theme(legend.title = element_text(face="bold"))+ 
  theme(plot.title = element_text(hjust = 0.5, face="bold", size = 14))

#NY
datacity <- datasecond[which( datasecond$City ==2 ),]
Purpose <- as.numeric(datacity$Purpose_SP > 1)
Choice2 <- as.numeric(datacity$Old_Choice == 3)
Purpose <- recode(Purpose,"0" = "Personal", "1"= "Business")
Choice2.r <- recode(Choice2, "0"= "Yes", "1"= "No")


ggplot(as.data.frame(datacity),
       aes(axis1 = Purpose, axis2 = Choice2.r)) +
  theme_bw() +
  geom_flow(aes(fill = Purpose, colour = Purpose), alpha = .5, width = 1/12) +
  geom_stratum(width = 1/12, fill = "grey", color = "black") +
  geom_text(stat = "stratum", aes(label = after_stat(stratum)), size = 3, vjust = -0.2) + 
  geom_text(stat = "stratum",aes(label = percent(after_stat(prop), accuracy = .1)), size = 3, vjust = 1.5) +
  geom_text(stat = "flow",aes(label = percent(after_stat(prop))), color = "white", size = 3, nudge_x = 0.08)+
  scale_x_discrete(limits = c("Purpose of \n the trip", "SP travelling \n choice"), expand = c(.05, .05)) +
  scale_fill_brewer(type = "qual", palette = "Set1") +
  ggtitle("Choice after Covid-19: travelling again or not?\n(New York)")+
  #  facet_wrap(~City, labeller = labeller(City = City.labs)) +  
  #  theme(strip.background = element_rect(fill="white")) +
  theme(strip.text=  element_text(face="bold", size = 11))+
  xlab(element_blank()) + ylab("Number of SP choices") +
  theme(legend.title = element_text(face="bold"))+ 
  theme(plot.title = element_text(hjust = 0.5, face="bold", size = 14))

#Sh
datacity <- datasecond[which( datasecond$City ==3 ),]
Purpose <- as.numeric(datacity$Purpose_SP > 1)
Choice2 <- as.numeric(datacity$Old_Choice == 3)
Purpose <- recode(Purpose,"0" = "Personal", "1"= "Business")
Choice2.r <- recode(Choice2, "0"= "Yes", "1"= "No")


ggplot(as.data.frame(datacity),
       aes(axis1 = Purpose, axis2 = Choice2.r)) +
  theme_bw() +
  geom_flow(aes(fill = Purpose, colour = Purpose), alpha = .5, width = 1/12) +
  geom_stratum(width = 1/12, fill = "grey", color = "black") +
  geom_text(stat = "stratum", aes(label = after_stat(stratum)), size = 3, vjust = -0.2) + 
  geom_text(stat = "stratum",aes(label = percent(after_stat(prop), accuracy = .1)), size = 3, vjust = 1.5) +
  geom_text(stat = "flow",aes(label = percent(after_stat(prop))), color = "white", size = 3, nudge_x = 0.08)+
  scale_x_discrete(limits = c("Purpose of \n the trip", "SP travelling \n choice"), expand = c(.05, .05)) +
  scale_fill_brewer(type = "qual", palette = "Set1") +
  ggtitle("Choice after Covid-19: travelling again or not?\n(Shanghai)")+
  #  facet_wrap(~City, labeller = labeller(City = City.labs)) +  
  #  theme(strip.background = element_rect(fill="white")) +
  theme(strip.text=  element_text(face="bold", size = 11))+
  xlab(element_blank()) + ylab("Number of SP choices") +
  theme(legend.title = element_text(face="bold"))+ 
  theme(plot.title = element_text(hjust = 0.5, face="bold", size = 14))

#P
datacity <- datasecond[which( datasecond$City ==4 ),]
Purpose <- as.numeric(datacity$Purpose_SP > 1)
Choice2 <- as.numeric(datacity$Old_Choice == 3)
Purpose <- recode(Purpose,"0" = "Personal", "1"= "Business")
Choice2.r <- recode(Choice2, "0"= "Yes", "1"= "No")


ggplot(as.data.frame(datacity),
       aes(axis1 = Purpose, axis2 = Choice2.r)) +
  theme_bw() +
  geom_flow(aes(fill = Purpose, colour = Purpose), alpha = .5, width = 1/12) +
  geom_stratum(width = 1/12, fill = "grey", color = "black") +
  geom_text(stat = "stratum", aes(label = after_stat(stratum)), size = 3, vjust = -0.2) + 
  geom_text(stat = "stratum",aes(label = percent(after_stat(prop), accuracy = .1)), size = 3, vjust = 1.5) +
  geom_text(stat = "flow",aes(label = percent(after_stat(prop))), color = "white", size = 3, nudge_x = 0.08)+
  scale_x_discrete(limits = c("Purpose of \n the trip", "SP travelling \n choice"), expand = c(.05, .05)) +
  scale_fill_brewer(type = "qual", palette = "Set1") +
  ggtitle("Choice after Covid-19: travelling again or not?\n(Sao Paulo)")+
  #  facet_wrap(~City, labeller = labeller(City = City.labs)) +  
  #  theme(strip.background = element_rect(fill="white")) +
  theme(strip.text=  element_text(face="bold", size = 11))+
  xlab(element_blank()) + ylab("Number of SP choices") +
  theme(legend.title = element_text(face="bold"))+ 
  theme(plot.title = element_text(hjust = 0.5, face="bold", size = 14))

##############################




# Stacked + percent

dataplot <- data.frame(Covid_tot_forPlot, check.names=FALSE)
dataplot <- dataplot[which( dataplot$Choice != -990  &  (dataplot$ID != 1331 | dataplot$Count != 3)),]
dataplot <- dataplot[which( dataplot$Count == 1 ),]


datadataplotlondon <- dataplot[which( dataplot$City ==1 ),]

dataSafLond <- subset(datadataplotlondon, select= c(25:38))



choices  = c("Strongly disagree",	"Somewhat disagree",	"Neutral",	"Somewhat agree", "Strongly agree")
for(i in 1:14) {
  dataSafLond[,i] = factor(dataSafLond[,i], levels=1:5, labels=choices, ordered=TRUE)
}

write.table(dataSafLond, "~/Desktop/dataSafLond.txt", sep="\t",row.names = FALSE)

dataSafLond_lik <- likert(dataSafLond)


plot1pl <-  plot(dataSafLond_lik, ordered=FALSE,
     grid.range = c(1, 1),
     expand.grid = FALSE,
     values = "sum.outside",
     show.prc.sign = TRUE,text.size=3
     )+
  ggtitle("Safety perception and attitudes - London (n=386)") +
  #theme(legend.title = element_text(face="bold"))+ 
  theme(axis.text.y = element_text(size=8), axis.title.x = element_blank()) +
  theme(plot.title = element_text(hjust = 0.5, face="bold", size = 14))+ 
  theme(legend.position="none")


#############
datadataplotNY <- dataplot[which( dataplot$City ==2 ),]

dataSafNY <- subset(datadataplotNY, select= c(25:38))


choices  = c("Strongly disagree",	"Somewhat disagree",	"Neutral",	"Somewhat agree", "Strongly agree")
for(i in 1:14) {
  dataSafNY[,i] = factor(dataSafNY[,i], levels=1:5, labels=choices, ordered=TRUE)
}
write.table(dataSafNY, "~/Desktop/dataSafNy.txt", sep="\t",row.names = FALSE)

dataSafNY_lik <- likert(dataSafNY)


plot2pl <-  plot(dataSafNY_lik, ordered=FALSE,
                 grid.range = c(1, 1),
                 expand.grid = FALSE,
                 values = "sum.outside",
                 show.prc.sign = TRUE,text.size=3
)+
  ggtitle("Safety perception and attitudes - New York (n=228)") +
  theme(legend.title = element_text(face="bold"))+ 
  theme(axis.text.y = element_text(size=8), axis.title.x = element_blank()) +
  theme(plot.title = element_text(hjust = 0.5, face="bold", size = 14))

#############
datadataplotSH <- dataplot[which( dataplot$City ==3 ),]

dataSafSH <- subset(datadataplotSH, select= c(25:38))


choices  = c("Strongly disagree",	"Somewhat disagree",	"Neutral",	"Somewhat agree", "Strongly agree")
for(i in 1:14) {
  dataSafSH[,i] = factor(dataSafSH[,i], levels=1:5, labels=choices, ordered=TRUE)
}
write.table(dataSafSH, "~/Desktop/dataSafSH.txt", sep="\t",row.names = FALSE)


dataSafSH_lik <- likert(dataSafSH)


plot3pl <-  plot(dataSafSH_lik, ordered=FALSE,
              #   grid.range = c(0.2, 1),
                 expand.grid = FALSE,
                 values = "sum.outside",
                 show.prc.sign = TRUE,text.size=3
)+
  ggtitle("Safety perception and attitudes - Shanghai (n=414)") +
  #theme(legend.title = element_text(face="bold"))+ 
  theme(axis.text.y = element_text(size=8), axis.title.x = element_blank()) +
  
  #guides(x = "none") + 
  theme(plot.title = element_text(hjust = 0.5, face="bold", size = 14)) +
  theme(legend.position="none")


#plot3pl
#############
datadataplotSP <- dataplot[which( dataplot$City == 4 ),]

dataSafSP <- subset(datadataplotSP, select= c(25:38))


choices  = c("Strongly disagree",	"Somewhat disagree",	"Neutral",	"Somewhat agree", "Strongly agree")
for(i in 1:14) {
  dataSafSP[,i] = factor(dataSafSP[,i], levels=1:5, labels=choices, ordered=TRUE)
}

write.table(dataSafSP, "~/Desktop/dataSafSP.txt", sep="\t",row.names = FALSE)

dataSafSP_lik <- likert(dataSafSP)


plot4pl <-  plot(dataSafSP_lik, ordered=FALSE,
                 grid.range = c(1, 1),
                 expand.grid = FALSE,
                 values = "sum.outside",
                 show.prc.sign = TRUE,text.size=3
)+
  ggtitle("Safety perception and attitudes - Sao Paulo (n=439)") +
  theme(legend.title = element_text(face="bold")) + 
  theme(axis.text.y = element_text(size=8), axis.title.x = element_blank()) +
  theme(plot.title = element_text(hjust = 0.5, face="bold", size = 14))

plot4pl
grid.arrange(plot1pl,plot2pl,
              nrow=2, ncol=1)

grid.arrange(
             plot3pl, plot4pl, nrow=2, ncol=1)

#########NEw Likert mismetch with different the other likert function
library(HH)


plotnew1 <- plot.likert(dataSafLond_lik,
                   horizontal=TRUE,
                   aspect=0.6, 
                   reverse=FALSE, 
                   ylab=NULL,
       main="Safety perception and attitudes - London (n=386)",
       auto.key=list(space="bottom", 
                     columns=3,
                     reverse=TRUE, padding.text=1))


plotnew2 <- likert(dataSafLond_lik,
                   horizontal=TRUE,
                   aspect=0.6, 
                   reverse=FALSE,  
                   ylab=NULL,
      main="Safety perception and attitudes - New York (n=228)",
      auto.key=list(space="bottom", 
                    columns=3,
                    reverse=TRUE, padding.text=1))


grid.arrange(plotnew1,plotnew2,
             nrow=2, ncol=1)


plotnew3 <- plot.likert(dataSafSH_lik,
                        horizontal=TRUE,
                        aspect=0.6, 
                        reverse=FALSE,  xTickLabelsPositive = TRUE,
                        ylab=NULL,
                        main="Safety perception and attitudes - Shanghai (n=414)",
                        auto.key=list(space="bottom", 
                                      columns=3,
                                      reverse=TRUE, padding.text=1))


plotnew4 <- likert(dataSafSP_lik,
                   horizontal=TRUE,
                   aspect=0.6, 
                   reverse=FALSE,  xTickLabelsPositive = TRUE,
                   ylab=NULL,
                   main="Safety perception and attitudes - Sao Paulo (n=439)",
                   auto.key=list(space="bottom", 
                                 columns=3,
                                 reverse=TRUE, padding.text=1))


grid.arrange(plotnew3,plotnew4,
             nrow=2, ncol=1)

####################Virtual B During  17:20  21:24


dataVirtLond <- subset(datadataplotlondon, select= c(17:24))

write.table(dataVirtLond, "~/Desktop/dataVirtLond.txt", sep="\t",row.names = FALSE)


dataVirtLond
choices  = c("Several times a week",	"Several times a month",	"Several times a year",	"Never")
for(i in 1:4) {
  dataVirtLond[,i] = factor(dataVirtLond[,i], levels=1:4, labels=choices, ordered=TRUE)
}


choices  = c("Much less than before Covid-19",	"Less than before Covid-19",	"Same as before Covid-19",	"More than before Covid-19", "Much more than before Covid-19")
for(i in 5:8) {
  dataVirtLond[,i] = factor(dataVirtLond[,i], levels=1:5, labels=choices, ordered=TRUE)
}


dataVirtLondBD <- subset(dataVirtLond, select= c(1:4))
dataVirtLondA <- subset(dataVirtLond, select= c(5:8))

dataVirtLond_likBD <- likert(dataVirtLondBD)
dataVirtLond_likA <- likert(dataVirtLondA)

plotnew1VBD <- plot.likert(dataVirtLond_likBD,
                        horizontal=TRUE,
                        aspect=0.3, 
                        reverse=FALSE,  xTickLabelsPositive = TRUE,
                        ylab=NULL,
                        main="Use of virtual software in place of flying - London (n=386)",
                        auto.key=list(space="bottom", 
                                      columns=2,
                                      reverse=TRUE, padding.text=1))

plotnew1VA <- plot.likert(dataVirtLond_likA,
                           horizontal=TRUE,
                           aspect=0.3, 
                           reverse=FALSE,  xTickLabelsPositive = TRUE,
                           ylab=NULL,
                           main="Potential use of virtual software in place of flying - London (n=386)",
                          auto.key=list(space="bottom", 
                                        columns=3,
                                        reverse=TRUE, padding.text=1))





dataVirtNY <- subset(datadataplotNY, select= c(17:24))
write.table(dataVirtNY, "~/Desktop/dataVirtNY.txt", sep="\t",row.names = FALSE)


choices  = c("Several times a week",	"Several times a month",	"Several times a year",	"Never")
for(i in 1:4) {
  dataVirtNY[,i] = factor(dataVirtNY[,i], levels=1:4, labels=choices, ordered=TRUE)
}


choices  = c("Much less than before Covid-19",	"Less than before Covid-19",	"Same as before Covid-19",	"More than before Covid-19", "Much more than before Covid-19")
for(i in 5:8) {
  dataVirtNY[,i] = factor(dataVirtNY[,i], levels=1:5, labels=choices, ordered=TRUE)
}

dataVirtNYBD <- subset(dataVirtNY, select= c(1:4))
dataVirtNYA <-  subset(dataVirtNY, select= c(5:8))
dataVirtN_likBD <- likert(dataVirtNYBD)
dataVirtN_likA <- likert(dataVirtNYA)


plotnew2VBD <- likert(dataVirtN_likBD,
                   horizontal=TRUE,
                   aspect=0.3, 
                   reverse=FALSE,  xTickLabelsPositive = TRUE,
                   ylab=NULL,
                   main="Use of virtual software in place of flying - New York (n=228)",
                   auto.key=list(space="bottom", 
                                 columns=2,
                                 reverse=TRUE, padding.text=1))
plotnew2VA <- likert(dataVirtN_likA,
                      horizontal=TRUE,
                      aspect=0.3, 
                      reverse=FALSE,  xTickLabelsPositive = TRUE,
                      ylab=NULL,
                      main="Potential use of virtual software in place of flying - New York (n=228)",
                     auto.key=list(space="bottom", 
                                   columns=3,
                                   reverse=TRUE, padding.text=1))

grid.arrange(plotnew1VBD, plotnew2VBD,
             nrow=2, ncol=1)
grid.arrange(plotnew1VA,plotnew2VA,
             nrow=2, ncol=1)







dataVirtSH <- subset(datadataplotSH, select= c(17:24))
write.table(dataVirtSH, "~/Desktop/dataVirtSH.txt", sep="\t",row.names = FALSE)


choices  = c("Several times a week",	"Several times a month",	"Several times a year",	"Never")
for(i in 1:4) {
  dataVirtSH[,i] = factor(dataVirtSH[,i], levels=1:4, labels=choices, ordered=TRUE)
}


choices  = c("Much less than before Covid-19",	"Less than before Covid-19",	"Same as before Covid-19",	"More than before Covid-19", "Much more than before Covid-19")
for(i in 5:8) {
  dataVirtSH[,i] = factor(dataVirtSH[,i], levels=1:5, labels=choices, ordered=TRUE)
}

dataVirtSHBD <- subset(dataVirtSH, select= c(1:4))
dataVirtSHA <- subset(dataVirtSH, select= c(5:8))
dataVirtSH_likBD <- likert(dataVirtSHBD)
dataVirtSH_likA <- likert(dataVirtSHA)


plotnew3VBD <- plot.likert(dataVirtSH_likBD,
                        horizontal=TRUE,
                        aspect=0.3, 
                        reverse=FALSE,  xTickLabelsPositive = TRUE,
                        ylab=NULL,
                        main="Use of virtual software in place of flying - Shanghai (n=414)",
                        auto.key=list(space="bottom", 
                                      columns=2,
                                      reverse=TRUE, padding.text=1))


plotnew3VA <- plot.likert(dataVirtSH_likA,
                       horizontal=TRUE,
                       aspect=0.3, 
                       reverse=FALSE,  xTickLabelsPositive = TRUE,
                       ylab=NULL,
                       main="Potential use of virtual software in place of flying - Shanghai (n=414)",
                       auto.key=list(space="bottom", 
                                     columns=3,
                                     reverse=TRUE, padding.text=1))






dataVirtSP <- subset(datadataplotSP, select= c(17:24))
write.table(dataVirtSP, "~/Desktop/dataVirtSP.txt", sep="\t",row.names = FALSE)



choices  = c("Several times a week",	"Several times a month",	"Several times a year",	"Never")
for(i in 1:4) {
  dataVirtSP[,i] = factor(dataVirtSP[,i], levels=1:4, labels=choices, ordered=TRUE)
}


choices  = c("Much less than before Covid-19",	"Less than before Covid-19",	"Same as before Covid-19",	"More than before Covid-19", "Much more than before Covid-19")
for(i in 5:8) {
  dataVirtSP[,i] = factor(dataVirtSP[,i], levels=1:5, labels=choices, ordered=TRUE)
}

dataVirtSPBD <- subset(dataVirtSP, select= c(1:4))
dataVirtSPA <- subset(dataVirtSP, select= c(5:8))

dataVirtSP_likBD <- likert(dataVirtSPBD)
dataVirtSP_likA <- likert(dataVirtSPA)


plotnew4VBD <- likert(dataVirtSP_likBD,
                   horizontal=TRUE,
                   aspect=0.3, 
                   reverse=FALSE,  xTickLabelsPositive = TRUE,
                   ylab=NULL,
                   main="Use of virtual software in place of flying - Sao Paulo (n=439)",
                   auto.key=list(space="bottom", 
                                 columns=3,
                                 reverse=TRUE, padding.text=1))

plotnew4VA <- likert(dataVirtSP_likA,
                    horizontal=TRUE,
                    aspect=0.3, 
                    reverse=FALSE,  xTickLabelsPositive = TRUE,
                    ylab=NULL,
                    main="Potential use of virtual software in place of flying - Sao Paulo (n=439)",
                    auto.key=list(space="bottom", 
                                  columns=3,
                                  reverse=TRUE, padding.text=1))

plotnew4VA

grid.arrange(plotnew3VBD,plotnew4VBD,
             nrow=2, ncol=1)


grid.arrange(plotnew3VA,plotnew4VA,
             nrow=2, ncol=1)

