print("*********LES CARACTERES UTF-8 NE MARCHENT PAS, EVITEZ-LES (j'adore python.)")

post_title = str(input("Nom du poste (remplacer les espaces par des _): "))
article_title = str(input("Nom de l'article (titre vitrine): "))
author = str(input("Auteur du post: "))

if author == "Loulou-senpai":
    pdp = "loulou-pfp.jpg"
if author == "ZeyaTsu":
    pdp = "zeyatsu.png"
if author == "Your Local Musk":
    pdp = "ysm-pfp.jpg"

contenu = str(input("Contenu (Passer une ligne: <br/> eg: Salut <br/> à tous!): "))

sym = '"'
print(f"Ajouter des images à des endroits précis en éditant le fichier {post_title}.html avec la balise <img id={sym}pic{sym} src={sym}image.ext{sym} />")

with open(f'{post_title}.html', 'a') as fi:
    message = f"""
    <!DOCTYPE html>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <html>
        <head>
            <meta charset="utf-8" />
            <link rel="stylesheet" href="post.css" />
            <link rel="icon" type="image/x-icon" href="openo1logo.png">

            <title>OpenO1 | Blog</title>
        </head>
        
            <header>  
                <div class="head">
                    <a href="https://openo1.github.io/">
                        <img id="logo" src="openo1logo.png" />
                    </a>
                    <h1 id="text">| Blog</h1> 
                </div> 
            </header>
        
            <body>

                <div class="container-head">
                    <img id="pdp" src="{pdp}" />
                    <h1 id="username">{author}</h1>
                </div>

                <div class="post">
                    <h1>{article_title}</h1>
                    <h4>{contenu}</h4>    
                </div>
            
                
            </body>
        
            <footer>         
            </footer>
    </html>"""

    






    fi.write(message)

