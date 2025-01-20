Readme Du TP multithreading : Achachera - Lestrade
Comparaison des performances : Python vs C++ pour une tâche de taille = 2000

- Temps d'exécution

-- Python (numpy.linalg.solve)

    0.137333491 secondes
    
    0.150069403 secondes
    
    0.158800008 secondes
    
    0.219663992 secondes
    
    0.141271969 secondes

Temps moyen d'exécution : 0.16 secondes

-- C++

1. Méthode ColPivHouseholderQr

    4.27834 secondes
    
    4.53753 secondes
    
    4.74454 secondes
    
    4.40566 secondes
    
    4.43835 secondes

Temps moyen d'exécution : 4.48 secondes

2. Méthode LDLT

    0.704272 secondes
    
    0.748951 secondes
    
    1.015490 secondes
    
    0.826262 secondes
    
    0.708208 secondes

Temps moyen d'exécution : 0.8 secondes

3. Méthode LLT

    0.0141185 secondes
    
    0.0295315 secondes
    
    0.0119103 secondes
    
    0.0121380 secondes
    
    0.0150157 secondes

Temps moyen d'exécution : 0.02 secondes


- Conclusion

La méthode LLT en C++ reste la plus rapide avec un temps moyen de 0.02 secondes, même pour une taille de 2000.

Python (numpy.linalg.solve) est 10 fois plus lent que LLT mais reste plus rapide que la méthode LDLT et beaucoup plus rapide que ColPivHouseholderQr.

La méthode ColPivHouseholderQr en C++ est la plus lente, prenant environ 4.48 secondes en moyenne.

- Analyse :

C++ est globalement plus performant que Python pour la résolution de grands systèmes linéaires.

LLT montre une très bonne scalabilité et reste très rapide même avec des matrices de grande taille.

- Recommandation :

Privilégier LLT en C++ pour des calculs haute performance.

Utiliser Python pour des développements plus rapides ou pour des tâches où la performance n'est pas critique.
