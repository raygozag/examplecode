package org.raygoza.bx.rPrimer;

import org.apache.commons.httpclient.HttpClient;
import org.apache.commons.httpclient.methods.PostMethod;
import org.apache.commons.httpclient.methods.StringRequestEntity;
import org.apache.commons.io.IOUtils;

public class Primer3Interfacer {

	HttpClient client;
	String host ="";
	
	public Primer3Interfacer(String host) {
		client = new HttpClient();
		this.host = host;
	}
	
	
	
	
	public PrimerInfo getLeftPrimerInfo(String seqname,String sequence) throws Exception {
		
		
		PostMethod left = new PostMethod(host);


		StringRequestEntity sre = new StringRequestEntity("PRIMER_MISPRIMING_LIBRARY=NONE&SEQUENCE="+sequence+"&MUST_XLATE_PICK_LEFT=1&PRIMER_LEFT_INPUT=&PRIMER_INTERNAL_OLIGO_INPUT=&PRIMER_RIGHT_INPUT=&Pick+Primers=Pick+Primers&PRIMER_SEQUENCE_ID="+seqname+"&TARGET=&EXCLUDED_REGION=&MUST_XLATE_PRODUCT_MIN_SIZE=100&PRIMER_PRODUCT_OPT_SIZE=200&MUST_XLATE_PRODUCT_MAX_SIZE=1000&PRIMER_NUM_RETURN=5&PRIMER_MAX_END_STABILITY=9.0&PRIMER_MAX_MISPRIMING=12.00&PRIMER_PAIR_MAX_MISPRIMING=24.00&PRIMER_MIN_SIZE=21&PRIMER_OPT_SIZE=23&PRIMER_MAX_SIZE=25&PRIMER_MIN_TM=57.0&PRIMER_OPT_TM=60.0&PRIMER_MAX_TM=63.0&PRIMER_MAX_DIFF_TM=100.0&PRIMER_PRODUCT_MIN_TM=&PRIMER_PRODUCT_OPT_TM=&PRIMER_PRODUCT_MAX_TM=&PRIMER_MIN_GC=20.0&PRIMER_OPT_GC_PERCENT=&PRIMER_MAX_GC=80.0&PRIMER_SELF_ANY=8.00&PRIMER_SELF_END=3.00&PRIMER_NUM_NS_ACCEPTED=0&PRIMER_MAX_POLY_X=5&PRIMER_INSIDE_PENALTY=&PRIMER_OUTSIDE_PENALTY=0&PRIMER_FIRST_BASE_INDEX=1&PRIMER_GC_CLAMP=0&PRIMER_SALT_CONC=50.0&PRIMER_DNA_CONC=50.0&PRIMER_LIBERAL_BASE=1&INCLUDED_REGION=&PRIMER_START_CODON_POSITION=&PRIMER_SEQUENCE_QUALITY=+&PRIMER_MIN_QUALITY=0&PRIMER_MIN_END_QUALITY=0&PRIMER_QUALITY_RANGE_MIN=0&PRIMER_QUALITY_RANGE_MAX=100&PRIMER_WT_TM_LT=1.0&PRIMER_WT_TM_GT=1.0&PRIMER_WT_SIZE_LT=1.0&PRIMER_WT_SIZE_GT=1.0&PRIMER_WT_GC_PERCENT_LT=0.0&PRIMER_WT_GC_PERCENT_GT=0.0&PRIMER_WT_COMPL_ANY=0.0&PRIMER_WT_COMPL_END=0.0&PRIMER_WT_NUM_NS=0.0&PRIMER_WT_REP_SIM=0.0&PRIMER_WT_SEQ_QUAL=0.0&PRIMER_WT_END_QUAL=0.0&PRIMER_WT_POS_PENALTY=0.0&PRIMER_WT_END_STABILITY=0.0&PRIMER_PAIR_WT_PRODUCT_SIZE_LT=0.05&PRIMER_PAIR_WT_PRODUCT_SIZE_GT=0.05&PRIMER_PAIR_WT_PRODUCT_TM_LT=0.0&PRIMER_PAIR_WT_PRODUCT_TM_GT=0.0&PRIMER_PAIR_WT_DIFF_TM=0.0&PRIMER_PAIR_WT_COMPL_ANY=0.0&PRIMER_PAIR_WT_COMPL_END=0.0&PRIMER_PAIR_WT_REP_SIM=0.0&PRIMER_PAIR_WT_PR_PENALTY=1.0&PRIMER_PAIR_WT_IO_PENALTY=0.0&PRIMER_INTERNAL_OLIGO_EXCLUDED_REGION=&PRIMER_INTERNAL_OLIGO_MIN_SIZE=18&PRIMER_INTERNAL_OLIGO_OPT_SIZE=20&PRIMER_INTERNAL_OLIGO_MAX_SIZE=27&PRIMER_INTERNAL_OLIGO_MIN_TM=57.0&PRIMER_INTERNAL_OLIGO_OPT_TM=60.0&PRIMER_INTERNAL_OLIGO_MAX_TM=63.0&PRIMER_INTERNAL_OLIGO_MIN_GC=20.0&PRIMER_INTERNAL_OLIGO_OPT_GC_PERCENT=&PRIMER_INTERNAL_OLIGO_MAX_GC=80.0&PRIMER_INTERNAL_OLIGO_SELF_ANY=12.00&PRIMER_INTERNAL_OLIGO_SELF_END=12.00&PRIMER_INTERNAL_OLIGO_NUM_NS=0&PRIMER_INTERNAL_OLIGO_MAX_POLY_X=5&PRIMER_INTERNAL_OLIGO_MISHYB_LIBRARY=NONE&PRIMER_INTERNAL_OLIGO_MAX_MISHYB=12.00&PRIMER_INTERNAL_OLIGO_MIN_QUALITY=0&PRIMER_INTERNAL_OLIGO_SALT_CONC=50.0&PRIMER_INTERNAL_OLIGO_DNA_CONC=50.0&PRIMER_IO_WT_TM_LT=1.0&PRIMER_IO_WT_TM_GT=1.0&PRIMER_IO_WT_SIZE_LT=1.0&PRIMER_IO_WT_SIZE_GT=1.0&PRIMER_IO_WT_GC_PERCENT_LT=0.0&PRIMER_IO_WT_GC_PERCENT_GT=0.0&PRIMER_IO_WT_COMPL_ANY=0.0&PRIMER_IO_WT_NUM_NS=0.0&PRIMER_IO_WT_REP_SIM=0.0&PRIMER_IO_WT_SEQ_QUAL=0.0");
		left.setRequestEntity(sre);

		client.executeMethod(left);
		
		
		PrimerInfo info = new PrimerInfo(IOUtils.toString(left.getResponseBodyAsStream()));
		
		
		
		return info;
		
	}
	
	
	public PrimerInfo getRightPrimerInfo(String seqname,String sequence) throws Exception {
		
		PostMethod right = new PostMethod("http://biotools.umassmed.edu/bioapps/primer3_www_results.cgi");

		StringRequestEntity rsre = new StringRequestEntity("PRIMER_MISPRIMING_LIBRARY=NONE&SEQUENCE=" +sequence+
				"&MUST_XLATE_PICK_RIGHT=1&PRIMER_LEFT_INPUT=&PRIMER_INTERNAL_OLIGO_INPUT=&PRIMER_RIGHT_INPUT=&Pick+Primers=Pick+Primers&PRIMER_SEQUENCE_ID="+seqname+"&TARGET=&EXCLUDED_REGION=&MUST_XLATE_PRODUCT_MIN_SIZE=100&PRIMER_PRODUCT_OPT_SIZE=230&MUST_XLATE_PRODUCT_MAX_SIZE=" +
				"1000&PRIMER_NUM_RETURN=5&PRIMER_MAX_END_STABILITY=9.0&PRIMER_MAX_MISPRIMING=12.00&PRIMER_PAIR_MAX_MISPRIMING=24.00&PRIMER_MIN_SIZE=21&PRIMER_OPT_SIZE=23&PRIMER_MAX_SIZE=25&PRIMER_MIN_TM=57.0&PRIMER_OPT_TM=60.0&PRIMER_MAX_TM=63.0&PRIMER_MAX_DIFF_TM=100.0&PRIMER_PRODUCT_" +
				"MIN_TM=&PRIMER_PRODUCT_OPT_TM=&PRIMER_PRODUCT_MAX_TM=&PRIMER_MIN_GC=20.0&PRIMER_OPT_GC_PERCENT=&PRIMER_MAX_GC=80.0&PRIMER_SELF_ANY=8.00&PRIMER_SELF_END=3.00&PRIMER_NUM_NS_ACCEPTED=0&PRIMER_MAX_POLY_X=5&PRIMER_INSIDE_PENALTY=&PRIMER_OUTSIDE_PENALTY=0&PRIMER_FIRST_BASE_I" +
				"NDEX=1&PRIMER_GC_CLAMP=0&PRIMER_SALT_CONC=50.0&PRIMER_DNA_CONC=50.0&PRIMER_LIBERAL_BASE=1&INCLUDED_REGION=&PRIMER_START_CODON_POSITION=&PRIMER_SEQUENCE_QUALITY=+&PRIMER_MIN_QUALITY=0&PRIMER_MIN_END_QUALITY=0&PRIMER_QUALITY_RANGE_MIN=0&PRIMER_QUALITY_RANGE_MAX=100&PRIME" +
				"R_WT_TM_LT=1.0&PRIMER_WT_TM_GT=1.0&PRIMER_WT_SIZE_LT=1.0&PRIMER_WT_SIZE_GT=1.0&PRIMER_WT_GC_PERCENT_LT=0.0&PRIMER_WT_GC_PERCENT_GT=0.0&PRIMER_WT_COMPL_ANY=0.0&PRIMER_WT_COMPL_END=0.0&PRIMER_WT_NUM_NS=0.0&PRIMER_WT_REP_SIM=0.0&PRIMER_WT_SEQ_QUAL=0.0&PRIMER_WT_END_QUAL=0" +
				".0&PRIMER_WT_POS_PENALTY=0.0&PRIMER_WT_END_STABILITY=0.0&PRIMER_PAIR_WT_PRODUCT_SIZE_LT=0.05&PRIMER_PAIR_WT_PRODUCT_SIZE_GT=0.05&PRIMER_PAIR_WT_PRODUCT_TM_LT=0.0&PRIMER_PAIR_WT_PRODUCT_TM_GT=0.0&PRIMER_PAIR_WT_DIFF_TM=0.0&PRIMER_PAIR_WT_COMPL_ANY=0.0&PRIMER_PAIR_WT_COM" +
				"PL_END=0.0&PRIMER_PAIR_WT_REP_SIM=0.0&PRIMER_PAIR_WT_PR_PENALTY=1.0&PRIMER_PAIR_WT_IO_PENALTY=0.0&PRIMER_INTERNAL_OLIGO_EXCLUDED_REGION=&PRIMER_INTERNAL_OLIGO_MIN_SIZE=18&PRIMER_INTERNAL_OLIGO_OPT_SIZE=20&PRIMER_INTERNAL_OLIGO_MAX_SIZE=27&PRIMER_INTERNAL_OLIGO_MIN_TM=5" +
				"7.0&PRIMER_INTERNAL_OLIGO_OPT_TM=60.0&PRIMER_INTERNAL_OLIGO_MAX_TM=63.0&PRIMER_INTERNAL_OLIGO_MIN_GC=20.0&PRIMER_INTERNAL_OLIGO_OPT_GC_PERCENT=&PRIMER_INTERNAL_OLIGO_MAX_GC=80.0&PRIMER_INTERNAL_OLIGO_SELF_ANY=12.00&PRIMER_INTERNAL_OLIGO_SELF_END=12.00&PRIMER_INTERNAL_O" +
				"LIGO_NUM_NS=0&PRIMER_INTERNAL_OLIGO_MAX_POLY_X=5&PRIMER_INTERNAL_OLIGO_MISHYB_LIBRARY=NONE&PRIMER_INTERNAL_OLIGO_MAX_MISHYB=12.00&PRIMER_INTERNAL_OLIGO_MIN_QUALITY=0&PRIMER_INTERNAL_OLIGO_SALT_CONC=50.0&PRIMER_INTERNAL_OLIGO_DNA_CONC=50.0&PRIMER_IO_WT_TM_LT=1.0&PRIMER_" +
				"IO_WT_TM_GT=1.0&PRIMER_IO_WT_SIZE_LT=1.0&PRIMER_IO_WT_SIZE_GT=1.0&PRIMER_IO_WT_GC_PERCENT_LT=0.0&PRIMER_IO_WT_GC_PERCENT_GT=0.0&PRIMER_IO_WT_COMPL_ANY=0.0&PRIMER_IO_WT_NUM_NS=0.0&PRIMER_IO_WT_REP_SIM=0.0&PRIMER_IO_WT_SEQ_QUAL=0.0");
		right.setRequestEntity(rsre);
		
		client.executeMethod(right);
		
		
		PrimerInfo info = new PrimerInfo(IOUtils.toString(right.getResponseBodyAsStream()));
		
		
		
		return info;
		
		
	}
	
	
}