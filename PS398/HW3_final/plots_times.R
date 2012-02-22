

times<-read.csv("/Users/cassydorff/PS398/times.csv")
colnames(times)<-c("selSort", "bubbleSort")

plot(times$selSort, type ="l", ylab= "Time in millisec", xlab="List Length", col= "orange", yaxt='n', main= "Sort Time")
lines(times$bubbleSort, col ="purple")
axis(2, las=2, labels=c("a little", "a bit", "a lot"), at = c(0.00,0.040, 0.070))
text(200, .02, labels = "Bubble Sort", col = "purple")
text(500, .008, labels = "Selection Sort", col = "orange")


