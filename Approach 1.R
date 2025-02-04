library(png)
img = readPNG("image2.png")
row = dim(img)[1]
col = dim(img)[2]
for (i in 1:row){
for (j in 1:col){
if (img[i,j,1]>0.25 & img[i,j,1]<0.5 & img[i,j,2]>0.55 & img[i,j,2]<0.75 & img[i,j,3]>0.2 & img[i,j,3]<0.45){
img[i,j,1]=1
img[i,j,2]=1
img[i,j,3]=1
}}}
plot(as.raster(img))
writePNG(img,"imperfect.png")