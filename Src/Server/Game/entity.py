"""
    Ce module contient:
        La classe Entity: Element de base present en jeu.
"""

class Entity(object):
    """
        Element de base present en jeu.
        Definit une entite capable d'interragir
        avec le jeu.
    """

    def __init__(self, client):
        self.client = client
