def eigenDecompose(bed, kinshipFile=None, outFile=None):
	import eigenDecompose	
	return eigenDecompose.eigenDecompose(bed, kinshipFile, outFile)
	
def findRelated(bed, outFile=None, cutoff=0.05, kinshipFile=None):
	import findRelated
	return findRelated.findRelated(bed, outFile, cutoff, kinshipFile)

def calcH2(pheno, prev, eigen, keepArr=None, covar=None, numRemovePCs=10, lowtail=False):
	import calc_h2
	return calc_h2.calc_h2(pheno, prev, eigen, keepArr, covar, numRemovePCs, lowtail)

def probit(bed, pheno, h2, prev, eigen, outFile=None, keepArr=None, covar=None, thresholds=None, nofail=False, 
				numSkipTopPCs=0, mineig=1e-3, hess=False, recenter=True, maxFixedIters=100, epsilon=1e-3, treatFixedAsRandom=False):
	import probit
	return probit.probit(bed, pheno, h2, prev, eigen, outFile, keepArr, covar, thresholds, nofail, 
				numSkipTopPCs, mineig, hess, recenter, maxFixedIters, epsilon, treatFixedAsRandom=treatFixedAsRandom)

def leapGwas(bedSim, bedTest, pheno, h2, outFile=None, eigenFile=None, covar=None):
	import leap_gwas
	return leap_gwas.gwas(bedSim, bedTest, pheno, h2, outFile, eigenFile, covar)

	
	
	