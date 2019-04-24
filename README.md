# ArbitrageTrading

Using https://docs.openexchangerates.org/docs/ I will get information about current exchange rates. Then based on the current exchange rates I will construct a graph to determine if there are any negative cycles (adaptation of Bellman-Fords algorithm) I will return the negative cycle path which will increase the value of your money if all the trades are done in that sequence.

The plan is to use python and store the graph as an adjacency matrix because it will not be a sparse graph and will have O(1) lookup for prices.

