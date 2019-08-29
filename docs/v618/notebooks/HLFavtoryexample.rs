// The simplest card

gauss = Gaussian(mes[5.20,5.30],mean[5.28,5.2,5.3],width[0.0027,0.001,1]);
argus = ArgusBG(mes,5.291,argpar[-20,-100,-1]);
sum = SUM(nsig[200,0,10000]*gauss,nbkg[800,0,10000]*argus);

