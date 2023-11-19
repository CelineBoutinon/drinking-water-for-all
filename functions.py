# check if item in first list is in second list and return list of items in first list not found in second list
def isInList(list_1,list_2):
    list_1_not_in_2 = []
    for x in list_1:
        if x not in list_2:
            list_1_not_in_2.append(x)
    return list_1_not_in_2


# find color reference from a pixel sample from a company logo, to use matching colors on graphs
def findColor(image):
    from PIL import Image
    img = Image.open(image)
    pixels = img.load()
    for y in range(0, 1):
        for x in range(0, 1):
            r, g, b, a = pixels[x, y]
            color = f"#{r:02x}{g:02x}{b:02x}"
            return color
        
# to find eligible keys in dataframe.
# careful: use function only on dataframes with duplicated lines already checked & removed
def isCandKey(df, col):
    if df.shape[0] == len(df[col].unique()):
        print(str(col), "est une clé candidate.")
        return True
    else:
        print(col, "n'est pas une clé candidate.")
        return False       
        
# format seconds into hh:mm:ss        
def formHMS(secs):
    return str(datetime.timedelta(seconds = secs))        
        
# conditional display of labels >2% on pie plots
def my_autopct(pct):
    return ('%1.1f%%' % pct) if pct > 2 else ''   
    
def correlation_graph(pca, 
                      x_y, 
                      features, col) : 
    """Affiche le graphe des correlations

    Positional arguments : 
    -----------------------------------
    pca : sklearn.decomposition.PCA : notre objet PCA qui a été fit
    x_y : list ou tuple : le couple x,y des plans à afficher, exemple [0,1] pour F1, F2
    features : list ou tuple : la liste des features (ie des dimensions) à représenter
    """
    import matplotlib.pyplot as plt
    import numpy as np
    
    # Extrait x et y 
    x,y=x_y

    # Taille de l'image (en inches)
    fig, ax = plt.subplots(figsize=(8,8))

    # Pour chaque composante : 
    for i in range(0, pca.components_.shape[1]):

        # Les flèches
        ax.arrow(0,0, 
                pca.components_[x, i],  
                pca.components_[y, i],  
                head_width=0.02,
                head_length=0.02, 
                width=0.01, color=col)

        # Les labels
        plt.text(pca.components_[x, i] + 0.02,
                pca.components_[y, i] - 0.02,
                features[i], fontsize=8)
        
    
    # plot thicker abscissa and ordinate lines
    plt.axvline(x=0, c='gainsboro', lw=1, linestyle='solid')
    plt.axhline(y=0, c='gainsboro', lw=1, linestyle='solid')

    # Nom des axes, avec le pourcentage d'inertie expliqué
    plt.xlabel('F{} ({}%)'.format(x+1, round(100*pca.explained_variance_ratio_[x],2)))
    plt.ylabel('F{} ({}%)'.format(y+1, round(100*pca.explained_variance_ratio_[y],2)))
    
  
    # Ajout du titre
    plt.title("Cercle des corrélations (F{} et F{})".format(x+1, y+1), fontsize=12)

    # Le cercle 
    an = np.linspace(0, 2 * np.pi, 100)
    plt.plot(np.cos(an), np.sin(an), color='gainsboro', ls='--')  # Add a unit circle for scale

    # Axes et display
    plt.axis('equal')
    plt.grid(axis='both', color='gainsboro', linewidth=0.5)
    plt.show(block=False)    
    
    
    
    
def display_factorial_planes(   X_projected, 
                                x_y, 
                                pca=None, 
                                labels = None,
                                clusters=None, 
                                alpha=1,
                                figsize=[10,8], 
                                marker="." ):
    """
    Affiche la projection des individus

    Positional arguments : 
    -------------------------------------
    X_projected : np.array, pd.DataFrame, list of list : la matrice des points projetés
    x_y : list ou tuple : le couple x,y des plans à afficher, exemple [0,1] pour F1, F2

    Optional arguments : 
    -------------------------------------
    pca : sklearn.decomposition.PCA : un objet PCA qui a été fit, cela nous permettra d'afficher la variance de chaque composante, default = None
    labels : list ou tuple : les labels des individus à projeter, default = None
    clusters : list ou tuple : la liste des clusters auquel appartient chaque individu, default = None
    alpha : float in [0,1] : paramètre de transparence, 0=100% transparent, 1=0% transparent, default = 1
    figsize : list ou tuple : couple width, height qui définit la taille de la figure en inches, default = [10,8] 
    marker : str : le type de marker utilisé pour représenter les individus, points croix etc etc, default = "."
    """
    import matplotlib.pyplot as plt
    import numpy as np
    import seaborn as sns
    
    
    # Transforme X_projected en np.array
    X_ = np.array(X_projected)

    # On définit la forme de la figure si elle n'a pas été donnée
    if not figsize: 
        figsize = (5,5)

    # On gère les labels
    if  labels is None : 
        labels = []
    try : 
        len(labels)
    except Exception as e : 
        raise e

    # On vérifie la variable axis 
    if not len(x_y) ==2 : 
        raise AttributeError("2 axes sont demandées")   
    if max(x_y )>= X_.shape[1] : 
        raise AttributeError("la variable axis n'est pas bonne")   

    # on définit x et y 
    x, y = x_y

    # Initialisation de la figure       
    fig, ax = plt.subplots(1, 1, figsize=figsize)

    # On vérifie s'il y a des clusters ou non
    c = None if clusters is None else clusters
 
    # Les points    
    # plt.scatter(   X_[:, x], X_[:, y], alpha=alpha, 
    #                     c=c, cmap="Set1", marker=marker)
    sns.scatterplot(data=None, x=X_[:, x], y=X_[:, y], hue=c, palette="Set1")

    # Si la variable pca a été fournie, on peut calculer le % de variance de chaque axe 
    if pca : 
        v1 = str(round(100*pca.explained_variance_ratio_[x],2))  + " %"
        v2 = str(round(100*pca.explained_variance_ratio_[y],2))  + " %"
    else : 
        v1=v2= ''

    # Nom des axes, avec le pourcentage d'inertie expliqué
    ax.set_xlabel(f'F{x+1} {v1}', fontsize=12)
    ax.set_ylabel(f'F{y+1} {v2}', fontsize=12)

    # Valeur x max et y max
    x_max = np.abs(X_[:, x]).max() *1.1
    y_max = np.abs(X_[:, y]).max() *1.1

    # On borne x et y 
    ax.set_xlim(left=-x_max, right=x_max)
    ax.set_ylim(bottom= -y_max, top=y_max)

    # plot thicker abscissa and ordinate lines
    plt.axvline(x=0, c='gainsboro', lw=1, linestyle='solid')
    plt.axhline(y=0, c='gainsboro', lw=1, linestyle='solid')
    plt.grid(axis='both', color='gainsboro', linewidth=0.5)

    # Affichage des labels des points
    if len(labels) : 
        for i,(_x,_y) in enumerate(X_[:,[x,y]]):
            plt.text(_x, _y+0.05, labels[i], fontsize='8', ha='center',va='center') 

    # Titre et display
    plt.title(f"Projection des individus (sur F{x+1} et F{y+1})", fontsize=12)
    plt.savefig("clusters&country2.png", bbox_inches='tight')
    plt.show()
