from math import exp

from math import tanh

class test:
	def value(self,index,in0,in1,in2):
		self.input0 = (in0 - 0.459987)/0.0509152
		self.input1 = (in1 - 0.188581)/0.0656804
		self.input2 = (in2 - 134.719)/16.5033
		if index==0: return self.neuron0x7f1dd4734020();
		return 0.
	def neuron0x7f1dd40b7e20(self):
		return self.input0
	def neuron0x7f1dd40916e0(self):
		return self.input1
	def neuron0x7f1dd4090c10(self):
		return self.input2
	def neuron0x7f1dd40e3940(self):
		input = -0.175365
		input = input + self.synapse0x7f1dd475afc0()
		input = input + self.synapse0x7f1dd475b000()
		input = input + self.synapse0x7f1dd47535a0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x7f1dd4017700(self):
		input = 0.485643
		input = input + self.synapse0x7f1dd46f5090()
		input = input + self.synapse0x7f1dd47374b0()
		input = input + self.synapse0x7f1dd46ff280()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x7f1dd4035ec0(self):
		input = 1.63907
		input = input + self.synapse0x7f1dd46ff3c0()
		input = input + self.synapse0x7f1dd464f2b0()
		input = input + self.synapse0x7f1dd4664110()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x7f1dd473c740(self):
		input = -0.212857
		input = input + self.synapse0x7f1dd4696100()
		input = input + self.synapse0x7f1dd4696140()
		input = input + self.synapse0x7f1dd46ff9c0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x7f1dd46f9c50(self):
		input = -0.122071
		input = input + self.synapse0x7f1dd40dc420()
		input = input + self.synapse0x7f1dd40dc460()
		input = input + self.synapse0x7f1dd46abbb0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x7f1dd4750cc0(self):
		input = -0.269999
		input = input + self.synapse0x7f1dd4750e50()
		input = input + self.synapse0x7f1dd4767150()
		input = input + self.synapse0x7f1dd4767190()
		input = input + self.synapse0x7f1dd47671d0()
		input = input + self.synapse0x7f1dd4724330()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x7f1dd4255b80(self):
		input = -0.505189
		input = input + self.synapse0x7f1dd4724370()
		input = input + self.synapse0x7f1dd473b6b0()
		input = input + self.synapse0x7f1dd4255d10()
		input = input + self.synapse0x7f1dd4725b60()
		input = input + self.synapse0x7f1dd4725ba0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x7f1dd46ab770(self):
		input = -0.462626
		input = input + self.synapse0x7f1dd473b9b0()
		input = input + self.synapse0x7f1dd46ab990()
		input = input + self.synapse0x7f1dd4771450()
		input = input + self.synapse0x7f1dd4771490()
		input = input + self.synapse0x7f1dd46ad710()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x7f1dd4734020(self):
		input = 2.19619
		input = input + self.synapse0x7f1dd46ad750()
		input = input + self.synapse0x7f1dd46aab60()
		input = input + self.synapse0x7f1dd4734240()
		return (input*1)+0
	def synapse0x7f1dd475afc0(self):
		return (self.neuron0x7f1dd40b7e20()*-0.0649435)
	def synapse0x7f1dd475b000(self):
		return (self.neuron0x7f1dd40916e0()*-0.0255939)
	def synapse0x7f1dd47535a0(self):
		return (self.neuron0x7f1dd4090c10()*0.647241)
	def synapse0x7f1dd46f5090(self):
		return (self.neuron0x7f1dd40b7e20()*-0.71193)
	def synapse0x7f1dd47374b0(self):
		return (self.neuron0x7f1dd40916e0()*0.349661)
	def synapse0x7f1dd46ff280(self):
		return (self.neuron0x7f1dd4090c10()*1.24151)
	def synapse0x7f1dd46ff3c0(self):
		return (self.neuron0x7f1dd40b7e20()*-0.51405)
	def synapse0x7f1dd464f2b0(self):
		return (self.neuron0x7f1dd40916e0()*2.66875)
	def synapse0x7f1dd4664110(self):
		return (self.neuron0x7f1dd4090c10()*-2.63387)
	def synapse0x7f1dd4696100(self):
		return (self.neuron0x7f1dd40b7e20()*-1.21375)
	def synapse0x7f1dd4696140(self):
		return (self.neuron0x7f1dd40916e0()*2.24167)
	def synapse0x7f1dd46ff9c0(self):
		return (self.neuron0x7f1dd4090c10()*-0.317647)
	def synapse0x7f1dd40dc420(self):
		return (self.neuron0x7f1dd40b7e20()*-0.542042)
	def synapse0x7f1dd40dc460(self):
		return (self.neuron0x7f1dd40916e0()*1.765)
	def synapse0x7f1dd46abbb0(self):
		return (self.neuron0x7f1dd4090c10()*-1.03009)
	def synapse0x7f1dd4750e50(self):
		return (self.neuron0x7f1dd40e3940()*-0.649539)
	def synapse0x7f1dd4767150(self):
		return (self.neuron0x7f1dd4017700()*-0.900423)
	def synapse0x7f1dd4767190(self):
		return (self.neuron0x7f1dd4035ec0()*1.03922)
	def synapse0x7f1dd47671d0(self):
		return (self.neuron0x7f1dd473c740()*1.43649)
	def synapse0x7f1dd4724330(self):
		return (self.neuron0x7f1dd46f9c50()*0.916238)
	def synapse0x7f1dd4724370(self):
		return (self.neuron0x7f1dd40e3940()*1.89716)
	def synapse0x7f1dd473b6b0(self):
		return (self.neuron0x7f1dd4017700()*-1.66765)
	def synapse0x7f1dd4255d10(self):
		return (self.neuron0x7f1dd4035ec0()*1.34846)
	def synapse0x7f1dd4725b60(self):
		return (self.neuron0x7f1dd473c740()*1.17666)
	def synapse0x7f1dd4725ba0(self):
		return (self.neuron0x7f1dd46f9c50()*0.205907)
	def synapse0x7f1dd473b9b0(self):
		return (self.neuron0x7f1dd40e3940()*0.0932871)
	def synapse0x7f1dd46ab990(self):
		return (self.neuron0x7f1dd4017700()*0.071432)
	def synapse0x7f1dd4771450(self):
		return (self.neuron0x7f1dd4035ec0()*-0.387419)
	def synapse0x7f1dd4771490(self):
		return (self.neuron0x7f1dd473c740()*-0.563103)
	def synapse0x7f1dd46ad710(self):
		return (self.neuron0x7f1dd46f9c50()*-0.525207)
	def synapse0x7f1dd46ad750(self):
		return (self.neuron0x7f1dd4750cc0()*2.96954)
	def synapse0x7f1dd46aab60(self):
		return (self.neuron0x7f1dd4255b80()*-5.59158)
	def synapse0x7f1dd4734240(self):
		return (self.neuron0x7f1dd46ab770()*0.124324)
