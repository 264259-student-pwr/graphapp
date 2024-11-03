from django.shortcuts import render
from .models import miasta_i_wspolrzedne, polaczenia_miedzy_miastami
import networkx as nx

def create_graph(request):
    # Initialize a NetworkX graph
    graph = nx.Graph()

    # Fetch all cities and add them as nodes with their coordinates
    for city in miasta_i_wspolrzedne.objects.all():
        graph.add_node(city.miasto, pos=(city.longitude, city.latitude))

    # Fetch all connections and add them as bidirectional edges
    for connection in polaczenia_miedzy_miastami.objects.all():
        graph.add_edge(connection.miasto_a, connection.miasto_b, weight=connection.dlugosc_polaczenia)
        graph.add_edge(connection.miasto_b, connection.miasto_a, weight=connection.dlugosc_polaczenia)

    # Render the response (or return the graph as JSON, etc.)
    return render(request, 'graphapp/graph.html', {'graph': graph})
