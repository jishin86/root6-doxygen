// The simplest card for combination

gauss1 = Gaussian(x[0,100],mean1[50,0,100],4);
flat1 = Polynomial(x,0);
sb_model1 = SUM(nsig1[120,0,300]*gauss1 , nbkg1[100,0,1000]*flat1);
gauss2 = Gaussian(x,mean2[80,0,100],5);
flat2 = Polynomial(x,0);
sb_model2 = SUM(nsig2[90,0,400]*gauss2 , nbkg2[80,0,1000]*flat2);
