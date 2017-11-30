In this work Junto toolkit has been used.This toolkit  implements Modified Adsorption(MAD) algorithm. 
Prerequisites:
junto-toolkit - https://github.com/parthatalukdar/junto/blob/master/README

To run label propagation in junto the constructed graph needs to be fed. 
To construct the graph of all unlabled word pairs – 

1.	Run the edgeweight_avg_<#seed>.py to create the edgeweights between the word pair nodes. word_all.txt file having all the word pair vectors used in the work. Here we have used word pair of ten –affixes. i.e. –ally, -ism, -ist, -y, -man, -ation, -like, -hood, -ic, -ment. edgeweight_avg_<#seed>.py  takes average of each word pair words and after finding average of all word pair, it calculate the cosine similarity. It also creates the seed_<#seed>.txt file for seed information and avg_edgweight_<#seed>.txt for nodes and their corresponding weights.

2.	Execute gold_label.py file to generate gold_labels for unlabeled nodes. Here the limits of the if else conditions needs to changed as the index of the unlabeled nodes.


3.	Rename the avg_edgweight_<#seed>.txt  file to input_graph and seed_<#seed>.txt file to seeds  and move it to junto-master/examples/simple/data directory.

4.	Move to junto-master/examples/simple and execute junto with the command junto config simple_config 

5.	Output file label_prop_output will be generated in the junto-master/examples/simple/data


