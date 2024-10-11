/*
A KBase module: dkishore_contig_filter
This sample module contains one small method that filters contigs.
*/

module dkishore_contig_filter {
    typedef structure {
        string report_name;
        string report_ref;
    } ReportResults;

    /*
        This example function accepts any number of parameters and returns results in a KBaseReport
    */
    funcdef run_dkishore_contig_filter(mapping<string,UnspecifiedObject> params) returns (ReportResults output) authentication required;

};
