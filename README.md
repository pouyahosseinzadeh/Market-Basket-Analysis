# Market-Basket-Analysis in Python
In this project I am going to analyze Market-Basket datasets to find the frequent itemsets and also generate some rules which is a key factor for Market-Basket analysis.

To have an overall overview, first take a quick look at what Market-Basket analysis is and how it is used in real life applications.

Suppose you are in a supermarket and you are thinking of your little baby and buy a diaper. Afterwards, you see beers next to the diapers and pick them up!

Statistics show that(this project is one of them) fathers who buy a diaper, they tend to buy beers afterwards. So, if we put the shelves belonging to beers next to the diaper ones, we push them to buy beers subconsciously.

Now, let's talk about these statistics and analyses to see which products come after each other and learn how to analyze any dataset with a simple lines of code.

In this project I am using two CSV datasets(Italian products) which are described below. First of all we need to consider the customers' transactions and be informed of what products they buy in the supermarket.

To do so, we are given a huge dataset named "transactions" which contains the customers' transaction code with the number of product she/he bought.

The second dataset contains number of columns which are information we are not very interested to most of them. But we need two important ones. First, the product number which we had in "transaction" file and also segment column.

to make it clear I am going to explain what we are going to do with these project. We want to analyze the customer's purchased stuffs and analyze what kind of products they bought and see which of them are more frequent and which item they are tending to buy afterwards.

The difference here is that we want to analyze the segments and not the products. The column "Segmento" in the "segments-description" is our focus.

To sum up, we have two CSV files named "transactions" and "segments-description".

To see how the dataset looks like, check out the Issues.
