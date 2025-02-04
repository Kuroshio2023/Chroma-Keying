library("png")
img=readPNG("image2.png")
img2=img
plot(as.raster(img))
for (i in 1:dim(img)[1]){
  for (j in 1:dim(img)[2]){
    if (img2[i,j,2]>1.2*img2[i,j,1] & img2[i,j,2]>1.2*img2[i,j,3]  ){
      img2[i,j,1]=1
      img2[i,j,2]=1
      img2[i,j,3]=1
     
    }
  }
}
plot(as.raster(img2))