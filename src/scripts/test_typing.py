import time

def typing_effect(string, timeout=0.05):
    for i in string:
        print(i, end="", flush=True)
        time.sleep(timeout)
        
        
typing_effect("Bonjour, ceci est un texte completement aléatoire pour tester ma magnifique fonction typing_effect, qui, comme son nom l'indique, créé un effet de typing")