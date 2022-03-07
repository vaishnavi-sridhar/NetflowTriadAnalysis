# NetflowTriadAnalysis

This project is an add-on to the java based project (https://github.com/vaishnavi-sridhar/FlinkExamples) and is helpful in:
1. Aggregating data from triad output files into json and creating graphs for analysis (triadsaggregator.py)
2. Plotting graphs for 2nd programming assignment objectives (graph.py)
3. Aggregating data for frequent vs rare sites grouped by source IP address (sitefrequencygenerator.py)


Assumptions:
1. Triad file format: 

triads-<4digitdatemmdd>-<4digittod>-<querywindow>-<wateringhole>
  
  Examples:
  
  triads-0303-0000-25-nonwh - Triads O/P file for March 3rd , 12:00 AM for a query window of 25 , triad formation direction: A->B->C
  
  triads-0304-0000-5-wh - Triads O/P file for March 4th , 12:00 AM for a query window of 5 , triad formation direction: A<-B->C(Watering Hole attack)
