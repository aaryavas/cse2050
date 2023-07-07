from Graph import Graph
import unittest

class test_Graph(unittest.TestCase):

    # Create a graph `self.g` that you can use in your other unittests. Include ASCII art.

    """

                             2434

        Portland ----------------------------------New York City

        |   \                                               /

        |        \                             745      /

        |             \                             /

        |                  \ 2704                /

    1005|                     \               /

        |                         \       /

        |                            \ /

        |                               \ 

        |                           /        \ 

        |                         /               \ 

        Phoenix ---------------Atlanta------------------Miami

                    1583                    600



    """

    def setUp(self):
        """
        Sets up graph for testing
        """
        self.g = Graph()
        self.g.add_vertex('Portland')
        self.g.add_vertex('New York City')
        self.g.add_vertex('Atlanta')
        self.g.add_vertex('Miami')
        self.g.add_vertex('Phoenix')
        self.g.add_edge('New York City', 'Portland', 2434)
        self.g.add_edge('Portland', 'New York City', 2434)
        self.g.add_edge('New York City', 'Atlanta', 745)
        self.g.add_edge('Atlanta', 'New York City', 745)
        self.g.add_edge('Portland', 'Phoenix', 1005)
        self.g.add_edge('Phoenix', 'Portland', 1005)
        self.g.add_edge('Portland', 'Miami', 2704)
        self.g.add_edge('Miami', 'Portland', 2704)
        self.g.add_edge('Atlanta', 'Miami', 600)
        self.g.add_edge('Miami', 'Atlanta', 600)
        self.g.add_edge('Atlanta', 'Phoenix', 1583)
        self.g.add_edge('Phoenix', 'Atlanta', 1583)



    def test_add_vertex(self):
        """

        Tests add_vertex function

        """
        self.assertIn('Atlanta', self.g.V)

    
    def test_remove_vertex(self):
        """

        Tests remove_vertex function
        """
        self.g.add_vertex('Salt Lake City')
        self.g.remove_vertex('Salt Lake City')
        self.assertNotIn('Salt Lake City', self.g.V)

    
    def test_add_edge(self):
        """
        Tests add_edge function
        """
        self.assertIn(('New York City', 745), self.g.adjacent['Atlanta'])
  
    def test_remove_edge(self):
        """
        Tests remove_edge function
        """
        self.g.add_edge('Atlanta', 'Hartford', 100)
        self.g.remove_edge('Atlanta', 'Hartford', 100)
        self.assertNotIn(('Hartford', 100), self.g.adjacent['Atlanta'])
   
    def test_nbrs(self):
        """

        Tests neighbors

        """
        self.assertEqual(set(self.g.nbrs('Portland')), {('Phoenix', 1005), ('Miami', 2704), ('New York City', 2434)})
    
class test_GraphTraversal(unittest.TestCase):
    # Create a graph `self.g` that you can use in your other unittests. Include ASCII art.
    """

                             2434

        Portland ----------------------------------New York City

        |   \                                               /

        |        \                             745      /

        |             \                             /

        |                  \ 2704                /

    1005|                     \               /

        |                         \       /

        |                            \ /

        |                               \ 

        |                           /        \ 

        |                         /               \ 

        Phoenix ---------------Atlanta------------------Miami

                    1583                    600
    """
    def setUp(self):
        """
        Sets up graph for testing
        """
        self.g = Graph()
        self.g.add_vertex('Portland')
        self.g.add_vertex('New York City')
        self.g.add_vertex('Atlanta')
        self.g.add_vertex('Miami')
        self.g.add_vertex('Phoenix')
        self.g.add_edge('New York City', 'Portland', 2434)
        self.g.add_edge('Portland', 'New York City', 2434)
        self.g.add_edge('New York City', 'Atlanta', 745)
        self.g.add_edge('Atlanta', 'New York City', 745)
        self.g.add_edge('Portland', 'Phoenix', 1005)
        self.g.add_edge('Phoenix', 'Portland', 1005)
        self.g.add_edge('Portland', 'Miami', 2704)
        self.g.add_edge('Miami', 'Portland', 2704)
        self.g.add_edge('Atlanta', 'Miami', 600)
        self.g.add_edge('Miami', 'Atlanta', 600)
        self.g.add_edge('Atlanta', 'Phoenix', 1583)
        self.g.add_edge('Phoenix', 'Atlanta', 1583)
    # TODO: Which alg do you use here, and why?
    # Alg: BFS Algorithim
    # Why: BFS does a good job of finding the fewest flights because it doesn't account for weights, just number of flights
    def test_fewest_flights(self):
        """Tests fewest_flights function"""
        expected = {'Miami': 1, 'New York City': 1, 'Phoenix': 1, 'Portland': 2}
        self.assertEqual(self.g.fewest_flights('Atlanta'), expected)
    # TODO: Which alg do you use here, and why?
    # Alg: Dijkstra's Algorithim
    # Why: Dijkstra's is best for finding the shortest path between two nodes, so it does a good job with edge weights
    def test_shortest_path(self):
        """Tests shortest_path function"""
        self.assertEqual(self.g.shortest_path('Atlanta'), {(('Atlanta', 'Phoenix'), 1583), (('Atlanta', 'New York City'), 745), (('Atlanta', 'Phoenix', 'Portland'), 2588), (('Atlanta', 'Miami'), 600)})
    # TODO: Which alg do you use here, and why?
    # Alg: Prim's Algorithim
    # Why: Prim's is most efficient when finidng the minimum set in comparison to the others
    def test_minimum_salt(self):
        """Tests minimum_salt function"""
        mst = self.g.minimum_salt('Atlanta')
        self.assertEqual(len(mst.V), len(self.g.V))  
        self.assertEqual(len(mst.adjacent), len(self.g.adjacent))  
        self.assertEqual(sum(wt for nbrs in mst.adjacent.values() for _, wt in nbrs), 7866)
        

unittest.main()