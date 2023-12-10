# http://thinkingtkinter.sourceforge.net/languages/france/penser_en_tkinter.html

"""
tt010.py
Dans le programme précédent, les boutons faisaient quelque chose en clickant dessus avec la souris, mais appuyer sur une
touche du clavier ne faisait rien. Dans ce programme, nous voyons comment faire réagir à des évènements du clavier, et
à des évènements de la souris.

D'abord, il faut voir le concept de "input focus", ou simplement "focus".

Si vous connaissez la mythologie grecque (ou si vous avez vu le dessin animé de Disney "Hercules") vous vous souvenez
des Parques. Les Parques sont trois vieilles femmes qui contrôlent les destinées des hommes. Chaque vie humaine est un
fil dans les mains des Parques, et quand elles coupent le fil, la vie se termine.

Ce qui est remarquable à propos des Parques est qu'elles se partagent un oeil entre elles trois. Celle qui avait l'oeil
devait regarder et dire aux deux autres ce qu'elle voyait. Les Parques pouvaient se passer l'oeil, pour se relayer. Et
evidemment, si vous pouvez voler l'oeil, vous avez un atout MAITRE pour négocier avec les Parques.

"Focus" est ce qui permet aux widgets de votre GUI de voir les évènements clavier. C'est pour les widgets de votre GUI,
ce que l'unique oeil était aux Parques.

Seulement un widget à la fois peut avoir le focus, et le widget qui "a le focus" est le widget qui voit, et répond aux
évènements clavier. "Setting focus" sur un widget est le fait de donner le focus au widget.

Dans ce programme, par example, notre GUI a deux boutons: "OK" et "Cancel". Supposons que j'appuie sur la touche RETURN
du clavier. Est-ce que cet appui sur "Return" sera vu (ou envoyé à) par le bouton "OK", indiquant que l'utilisateur a
accepté ce choix ? Ou bien l'évènement "Return" sera vu (ou envoyé à) par le bouton "Cancel", indiquant que
l'utilisateur a annulé l'opération ? Cela dépend, où est le "focus". C'est-à-dire, cela dépend quel bouton "a le focus"
(si l'un des deux l'a).

Comme l'oeil des Parques, qui pouvait être passé d'une Parque à une autre, le focus peut être passé d'un widget du GUI
à un autre. Il y a plusieurs façons de passer, ou déplacer, le focus d'un widget à un autre. Une façon est avec la
souris. Vous pouvez faire "set focus" sur un widget en clickant sur le widget avec le bouton gauche de la souris.
(Au moins, ce modèle, qui est appelé le modèle "click to type", est la manière dont cela fonctionne sur Windows et
Macintosh, et dans Tk et Tkinter. Certains systèmes utilisent une convention "focus follows mouse" dans laquelle le
widget qui est sous la souris a automatiquement le focus, et il n'est pas nécessaire de clicker. Vous pouvez arriver
au même résultat dans Tk en utilsiant la procédure tk_focusFollowsMouse.)

Une autre façon d'avoir le focus est d'utiliser le clavier. Les widgets qui peuvent recevoir le focus sont rangés dans
une liste circulaire (le "traversal order") dans l'ordre de création des widgets. Appuyer sur la touche TAB du clavier
déplace le focus de sa position actuelle (qui peut être nulle part) au prochain widget dans la liste. A la fin de la
liste, le focus se place sur le widget au sommet de la liste. Et appuyer sur SHIFT+TAB déplace le focus en arrière,
plutôt qu'en avant, dans la liste.

Quand un bouton du GUI a le focus, cela est montré par une dotted box (petite boîte) autour du texte du bouton. Voici
comment voir cela. Lancez le programme précédent. Quand le programme démarre, et que le GUI s'affiche, aucun des boutons
n'a le focus, donc vous ne voyez pas la dotted box. maintenant appuyer sur la touche TAB. Vous verrez la dotted box
apparaître autour du bouton gauche, montrant que le focus lui a été donné. Maintenant appuyez sur la touche TAB à
nouveau, et encore une autre fois. Vous verrez comme le focus passe au bouton suivant, et quand il arrive au dernier
bouton, il revient au premier. (Comme le programme affiche seulement deux boutons, l'effet est que le focus passe d'un
bouton à l'autre.)

(0) Dans ce programme, nous voulons que le bouton OK ait le focus dès le début. Donc nous utilisons la méthode
"focus_force()", qui force le focus sur le bouton OK. Quand vous lancez ce programme, vous verrez que le bouton OK a le
focus dès que l'application démarre.

Dans le dernier programme, nos boutons répondaient seulement à un évènement clavier -- appuyer sur la touche TAB -- qui
faisait alterner le focus entre les deux boutons. mais si vous appuyez sur la touche ENTER/RETURN du clavier, rien ne
se passe. C'est parce que nous avons fait un lien entre les clicks de la souris et nos boutons, pas entre les évènements
clavier et nos boutons.

Dans ce programme, nous allons lier les évènements du clavier aux boutons.

(1) (2) Les instructions pour lier les évènements du clavier aux boutons sont simples -- elles ont le même format que
les instructions pour lier les évènements de la souris. La seule différence est que le nom de l'évènement est le nom
d'un évènement clavier (dans ce cas, "<Return>") plutôt qu'un évènement souris.

Nous voulons qu'un appui sur la touche RETURN du clavier et un click gauche du bouton de la souris, aient le même effet
sur le widget, donc nous lions le même gestionnaire d'évènements aux deux types d'évènement.

Ce programme montre que vous pouvez lier plusieurs types d'évènements à un seul widget (comme un bouton). Et vous pouvez
lier plusieurs combinaisons <widget, event> au même gestionnaire d'évènements.

(3) (4) Maintenant que notre button widget répond à différents évènements, nous pouvons montrer comment retrouver cette
information à partir d'un objet évènement. Nous allons passer les objets évènements à une routine (5) "report_event" qui
va (6) afficher notre information à propos de l'évènement obtenu à partir des attributs de l'évènement.

Notez que pour voir ces informations s'afficher sur la console, il vous faut lancer ce programme avec python
(et pas pythonw) à partir d'une console.

Comportement Du Programme

Quand vous lancez ce programme, vous verrez deux boutons. Clicker sur le bouton de gauche, ou appuyer sur la touche
ETURN quand le bouton a le focus du clavier, changera sa couleur. Clicker sur le bouton de droite, ou appuyer sur la
touche RETURN quand le bouton a le focus du clavier, va fermer l'application. Pour n'importe lequel de ces évènements
clavier ou souris, vous devez voir un message s'afficher avec l'heure de l'évènement et sa description.

[Date de dernière mise à jour: 2002-09-26]
"""

"""
tt030.py

Dans ce programme, nous créons notre premier widget, et nous le plaçons dans myContainer1.

(1) Le widget sera un bouton -- c'est-à-dire, il sera une instance de la classe "Button" de Tkinter. L'instruction :

		button1 = Button(myContainer1)

crée le bouton, lui donne le nom "button1", et l'associe avec son parent, l'objet container appelé myContainer1.

(2)(3) Les widgets possèdent de nombreux attributs, qui sont rangés dans le local namespace dictionary. Les Button
widgets ont des attributs pour contrôler leur taille, leur couleurs d'arrière-plan et d'avant-plan, le texte qu'ils
affichent, l'apparence de leur bord, et ainsi de suite. Dans cet exemple, nous allons juste positionner deux des
attributs de button1 : la couleur d'arrière-plan et le texte. Nous faisons cela en donnant les valeurs dans le
dictionnaire du bouton avec les clés "text" et "background".

		button1["text"]= "Bonjour, Monde !"
		button1["background"] = "green"

(4) Et bien sur, nous insérons (ce qui se fait avec le verbe pack) button1.

		button1.pack()

Quelques Termes Techniques

Quelques fois la relation entre un container et le widget qu'il contient est décrite comme une relation "parent/enfant"
, d'autres fois comme une relation "maitre/esclave".

Comportement Du Programme

Quand vous lancez ce programme, vous verrez que Container1 contient maintenant un bouton vert avec le texte "Bonjour,
Monde !". Quand vous clickez dessus, il ne se passe rien, car nous n 'avons pas encore indiqué ce qui doit se passer
quand ce bouton est clické. (Nous ferons cela plus tard.)

Pour l'instant, il faut fermer la fenêtre, comme précédemmment, en clickant sur l'icône CLOSE de la barre de titre.

Notez comme myContainer1 s'est étiré pour accueillir button1.
"""
# from tkinter import * ### (1)
#
# root = Tk()
#
# myContainer1 = Frame(root)  ### (1)
# myContainer1.pack()         ### (2)
#
# button1 = Button(myContainer1)
#
# button1 = Button(root,
#                  text="Bonjour, Monde !",
#                  background="green")
#
# button1.pack()
#
# root.mainloop()


# Meme programme que ci-dessus, mais en OOP
# import tkinter as tk
# from tkinter import *
#
#
# class MyApp(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.myContainer1 = Frame()
#         self.myContainer1.pack()
#
#         self.button1 = Button(self.myContainer1,
#                               text='OK',
#                               background="green")
#         self.button1.pack(side=LEFT)
#         self.button1.bind("<Button-1>", self.button1Click)
#
#         self.button2 = Button(self.myContainer1,
#                               text='Cancel',
#                               background="red")
#         self.button2.pack(side=RIGHT)
#         self.button2.bind("<Button-1>", self.button2Click)
#
#     def button1Click(self, event):
#         if self.button1["background"] == "green":
#             self.button1["background"] = "yellow"
#         else:
#             self.button1["background"] = "green"
#
#     def button2Click(self, event):
#         self.destroy()
#
#
# if __name__ == "__main__":
#     myapp = MyApp()
#     myapp.mainloop()


"""
tt070.py
Dans le programme précédent, les boutons faisaient quelque chose en clickant dessus avec la souris, mais appuyer sur une
 touche du clavier ne faisait rien. Dans ce programme, nous voyons comment faire réagir à des évènements du clavier, et 
 à des évènements de la souris.

D'abord, il faut voir le concept de "input focus", ou simplement "focus".

Si vous connaissez la mythologie grecque (ou si vous avez vu le dessin animé de Disney "Hercules") vous vous souvenez 
des Parques. Les Parques sont trois vieilles femmes qui contrôlent les destinées des hommes. Chaque vie humaine est un 
fil dans les mains des Parques, et quand elles coupent le fil, la vie se termine.

Ce qui est remarquable à propos des Parques est qu'elles se partagent un oeil entre elles trois. Celle qui avait l'oeil 
devait regarder et dire aux deux autres ce qu'elle voyait. Les Parques pouvaient se passer l'oeil, pour se relayer. Et 
evidemment, si vous pouvez voler l'oeil, vous avez un atout MAITRE pour négocier avec les Parques.

"Focus" est ce qui permet aux widgets de votre GUI de voir les évènements clavier. C'est pour les widgets de votre GUI, 
ce que l'unique oeil était aux Parques.

Seulement un widget à la fois peut avoir le focus, et le widget qui "a le focus" est le widget qui voit, et répond aux 
évènements clavier. "Setting focus" sur un widget est le fait de donner le focus au widget.

Dans ce programme, par example, notre GUI a deux boutons: "OK" et "Cancel". Supposons que j'appuie sur la touche RETURN 
du clavier. Est-ce que cet appui sur "Return" sera vu (ou envoyé à) par le bouton "OK", indiquant que l'utilisateur a 
accepté ce choix ? Ou bien l'évènement "Return" sera vu (ou envoyé à) par le bouton "Cancel", indiquant que 
l'utilisateur a annulé l'opération ? Cela dépend, où est le "focus". C'est-à-dire, cela dépend quel bouton "a le focus" 
(si l'un des deux l'a).

Comme l'oeil des Parques, qui pouvait être passé d'une Parque à une autre, le focus peut être passé d'un widget du GUI à
 un autre. Il y a plusieurs façons de passer, ou déplacer, le focus d'un widget à un autre. Une façon est avec la 
 souris. Vous pouvez faire "set focus" sur un widget en clickant sur le widget avec le bouton gauche de la souris. 
 (Au moins, ce modèle, qui est appelé le modèle "click to type", est la manière dont cela fonctionne sur Windows et 
 Macintosh, et dans Tk et Tkinter. Certains systèmes utilisent une convention "focus follows mouse" dans laquelle le 
 widget qui est sous la souris a automatiquement le focus, et il n'est pas nécessaire de clicker. Vous pouvez arriver au
  même résultat dans Tk en utilsiant la procédure tk_focusFollowsMouse.)

Une autre façon d'avoir le focus est d'utiliser le clavier. Les widgets qui peuvent recevoir le focus sont rangés dans 
une liste circulaire (le "traversal order") dans l'ordre de création des widgets. Appuyer sur la touche TAB du clavier 
déplace le focus de sa position actuelle (qui peut être nulle part) au prochain widget dans la liste. A la fin de la 
liste, le focus se place sur le widget au sommet de la liste. Et appuyer sur SHIFT+TAB déplace le focus en arrière, 
plutôt qu'en avant, dans la liste.

Quand un bouton du GUI a le focus, cela est montré par une dotted box (petite boîte) autour du texte du bouton. Voici 
comment voir cela. Lancez le programme précédent. Quand le programme démarre, et que le GUI s'affiche, aucun des boutons
 n'a le focus, donc vous ne voyez pas la dotted box. maintenant appuyer sur la touche TAB. Vous verrez la dotted box 
 apparaître autour du bouton gauche, montrant que le focus lui a été donné. Maintenant appuyez sur la touche TAB à nouveau, et encore une autre fois. Vous verrez comme le focus passe au bouton suivant, et quand il arrive au dernier bouton, il revient au premier. (Comme le programme affiche seulement deux boutons, l'effet est que le focus passe d'un bouton à l'autre.)

(0) Dans ce programme, nous voulons que le bouton OK ait le focus dès le début. Donc nous utilisons la méthode 
"focus_force()", qui force le focus sur le bouton OK. Quand vous lancez ce programme, vous verrez que le bouton OK a le 
focus dès que l'application démarre.

Dans le dernier programme, nos boutons répondaient seulement à un évènement clavier -- appuyer sur la touche TAB -- qui 
faisait alterner le focus entre les deux boutons. mais si vous appuyez sur la touche ENTER/RETURN du clavier, rien ne se
 passe. C'est parce que nous avons fait un lien entre les clicks de la souris et nos boutons, pas entre les évènements 
 clavier et nos boutons.

Dans ce programme, nous allons lier les évènements du clavier aux boutons.

(1) (2) Les instructions pour lier les évènements du clavier aux boutons sont simples -- elles ont le même format que 
les instructions pour lier les évènements de la souris. La seule différence est que le nom de l'évènement est le nom 
d'un évènement clavier (dans ce cas, "<Return>") plutôt qu'un évènement souris.

Nous voulons qu'un appui sur la touche RETURN du clavier et un click gauche du bouton de la souris, aient le même effet 
sur le widget, donc nous lions le même gestionnaire d'évènements aux deux types d'évènement.

Ce programme montre que vous pouvez lier plusieurs types d'évènements à un seul widget (comme un bouton). Et vous pouvez
 lier plusieurs combinaisons <widget, event> au même gestionnaire d'évènements.

(3) (4) Maintenant que notre button widget répond à différents évènements, nous pouvons montrer comment retrouver cette 
information à partir d'un objet évènement. Nous allons passer les objets évènements à une routine (5) "report_event" qui
 va (6) afficher notre information à propos de l'évènement obtenu à partir des attributs de l'évènement.

Notez que pour voir ces informations s'afficher sur la console, il vous faut lancer ce programme avec python (et pas 
pythonw) à partir d'une console.

Comportement Du Programme

Quand vous lancez ce programme, vous verrez deux boutons. Clicker sur le bouton de gauche, ou appuyer sur la touche 
RETURN quand le bouton a le focus du clavier, changera sa couleur. Clicker sur le bouton de droite, ou appuyer sur la 
touche RETURN quand le bouton a le focus du clavier, va fermer l'application. Pour n'importe lequel de ces évènements 
clavier ou souris, vous devez voir un message s'afficher avec l'heure de l'évènement et sa description. 
"""

# import tkinter as tk
# from tkinter import *
#
#
# class MyApp(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.myContainer1 = Frame()
#         self.myContainer1.pack()
#
#         self.button1 = Button(self.myContainer1)
#         self.button1.configure(text="OK",
#                                background="green")
#         self.button1.pack(side=LEFT)
#         self.button1.focus_force()
#         self.button1.bind("<Button-1>", self.button1Click)
#         self.button1.bind("<Return>", self.button1Click)
#
#         self.button2 = Button(self.myContainer1)
#         self.button2.configure(text="Cancel",
#                                background="red")
#         self.button2.pack(side=RIGHT)
#         self.button2.bind("<Button-1>", self.button2Click)
#         self.button2.bind("<Return>", self.button2Click)
#
#     def button1Click(self, event):
#         report_event(event)
#         if self.button1["background"] == "green":
#             self.button1["background"] = "yellow"
#         else:
#             self.button1["background"] = "green"
#
#     def button2Click(self, event):
#         report_event(event)
#         self.destroy()
#
#
# def report_event(event):
#     """
#     Affiche une description de l'evenement, base sur ses attributs.
#     """
#     event_name = {"2": "KeyPress", "4": "ButtonPress"}
#     print("Time:", str(event.time))
#     print("EvenType" + str(event.type), event_name[str(event.type)],
#           "EventWidgetId=" + str(event.widget),
#           "EventKeySymbol=" + str(event.keysym))
#
#
# if __name__ == "__main__":
#     myapp = MyApp()
#     myapp.mainloop()

"""
tt074.py
Dans un programme précédent, nous avons introduit l'"event binding". Il y a une autre façon de lier un event_handler à 
un widget. C'est le "command binding" et nous allons voir cela dans ce programme.
Command Binding

Vous vous souvenez que dans nos programmes précédents, nous avons lié l'évènement de la souris "<Button-1>" à notre 
bouton widget. "Button" est un autre nom pour l'évènement souris "ButtonPress". Et un évènement souris "ButtonPress" est 
différent d'un évènement souris "ButtonRelease". L'évènement "ButtonPress" est le fait d'appuyer sur le bouton de la 
souris, MAIS DE NE PAS le RELACHER. L'évènement "ButtonRelease" est le fait de relâcher le bouton de la souris.

Il nous faut distinguer un ButtonPress de la souris d'un ButtonRelease, afin de supporter des fonctionnalités comme le 
"drag and drop (glisser et déposer)", dans lequel nous faisons un ButtonPress sur un GUI component, glissons le 
component quelque part, et puis le "drop (déposer)" dans son nouvel emplacement en relâchant le bouton de la souris.

Mais les button widgets ne sont pas le genre de chose qui peuvent être glissés et déposés. Si un utilisateur pense 
qu'il peut faire un drag and drop d'un bouton, il pourrait faire un ButtonPress sur le button widget, puis un drag du 
pointeur de la souris à un autre endroit de l'écran, puis relâcher le bouton de la souris. Ce n'est pas le type 
d'activité que nous voulons reconnaître comme un "push" (ou -- terme technique -- "invocation") du button widget. 
Pour considérer qu'un button widget a été appuyé, l'utilisateur doit avoir fait un ButtonPress sur le widget, et ensuite
 -- SANS déplacer le pointeur de la souris du widget -- faire un ButtonRelease. *CELA* est ce que nous appelons un 
 button press.

C'est une notion plus compliquée de button invocation que dans nos précédents programmes, quand nous lions simplement un
 évènement "Button-1" au button widget avec l'event binding.

Heureusement, il existe une autre forme de binding qui supporte cette notion plus compliquée de widget invocation. On 
appelle cela "command binding" parce que cela utilise l'option "command" du widget.

Dans ce programme, regardez les lignes avec les commentaires (1) et (2) pour voir comment est fait le command binding. 
Dans ces lignes, nous utilisons l'option "command" pour lier button1 au gestionnaire d'évènement "self.button1Click", et
 lier button2 au gestionnaire d'évènement "self.button2Click".

(3) (4)

Regardez la définition des gestionnaires d'évènements. Notez que -- contrairement aux gestionnaires d'évènements dans le
 programme précédent -- ils n'attendent PAS un objet évènement en tant que paramètre. C'est parce que le command 
 binding, contrairement à l'event binding, ne passe PAS automatiquement un objet évènement en tant que paramètre. Et 
 évidemment, cela est sensé. Un command binding ne lie pas un simple évènement à un gestionnaire. Il lie plusieurs 
 évènements à un gestionnaire. Pour un Button widget, par exemple, il lie un motif de ButtonPress suivi d'un 
 ButtonRelease à un gestionnaire. S'il doit passer un évènement au gestionnaire d'évènement, cela sera lequel : 
 ButtonPress ou ButtonRelease? Aucun ne serait complètement correct. C'est pour cette raison, que le command binding, 
 contrairement à l'event binding, ne passe pas un objet évènement.

Nous verrons plus en détail cette différence dans le programme suivant, mais pour l'instant, lançons le programme.

Comportement Du Programme

Quand vous lancez ce programme, les boutons que vous voyez sont exactement comme dans le programme précédent...mais ils 
se comportent différemment.

Comparez leur comportement quand vous faites un ButtonPress avec la souris sur l'un des boutons. Par exemple, déplacez 
le pointeur de la souris jusqu'à ce qu'il soit positionné au-dessus du button widget "OK", puis appuyez sur le click 
gauche de la souris, MAIS NE LE RELACHEZ PAS.

Si vous faites cela dans l'exemple précédent, le gestionnaire the button1Click sera immédiatement exécuté et un message 
s'affichera. Mais si vous faites cela dans ce programme, rien ne se passera... JUSQU'A CE QUE LE BOUTON DE LA SOURIS 
SOIT RELACHE. A ce moment-là, vous verrez s'afficher un message.

Il y a une autre différence. Comparez leur comportement quand vous appuyez sur la barre d'espace et sur la touche 
RETURN. Par exemple, utilisez la touche TAB pour mettre le focus sur le bouton "OK", puis appuyez sur la barre d'espace 
ou la touche RETURN.

Dans le programme précédent (dans lequel nous avons lié le bouton "OK" à un appui sur la touche "Return"), appuyer sur 
la barre d'espace était sans effet, mais appuyer sur la touche RETURN changeait la couleur du bouton. Dans ce programme, 
le comportement est inversé -- appuyer sur la barre d'espace change la couleur du bouton, mais appuyer sur la touche 
RETURN est sans effet.

Nous verrons ces comportements dans le programme suivant. 
"""
# import tkinter as tk
# from tkinter import *
#
#
# class MyApp(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.mycontainer1 = Frame()
#         self.mycontainer1.pack()
#
#         self.button1 = Button(self.mycontainer1, command=self.button1Click)
#         self.button1.configure(text="OK",
#                                background="green")
#         self.button1.pack(side=LEFT)
#         self.button1.focus_force()
#
#         self.button2 = Button(self.mycontainer1, command=self.button2Click)
#         self.button2.configure(text="Cancel", background="red")
#         self.button2.pack(side=RIGHT)
#
#     def button1Click(self):
#         print("button1Click event handler")
#
#         if self.button1["background"] == "green":
#             self.button1["background"] = "yellow"
#         else:
#             self.button1["background"] = "green"
#
#     def button2Click(self):
#         print("button2Click event handler")
#         self.destroy()
#
#
# if __name__ == "__main__":
#     myapp = MyApp()
#     myapp.mainloop()

"""
tt075.py
Dans le programme précédent, nous avons introduit le "command binding" et mis en évidence quelques différences entre 
l'event binding et le command binding. Dans ce programme, nous verrons plus en détail ces différences.

A quels évènements "command" est lié ?

Dans le programme précédent, si vous utilisez la touche TAB pour mettre le focus sur le bouton "OK", appuyer sur la 
barre d'espace change la couleur du bouton, mais appuyer sur la touche RETURN est sans effet.

La raison est que l'option "command" pour un Button widget fournit la conscience des évènements clavier comme des 
évènements de la souris. L'évènement clavier qu'il écoute est un appui de la barre d'espace, pas de la touche RETURN. 
Donc, avec le command binding, appuyer sur la barre d'espace changera la couleur du bouton OK, mais appuyer sur la 
touche RETURN sera sans effet.

Ce comportement me semble (à moi, avec mon passé Windows) inhabituel. Donc la morale ici est que si vous utilisez le 
command binding, il faut comprendre exactement à quoi vous vous liez. C'est une bonne idée de savoir quels évènements 
clavier et souris déclenchent la commande invoquée.

Hélas, la seule source fiable d'informations est le code source de Tk lui-même. Pour une information plus accessible, 
vous pouvez consulter des livres sur Tk (le livre de Brent Welch "Practical Programming in Tcl and Tk" est très bon) ou 
à propos de Tkinter. La documentation Tk documentation est inégale, mais disponible en ligne. Pour la version 8.4 de 
Tcl, la documentation en ligne est disponible à :

      http://www.tcl.tk/man/tcl8.4/TkCmd/contents.htm

Vous devez savoir que tous les widgets ne fournissent pas une option "command". La plupart des Button widgets 
(RadioButton, CheckButton, etc.) la fournissent. Et d'autres proposent des options similaires 
(par exemple scrollcommand). Mais il vous faudra vraiment étudier chaque type de widget pour trouver si il supporte le 
command binding. Mais apprenez par tous les moyens les options de "command" pour les widgets que vous utiliserez. Cela 
améliorera le comportement de votre GUI, et vous simplifiera la vie.

Utiliser ensemble l'Event Binding et le Command Binding

Nous avons noté dans notre dernier programme, que le command binding, contrairement à l'event binding, ne passe pas 
automatiquement un objet évènement en tant que paramètre. Cela peut vous compliquer la vie si vous voulez lier un 
gestionnaire d'évènement à un widget en utilisant *à la fois* l'event binding *et* le command binding.

Par exemple, dans ce programme, nous voulons que nos boutons répondent à un appui sur la touche RETURN tout comme sur la
 barre d'espace. Pour y arriver, nous allons utiliser l'event binding avec l'évènement clavier <Return>, comme nous 
 avons fait dans un programme précédent. (1)

Le problème est que le command binding ne va pas passer un objet évènement en tant que paramètre, alors que l'event 
binding le fera. Donc, devons-nous écrire notre gestionnaire d'évènement ?

Il y a plusieurs solutions à ce problème, mais la plus simple est d'écrire deux gestionnaires d'évènements. Le 
"véritable" gestionnaire d'évènement (2) sera celui utilisé par le binding "command" et il n'attendra pas un objet 
évènement.

L'autre gestionnaire d'évènement (3) sera juste un wrapper pour le véritable gestionnaire d'évènement. Ce wrapper 
attendra le paramètre objet évènement , mais l'ignorera et appelera le véritable gestionnaire d'évènement sans 
paramètre. Nous donnerons au wrapper le même nom que le véritable gestionnaire d'évènement mais avec en plus un suffixe 
"_a".

Comportement Du Programme

Si vous lancez ce programme, son comportement sera le même que le programme précédent, avec cette différence que 
maintenant les boutons vont répondre à un appui sur la touche RETURN comme sur la barre d'espace. 
"""
# from tkinter import *
# import tkinter as tk
#
#
# class MyApp(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.myContainer1 = Frame()
#         self.myContainer1.pack()
#
#         self.button1 = Button(self.myContainer1, command=self.button1Click)
#         self.button1.bind("<Return>", self.button1Click_a)
#         self.button1.configure(text="OK", background="green")
#         self.button1.pack(side=LEFT)
#         self.button1.focus_force()
#
#         self.button2 = Button(self.myContainer1, command=self.button2Click)
#         self.button2.bind("<Return>", self.button2Click_a)
#         self.button2.configure(text="Cancel", background="red")
#         self.button2.pack(side=RIGHT)
#
#     def button1Click(self):
#         print("button1Click event handler")
#
#         if self.button1["background"] == "green":
#             self.button1["background"] = "yellow"
#         else:
#             self.button1["background"] = "green"
#
#     def button2Click(self):
#         print("button2Click event hanlder")
#         self.destroy()
#
#     def button1Click_a(self, event):
#         print("button1Click_a event handler (a wrapper)")
#         self.button1Click()
#
#     def button2Click_a(self, event):
#         print("button2Click_a event handler (a wrapper)")
#         self.button2Click()
#
#
# if __name__ == "__main__":
#     myapp = MyApp()
#     myapp.mainloop()

"""
tt076.py
Dans les derniers programmes, nous avons vu des façons de travailler avec des gestionnaires d'évènement.

Dans ce programme, nous voyons comment partager de l'information entre des gestionnaires d'évènement.

Partager De L'Information Entre Des Fonctions De Gestionnaire D'Evènement

Il y a différents cas dans lesquels vous voulez qu'un gestionnaire d'évènement accomplisse une tâche, puis partage les 
résultats de cette tâche avec les autres gestionnaires d'évènements de ce programme.

Un cas fréquent est une application avec deux jeux de widgets. Un jeu de widgets met en place, ou choisit des 
informations, et l'autre fait quelque chose avec cette information.

Par exemple, vous pouvez avoir un widget qui permet à un utilisateur de choisir un fichier dans une liste, et un autre 
jeu de widgets qui propose différentes opérations sur le fichier sélectionné -- ouvrir le fichier, le détruire, le 
copier, le renommer, et ainsi de suite.

Ou vous pouvez avoir un jeu de widgets qui définit des options de configuration pour votre application, ou un autre jeu 
(des boutons avec les options SAVE et CANCEL, peut-être) qui soit enregistrent ces valeurs sur disque, ou sort sans les 
enregistrer.

Ou bien vous pouvez avoir un jeu de widgets qui définit des paramètres pour un programme que vous voulez lancer, et un 
autre widget (sans doute un bouton avec un nom comme RUN ou EXECUTE) qui lance le programme avec ces paramètres.

Ou vous pouvez avoir besoin d'une invocation d'une fonction de gestionnaire d'évènement pour passer de l'information à 
un appel ultérieur de la même fonction. Considérez un gestionnaire d'évènement qui fait alterner une variable entre deux 
différentes valeurs. Pour assigner une nouvelle valeur à cette variable, il a besoin de savoir quelle valeur avait cette 
variable lors de la dernière exécution de la fontion

Le Problème

Le problème ici est que le gestionnaire d'évènement est une fonction séparée. Chaque gestionnaire d'évènement a ses 
propres variables locales qu'il ne partage pas avec les autres fonctions des gestionnaires d'évènements, ou même avec 
des futurs appels de cette fonction. Donc le problème est -- comment une fonction de gestionnaire d'évènement peut 
partager des données avec d'autres fonctions de gestionnaire d'évènement, si il ne peut pas partager ses variables 
locales entre les fonctions ?

La solution, évidemment, est que les variables à partager ne peuvent être locales aux fonctions de gestionnaire 
d'évènement. Elles doivent être stockées *en dehors* des fonctions de gestionnaire d'évènement.

Solution 1 -- Utiliser Des Variables Globales

Une technique pour faire cela est de les (les variables que vous voulez partager) rendre globales. Par exemple, dans 
chaque gestionnaire d'évènement qui a besoin de changer ou voir myVariable1 et myVariable2, vous pouvez mettre 
l'instruction :

		global myVariable1, myVariable2

Mais l'utilisation de variables globales est potentiellement dangereuse, et est généralement désapprouvé en tant que 
programmation baclée.

Solution 2 -- Utilisez Des Variables D'Instance

Une technique bien plus propre est d'utiliser des "variables d'instance" (c'est à dire, des variables "self.") pour 
détenir cette information que vous voulez partager entre les gestionnaires d'évènements. Pour faire cela, évidemment, 
votre application doit être implémentée en tant que classe, et pas simplement en tant que in-line code.

Cela est une des raisons pour lesquelles (plus tôt dans ces séries) nous avons mis notre application dans une classe. 
Comme nous avons fait cela plus tôt, maintenant notre application a déjà une structure qui nous permet d'utiliser des 
variables d'instance.

Dans ce programme, nous allons mémoriser et partager une information très simple : le nom du dernier bouton appelé. 
Nous le stockerons dans une variable d'instance appelée "self.myLastButtonInvoked". [voyez ### 1 commentaire]

Et pour montrer que nous mémorisons cette information, quand un gestionnaire de bouton est appelé, il affichera cette 
information. [voyez ### 2 commentaires]

Comportement Du Programme

Ce programme affiche trois boutons. Quand vous lancez ce programme, si vous clickez sur n'importe quel bouton, il 
affichera son nom, et le nom du précédent bouton clické.

Notez qu'aucun de ces boutons ne fermera l'application, donc quand vous voulez le faire, vous devez utiliser le widget 
CLOSE (l'icône avec un "X" dans la boîte, en haut à droite de la barre de titre). 
"""
# from tkinter import *
# import tkinter as tk
#
#
# class MyApp(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         # 1 -- Au debut, nous n'avons pas encore appele de gestionnaire de bouton.
#         self.myLastButtonInvoked = None
#
#         self.myContainer1 = Frame()
#         self.myContainer1.pack()
#
#         self.yellowButton = Button(self.myContainer1, command=self.yellowButtonClick)
#         self.yellowButton.configure(text="JAUNE", background="yellow")
#         self.yellowButton.pack(side=LEFT)
#
#         self.redButton = Button(self.myContainer1, command=self.redButtonClick)
#         self.redButton.configure(text="ROUGE", background="red")
#         self.redButton.pack(side=LEFT)
#
#         self.whiteButton = Button(self.myContainer1, command=self.whiteButtonClick)
#         self.whiteButton.configure(text="BLANC", background="white")
#         self.whiteButton.pack(side=LEFT)
#
#     def redButtonClick(self):
#         print("bouton ROUGE clicke. Le precedent bouton clicke etait", self.myLastButtonInvoked)
#         self.myLastButtonInvoked = "RED"
#
#     def yellowButtonClick(self):
#         print("bouton JAUNE clicke. Le precedent bouton clicke etait", self.myLastButtonInvoked)
#         self.myLastButtonInvoked = "YELLOW"
#
#     def whiteButtonClick(self):
#         print("bouton BLANC clicke. Le precedent bouton clicke etait", self.myLastButtonInvoked)
#         self.myLastButtonInvoked = "WHITE"
#
#
# if __name__ == "__main__":
#     print("\n" * 100)  # une facon simple de nettoyer l'ecran
#     print("Demarrage...")
#     myapp = MyApp()
#     myapp.mainloop()
#     print("...Done!")

"""
tt077.py
Dans ce programme nous voyons quelques ...
Fonctionnalités Avancées Du Command Binding
Dans le programme tt075.py, nous avons utilisé l'option "command" pour lier un gestionnaire d'évènement à un widget. 

Par exemple, dans ce programme, l'instruction
    self.button1 = Button(self.myContainer1, command=self.button1Click)
lie la fonction button1Click au widget button1.

Et nous avons utilisé l'event binding pour lier nos boutons à l'évènement clavier <Return>.
    self.button1.bind("", self.button1Click_a)
Dans notre programme précédent, les gestionnaires d'évènements pour les deux boutons faisaient des choses différentes.

Mais supposons un cas différent. Supposons, nous avons plusieurs boutons, qui doivent tous déclencher le *même* type 
d'action. La meilleure manière de faire dans ce cas est de lier tous les évènements pour tous les boutons à un seul 
gestionnaire d'évènement. Chaque bouton va appeler la même handler routine, mais lui passer différents paramètres lui 
indiquant quoi faire.

C'est ce que nous faisons dans ce programme.

Command Binding

Dans ce programme, comme vous pouvez le voir, nous avons deux boutons, et nous utilisons l'option "command" pour les 
lier tous les deux au même gestionnaire d'évènement, la routine -- "buttonHandler". Nous passons trois paramètres à la 
routine buttonHandler : le nom du bouton (dans la variabe button_name), un nombre, et une chaîne de caractères.

    self.button1 = Button(self.myContainer1,
    	command=self.buttonHandler(button_name, 1, "Bien !")
    	)

Dans un programme plus sérieux, la routine buttonHandler routine ferait évidemment un travail, mais dans ce programme, 
il affiche simplement les paramètres qu'il reçoit.

Event Binding

Nous avons vu le command binding. Et pour l'event binding?

Vous remarquerez que nous avons mis en commentaire les deux lignes qui font l'event binding sur l'évènement <Return>.

  # self.button1.bind("", self.buttonHandler_a(event, button_name, 1, "Bien !"))

Ceci est le premier signe d'un problème. L'Event binding passe automatiquement un paramètre event -- mais il n'y a pas 
de manière d'inclure un paramètre event dans notre liste de paramètres.

Nous reviendrons sur ce problème plus tard. Pour l'instant, lançons le programme et voyons ce qui se passe.

Comportement Du Programme

Quand vous regardez le code, ce programme semble raisonnable. Mais quand vous le lancez, vous verrez qu'il ne fonctionne
 pas correctement. La routine buttonHandler est appelée avant que le GUI ne s'affiche. En fait, elle est appelée DEUX 
 fois !

Et si vous faîtes un click gauche de la souris sur n'importe lequel des boutons, vous verrez que rien ne se passe -- la 
routine "eventHandler" n'est *pas* appelée.

Notez que la seule façon de fermer ce programme est de clicker sur l'icône "close" (le X "X" dans la boîte) en haut à 
droite de la barre de titre.

Donc lanceez le programme maintenant, et voyez ce qui se passe. Puis, dans notre programme, nous verrons pourquoi cela 
se passe. 
"""
# from tkinter import *
# import tkinter as tk
#
#
# class MyApp(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.myContainer1 = Frame()
#         self.myContainer1.pack()
#
#         button_name = "OK"
#         self.button1 = Button(self.myContainer1,
#                               command=self.buttonHandler(button_name, 1, "Bien !"))
#
#         # self.button1.bind("<Return>", self.buttonHandler_a(event, button_name, 1, "Bien 1"))
#         self.button1.configure(text=button_name, background="green")
#         self.button1.pack(side=LEFT)
#         self.button1.focus_force()  # Place le focus du clavier su button1
#
#         button_name = "Cancel"
#
#         self.button2 = Button(self.myContainer1,
#                               command=self.buttonHandler(button_name, 2, "Mal !"))
#
#         # self.button2.bind("<Return>", self.buttonHandler_a(event, button_name, 2, "Mal !"))
#         self.button2.configure(text=button_name, background="red")
#         self.button2.pack(side=LEFT)
#
#     def buttonHandler(self, arg1, arg2, arg3):
#         print("La routine buttonHandler a recu les parametres:", arg1.ljust(8), arg2, arg3)
#
#         def buttonHandler_a(self, event, arg1, arg2, arg3):
#             print("buttonHandler_a received event", event)
#             self.buttonHandler(arg1, arg2, arg3)
#
#
# print("\n" * 100)  # Clear the screen
# print("Starting program tty077")
#
# if __name__ == "__main__":
#     myapp = MyApp()
#     print("Ready to start executing the event loop.")
#     myapp.mainloop()
#     print("Finished exectuing the event loop.")

"""
tt078.py
En regardant l'exécution du programme précédent, nous devons demander : "Que se passe-t-il ici ??!! La routine 
"buttonHandler" est exécutée pour chaque bouton, même avant que la boucle d'évènement ne démarre !!"

La raison est une instruction comme

  self.button1 = Button(self.myContainer1,
       command = self.buttonHandler(button_name, 1, "Good stuff!"))

nous appelons la fonction ButtonHandler, plutôt que demander qu'il soit utilisé en tant que callback. Ce n'est pas ce 
que nous avions prévu de faire, mais c'est ce que nous faisons.

Notez Que -->

 * buttonHandler est un objet fonction, et peut être utilisé en tant que callback binding.

 * buttonHandler() (notez les parenthèses) d'un autre côté est un appel véritable à la fonction "buttonHandler".

Au moment où l'instruction

  self.button1 = Button(self.myContainer1,
       command = self.buttonHandler(button_name, 1, "Good stuff!"))

est exécutée, elle est en train de faire un appel à la routine "buttonHandler". La routine buttonHandler s'exécute, 
affiche son message, et renvoie les résultats de l'appel (dans ce cas, l'objet None). Puis l'option "command" du bouton 
est liée aux résultats de l'appel. En résumé, la commande est liée à l'objet "None". Et c'est pourquoi, quand vous 
clickez sur n'importe lequel des boutons, rien ne se passe.

Il y a-t-il une solution ?

Donc... quelle est la solution ? Il y a-t-il une façon de paramétrer, et re-utiliser, une fonction gestionnaire 
d'évènement ?

Oui. Il existe deux manières connues pour faire cela. L'une utilise la fonction intégrée "lambda" de Python, et l'autre 
utilise une technique appelée "currying".

Dans ce programme nous verrons comment travailler avec lambda, et dans le programme suivant nous étudierons le currying.

Je ne vais pas essayer d'expliquer comment fonctionnent lambda et currying -- cela est trop compliqué et loin de notre 
objectif, qui est de faire fontionner des programmes en Tkinter. Donc je vais simplement les traiter comme des boîtes 
noires. Je ne parlerai pas de la manière dont ils fonctionnent -- je parlerai seulement de la manière de travailler avec
 eux.

Donc étudions lambda.

Command Binding

Au départ, nous pensions que l'instruction suivant fonctionnerait :

  self.button1 = Button(self.myContainer1,
  	command = self.buttonHandler(button_name, 1, "Bien !")
  	)

... et nous avons découvert que cela ne fonctionnait pas comme cela devrait.

La façon de faire ce que nous voulons est de re-écrire l'instruction de cette manière :

  self.button1 = Button(self.myContainer1,
       command = lambda
       arg1=button_name, arg2=1, arg3="Good stuff!" :
       self.buttonHandler(arg1, arg2, arg3)
       )

Event Binding

Heureusement, lambda nous fournit également une manière de paramétrer l'event binding. Au lieu de :

     self.button1.bind("",
     	self.buttonHandler_a(event, button_name, 1, "Bien !"))

(qui ne marcherait pas, parce qu'il n'y a pas de manière d'inclure le paramètre event dans la liste des paramètres), 
nous pouvons utiliser lambda, de cette manière :

		# event binding -- passer l'évènement en tant que paramètre
		self.button1.bind("",
			lambda
			event, arg1=button_name, arg2=1, arg3="Bien !" :
			self.buttonHandler_a(event, arg1, arg2, arg3)
			)

[Notez que "event" est ici un nom de variable-- ce n'est pas un mot-clé Python ou quelque chose comme ça. Cet exemple 
utilise le nom "event" pour le paramètre event, mais des discussions de cette technique utilisent le nom "e" pour le 
paramètre event, et nous aurions pu aussi bien l'appeler "event_arg" si nous avions voulu.]

Une des chouettes fonctionnalités liées à l'utilisation de lambda est que nous pouvons (si nous le souhaitons), 
simplement ne pas passer le paramètre event. Si nous ne passons pas le paramètre event, alors nous pouvons appeler 
directement la fonction self.buttonHandler, au lieu de le faire indirectement à travers la fonction 
self.buttonHandler_a.

Pour illustrer cette technique, nous allons coder l'event binding pour button2 de manière différente de ce que nous 
avons fait pour button1. Voici ce que nous faisons avec button2:

		# event binding -- sans passer l'évènement en tant que paramètre
		self.button2.bind("",
			lambda
			event, arg1=button_name, arg2=2, arg3="Mal !" :
			self.buttonHandler(arg1, arg2, arg3)
			)

Comportement Du Programme

Si vous lancez ce programme, il se comportera comme nous le souhaitons.

Notez que vous pouvez changer le focus du clavier du bouton OK au bouton CANCEL, et revenir au bouton OK, en appuyant 
sur la touche TAB du clavier.

En particulier, vous devriez essayer en appelant le bouton OK en appuyant sur la touche <Return> du clavier. Si vous 
appelez le bouton OK en appuyant sur la touche <Return>, vous allez passer dans la fonction buttonHandler_a, et vous 
aurez un message de cette fonction, qui affichera l'information à propos de l'évènement qui lui a été passé.

Dans tous les cas, si vous clickez sur un button widget avec la souris, ou si vous appelez un widget via un appui sur la
 touche <Return> du clavier, il affichera joliment les paramètres passés à la fonction buttonHandler. 
"""

# from tkinter import *
# import tkinter as tk
#
#
# class MyApp(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.mycontainer1 = Frame()
#         self.mycontainer1.pack()
#
#         # --------------- BUTTON #1 --------------------------
#         button_name = "OK"
#
#         # command binding
#         self.button1 = Button(self.mycontainer1,
#                               command=lambda
#                                   arg1=button_name, arg2=1, arg3="Bien !":
#                               self.buttonHandler(arg1, arg2, arg3))
#
#         # event binding -- passage de l'evenement en tant que parametre
#         self.button1.bind("<Return>",
#                           lambda
#                               event, arg1=button_name, arg2=1, arg3="Bien !":
#                           self.buttonHandler_a(event, arg1, arg2, arg3))
#
#         self.button1.configure(text=button_name, background="green")
#         self.button1.pack(side=LEFT)
#         self.button1.focus_force()  # Place le focus du clavier sur button1
#
#         # --------------- BUTTON #2 --------------------------
#         button_name = "Cancel"
#
#         # command binding
#         self.button2 = Button(self.mycontainer1,
#                               command=lambda
#                                   arg1=button_name, arg2=2, arg3="Mal !":
#                               self.buttonHandler(arg1, arg2, arg3))
#
#         # event binding -- sans passer l'evenement en tant que parametre
#         self.button2.bind("<Return>",
#                           lambda
#                               event, arg1=button_name, arg2=2, arg3="Mal !":
#                           self.buttonHandler(arg1, arg2, arg3))
#
#         self.button2.configure(text=button_name, background="red")
#         self.button2.pack(side=LEFT)
#
#     def buttonHandler(self, argument1, argument2, argument3):
#         print("La routine buttonHandler a recu les prametres:"
#               , argument1.ljust(8), argument2, argument3)
#
#     def buttonHandler_a(self, event, argument1, argument2, argument3):
#         print("buttonHandler_a a recu l'evenement ", event,
#               self.buttonHandler(argument1, argument2, argument3))
#
#
# print("\n" * 100)  # nettoyage de l'ecran
# print("Demarrage du programme tt078.")
#
# if __name__ == "__main__":
#     myapp = MyApp()
#     print("Pret à commencer l'execution de l'event loop.")
#     myapp.mainloop()
#     print("Fini d'executer l'event loop.")

"""
tt079.py
Dans le programme précédent, nous avons étudié une technique utilisant lambda pour passer des paramètres à une fonction 
de gestionnaire d'évènement. Dans ce programme, nous étudierons une technique différente, appelée "currying".

A propos de Curry

Dans son sens le plus simple, currying est une technique pour utiliser une fonction pour construire d'autres fonctions.

Currying est une technique empruntée à la programmation fonctionnelle. Si vous voulez approfondir currying, il y a 
plusieurs recettes disponibles dans le "PythonCookbook":

	http://aspn.activestate.com/ASPN/Python/Cookbook/

La classe curry utilisée dans ce programme vient de la recette de Scott David Daniels "curry -- associating parameters 
with a function", disponible à http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/52549

Comme pour notre discussion de lambda, je ne vais pas essayer d'expliquer comment currying fonctionne. Je vais 
simplement traiter la classe curry comme une boîte noire. Je ne parlerai pas de la manière dont cela fonctionne -- je 
parlerai seulement de la manière de travailler avec.

Curry -- Comment L'Utiliser

La manière d'utiliser curry (la technique) est d'inclure une classe "curry" dans votre programme, ou de l'importer à 
partir du fichier Python. Dans ce programme, nous allons inclure le code curry directement dans le programme.

Au début, nous pensions que l'instruction suivante pouvait lier self.buttonHandler à la command option self.button1, 
mais nous avons vu que cela ne fonctionnait pas comme prévu.

  self.button1 = Button(self.myContainer1,
       command = self.buttonHandler(button_name, 1, "Bien !"))

En utilisant curry, pour faire ce que nous voulons, il faut re-écrire cette instruction ainsi :

  self.button1 = Button(self.myContainer1,
       command = curry(self.buttonHandler, button_name, 1, "Bien !"))

Comme vous pouvez le voir, le code est tout à fait simple. Au lieu d'appeler la fonction self.buttonHandler, nous créons 
un objet curry (c'est à dire, une instance de la classe curry), en passant la fonction self.buttonHandler en tant que 
premier paramètre. Essentiellement, ce qui se passe est que l'objet curry se souvient du nom de la fonction qui lui a 
été donné. Ensuite quand il (l'objet curry) est appelé, il appelle la fonction qui lui a été donnée lors de sa création.

Event Binding

Chad Netzer a imaginé une technique similaire au currying, qui peut être utilisée pour paramétrer l'event binding. [NOTE 
cette technique a besoin de Python 2 ou supérieur.] Elle implique d'utiliser une fonction "event_lambda".

Pour utiliser event_lambda, comme pour curry, vous avez besoin d'inclure le code pour la fonction "event_lambda" dans 
votre programme, ou l'importer à partir de son propre fichier Python. Dans ce programme, nous incluons le code pour la 
fonction event_lambda directement dans notre programme.

	# ---------- code for function: event_lambda --------
	def event_lambda(f, *args, **kwds ):
		"A helper function that wraps lambda in a prettier interface."
		return lambda event, f=f, args=args, kwds=kwds : f( *args, **kwds )

Une fois que la fonction event_lambda function est disponible pour nous, nous pouvons l'utiliser pour lier 
self.buttonHandler à l'évènement clavier <Return>, et lui passer quelques paramètres. Voici comment nous le faisons :

	self.button1.bind("",
		event_lambda( self.buttonHandler, button_name, 1, "Bien !" ) )

Si vous voulez absolument savoir comment event_lambda fonctionne, il est un peu plus facile de voir en regardant le 
codage pour button2.

Pour button2, nous utilisons un mécanisme en deux étapes. D'abord nous appelons la fonction event_lambda.

	event_handler = event_lambda( self.buttonHandler, button_name, 2, "Mal !" )

Quand la fonction event_lambda est appelée, elle utilise lambda pour créer une nouveau, non nommé, objet fonction 
("anonymous").

		lambda event, f=f, args=args, kwds=kwds : f( *args, **kwds )

La fonction objet non-nommé est un wrapper pour la fonction que nous voulons réellement appeler ("f", qui dans ce 
programme est "self.buttonHandler") et les paramètres que nous indiquons à ce moment sont ceux de l'appel à la 
fonction event_lambda.

Ensuite, la fonction event_lambda renvoie cette nouvelle fonction anonyme.

Quand event_lambda renvoie la fonction anonyme, nous lui donnons un nom : "event_handler".

	event_handler = event_lambda( self.buttonHandler, button_name, 2, "Mal !" )

Puis, dans la deuxième étape, nous lions l'évènement <Return> à la fonction "event_handler".

	self.button2.bind("", event_handler )

Notez que pour la fonction anonyme, 'event' est juste un paramètre fictif jamais utilisé et dont on se débarasse. 
Seulement les paramètres positionnels (args) et les paramètres arbitraires (kwds) sont passés à la routine 
button-handler.

Wow! Je viens de griller des neurones !!

Cela est piégeux. mais ne croyez pas que vous avez besoin de brûler des neurones pour arriver à comprendre comment cela 
fonctionne. Vous n'avez pas besoin de savoir COMMENT "curry" et "event_lambda" fonctionnent pour arriver à les utiliser. 
Traitez les juste comme des boîtes noires... utilisez-les juste et ne vous souciez pas de comment cela fonctionne.

Lambda Contre Curry Et Event_lambda -- Lequel utiliser ?

Hum...

 * Le code pour appeler curry et event_lambda est assez intuitif, court et simple.
   L'inconvénient est que les utiliser implique de les inclure dans le code de votre 
   programme, ou les importer.

 * Lambda, au contraire, est inclus dans le langage Python -- vous n'avez rien de spécial à faire pour 
   l'importer; il est juste ici.
   l'inconvénient est que le code pour l'utiliser peut être long et un peu déroutant.

Donc vous avez le choix. "You pays yer money and takes yer choice," comme on dit. Utilisez celui avec lequel vous êtes 
le plus à l'aise ,et/ou qui vous semble le plus adapté à cette tâche.

La VERITABLE morale de l'histoire est...

Python est un langage puissant, et il fournit de nombreux outils qui peuvent être utilisés pour créer des callback 
functions pour gérer les évènements. "Penser en Tkinter" est une introduction aux concepts de base, pas une encyclopédie 
de techniques, donc nous pouvons seulement en explorer quelques unes ici. Mais vous pouvez être confiant, en maîtrisant 
plus Python, et au fur et à mesure que vos besoins de flexibilité augmentent, des fonctionnalités plus avancées de 
Python deviendront disponibles, et vous permettront de créer juste le type de callback function dont vous avez besoin.

Comportement Du Programme

Si vous lancez ce programme, il se comportera exactement comme le précédent. Nous n'avons rien changé dans le 
comportement du programme, juste la manière dont le programme est codé. 
"""

"""
tt080.py
Dans les derniers programmes, nous avons passé beaucoup de temps à discuter des techniques pour lier les gestionnaires 
d'évènements aux widgets.

Avec ce programme, nous revenons à créer l'apparence du GUI -- déclarer les widgets et contrôler leur apparence et 
emplacement.

Trois Techniques Pour Contrôler La Disposition D'Un Gui

Il y a trois techniques pour contrôler la disposition générale d'un GUI.

  * les attributs des widgets
  * les options de pack()
  * les emboîtements de containers (cadres)

Dans ce programme, nous cherchons à contrôler l'apparence en définissant des attributs de widget et des options pack().

Nous allons beaucoup travailler avec les boutons, et le cadre qui les contient. Dans des versions précédentes de ce 
programme, nous avons appelé le cadre "myContainer1". Ici, nous l'avons renommé en quelque chose d'un peu plus 
significatif : "buttons_frame".

Les nombres dans la section suivante font référence aux numéros des commentaires dans le code source.

(1) D'abord, pour être certain que tous nos boutons ont la même largeur , nous indiquons un attribut "width" identique 
pour tous les boutons. Notez que l'attribut "width" est spécifique au widget "Button" de Tkinter -- tous les widgets 
n'ont pas un attribut width. Notez aussi que l'attibut width utilise des unités de caractères (et pas, par exemple, des 
unités en pixels, inches, ou millimètres). Comme notre plus grand label ("Cancel") contient six caractères, nous 
définissons la longueur pour nos boutons à "6". (1)

(2) Ensuite nous ajoutons du remplissage (padding) pour nos boutons. Padding est l'espace en plus autour du texte, entre 
le texte et le bord du bouton. Nous le faisons en donnant une valeur aux attributs "padx" et "pady" attributs des 
boutons. "padx" remplit sur l'axe des X, horizontalement, de la gauche vers la droite. "pady" remplit sur l'axe des Y, 
verticalement, du haut vers le bas.

Nous indiquerons notre remplissage horizontal à 3 millimètres (padx="3m") et notre remplissage vertical à 1 millimètre 
(pady="1m"). Notez que, contrairement à l'attribut "width" (qui était numérique), ces attributs sont entourés de 
quillemets. C'est parce que nous indiquons les unités de padding avec le suffixe "m", donc nous indiquons les longueurs 
de remplissage en tant que chaînes de caractères plutôt qu'en nombres.

(3) Finalement, nous ajoutons du remplissage au container (buttons_frame) qui contient les boutons. Pour le container, 
nous pouvons indiquer quatre attributs de remplissage. "padx" et "pady" indiquent le remplissage autour (en dehors) du 
cadre. "ipadx" et "ipady" ("internal padx" et "internal pady") indiquent le remplissage à l'intérieur. C'est le 
remplissage qui va autour de chacun des widgets qui sont à l'intérieur du container.

Notez que nous n'indiquons pas le remplissage du cadre en tant qu'attribut du cadre, mais comme des options que nous 
passons au packer. (4). Comme vous pouvez le voir, le remplissage est un peu déroutant. Les cadres ont un remplissage 
intérieur, mais les widgets comme des boutons n'en ont pas. Dans certains cas, le remplissage est un attribut du widget, 
alors que dans d'autres cas il est indiqué comme une option à pack().

Comportement Du Programme

Quand vous lancez ce programme, vous verrez deux boutons. Ils devraient être de la même taille. Les côtés des boutons ne 
débordent pas sur le texte. Et les boutons sont entourés par un peu d'espace. 
"""
# from tkinter import *
# import tkinter as tk
#
#
# class MyApp(tk.Tk):
#     def __init__(self):
#         super().__init__()
#
#         # ------ Constantes pour controler la dispoisition ------#
#         button_width = 6  # (1)
#         button_padx = "2m"  # (2)
#         button_pady = "1m"  # (2)
#
#         buttons_frame_padx = "3m"  # (3)
#         buttons_frame_pady = "2m"  # (3)
#         buttons_frame_ipadx = "3m"  # (3)
#         buttons_frame_ipady = "1m"  # (3)
#         # ------ Fin des constantes ------#
#
#         self.buttons_frame = Frame()
#         self.buttons_frame.pack(  # (3)
#             ipadx=buttons_frame_ipadx,  # (3)
#             ipady=buttons_frame_ipady,  # (3)
#             padx=buttons_frame_padx,  # (3)
#             pady=buttons_frame_pady,  # (3)
#         )
#
#         self.button1 = Button(self.buttons_frame, command=self.button1Click)
#         self.button1.configure(text="OK", background="green")
#         self.button1.focus_force()
#         self.button1.configure(
#             width=button_width,  # (1)
#             padx=button_padx,  # (2)
#             pady=button_pady  # (2)
#         )
#
#         self.button1.pack(side=LEFT)
#         self.button1.bind("<Return>", self.button1Click_a)
#
#         self.button2 = Button(self.buttons_frame, command=self.button2Click)
#         self.button2.configure(text="Cancel", background="red")
#         self.button2.configure(
#             width=button_width,  # (1)
#             padx=button_padx,  # (2)
#             pady=button_pady  # (2)
#         )
#
#         self.button2.pack(side=RIGHT)
#         self.button2.bind("<Return>", self.button2Click_a)
#
#     def button1Click(self):
#         if self.button1["background"] == "green":
#             self.button1["background"] = "yellow"
#
#         else:
#             self.button1["background"] = "green"
#
#     def button2Click(self):
#         self.destroy()
#
#     def button1Click_a(self, event):
#         self.button1Click()
#
#     def button2Click_a(self, event):
#         self.button2Click()
#
#
# if __name__ == "__main__":
#     myapp = MyApp()
#     print("Pret à commencer l'execution de l'event loop.")
#     myapp.mainloop()
#     print("Fin de l'execution de l'event loop")

"""
tt090.py
Dans ce programme, nous étudions l'emboîtement de containers (cadres). Nous allons créer une série de cadres, emboîtés 
les uns dans les autres: bottom_frame, left_frame, et big_frame.

Ces cadres ne contiendront rien -- pas de widget. Normalement, comme les cadres sont élastiques, cela se réduirait à 
rien. mais nous indiquons les attributs "height" et "width" pour indiquer une taille initiale pour ces attributs.

Notez que nous n'indiquons pas de hauteurs ou largeurs pour tous les cadres. Pour myContainer1, par exemple, nous n'en 
indiquons pas. Mais nous indiquons heights et widths pour ses descendants, et il va s'étirer pour s'adapter aux hauteurs 
et largeurs cumulées de ses descendants.

Dans un programme ultérieur, nous verrons comment placer des widgets dans ces cadres, mais dans ce programme nous allons 
simplement créer les cadres, et leur donner différentes tailles, positions et couleurs d'arrière-plan.

Nous mettons aussi une frontière striée autour des trois cadres qui nous intéresseront le plus : bottom_frame, 
left_frame, et right_frame. Les autres cadres (par exemple top_frame et buttons_frame) n'ont pas de bordure.

Comportement Du Programme

Quand vous lancez ce programme, vous verrez les différents cadres, avec des couleurs d'arrière-plan différentes. 
"""
# from tkinter import *
# import tkinter as tk
#
#
# class MyApp(tk.Tk):
#     def __init__(self):
#         super().__init__()
#
#         #  Our topmost frame is called myContainer1
#         self.myContainer1 = Frame()
#         self.myContainer1.pack()
#
#         # --------- Constants for controlling layout ---------#
#         button_width = 6  # (1)
#
#         button_padx = "2m"  # (2)
#         button_pady = "1m"  # (2)
#
#         buttons_frame_padx = "3m"  # (3)
#         buttons_frame_pady = "2m"  # (3)
#         buttons_frame_ipadx = "3m"  # (3)
#         buttons_frame_ipady = "1m"  # (3)
#         # --------- End Constants ---------#
#
#         # Nous utilliserons l'orientation VERTICALE (top/bottom) à l'intereieur de myContainer1.
#         # À l'interieur de myContainer1, nous creons d'abord button_frame.
#         # Puis nous creons top_frame et bottom_frame.
#         # Ils seront nos cadres de demonstration.
#
#         # buttons frame
#         self.buttons_frame = Frame(self.myContainer1)
#         self.buttons_frame.pack(
#             side=TOP,
#             ipadx=buttons_frame_ipadx,
#             ipady=buttons_frame_ipady,
#             padx=buttons_frame_padx,
#             pady=buttons_frame_pady,
#         )
#
#         # top frame
#         self.top_frame = Frame(self.myContainer1)
#         self.top_frame.pack(
#             side=TOP,
#             fill=BOTH,
#             expand=YES
#         )
#
#         # bottom frame
#         self.bottom_frame = Frame(self.myContainer1,
#                                   borderwidth=5,
#                                   relief=RIDGE,
#                                   height=50,
#                                   background="white",
#                                   )
#         self.bottom_frame.pack(side=TOP,
#                                fill=BOTH,
#                                expand=YES
#                                )
#
#         # Nous placons maintenant 2 autres cadres, left_frame et right_frame,
#         # à l'interieur de top frame. Nous utiliserons l'orientation HORIZONTALE (left/right)
#         # à l'interieur de top_frame.
#
#         # left_frame
#         self.left_frame = Frame(self.top_frame, background="red",
#                                 borderwidth=5, relief=RIDGE,
#                                 height=250,
#                                 width=50
#                                 )
#         self.left_frame.pack(side=LEFT,
#                              fill=BOTH,
#                              expand=YES
#                              )
#
#         # right frame
#         self.right_frame = Frame(self.top_frame, background="tan",
#                                  borderwidth=5, relief=RIDGE,
#                                  width=250)
#         self.right_frame.pack(side=RIGHT,
#                               fill=BOTH,
#                               expand=YES)
#
#         # Maintant nous ajoutons des bouttons à buttons_frame
#         self.button1 = Button(self.buttons_frame, command=self.button1Click)
#         self.button1.configure(text="OK", background="green")
#         self.button1.focus_force()
#         self.button1.configure(
#             width=button_width,  # (1)
#             padx=button_padx,  # (2)
#             pady=button_pady  # (2)
#         )
#
#         self.button1.pack(side=LEFT)
#         self.button1.bind("<Return>", self.button1Click_a)
#
#         self.button2 = Button(self.buttons_frame, command=self.button2Click)
#         self.button2.configure(text="Cancel", background="red")
#         self.button2.configure(
#             width=button_width,  # (1)
#             padx=button_padx,  # (2)
#             pady=button_pady  # (2)
#         )
#
#         self.button2.pack(side=RIGHT)
#         self.button2.bind("<Return>", self.button2Click_a)
#
#     def button1Click(self):
#         if self.button1["background"] == "green":
#             self.button1["background"] = "yellow"
#         else:
#             self.button1["background"] = "green"
#
#     def button2Click(self):
#         self.destroy()
#
#     def button1Click_a(self, event):
#         self.button1Click()
#
#     def button2Click_a(self, event):
#         self.button2Click()
#
#
# if __name__ == "__main__":
#     myapp = MyApp()
#     myapp.mainloop()

"""
tt095.py
Contrôler la taille des fenêtres peut être une expérience frustrante quand on travaille avec Tkinter. Imaginez cette 
situation. Vous pratiquez le développement itératif, donc vous dessinez prudemment un cadre en indiquant une hauteur et 
une largeur. Vous testez et cela fonctionne. Puis vous passez à l'étape suivante, et vous ajoutez des boutons au cadre. 
Vous testez à nouveau, et à votre grande surprise, Tkinter agit comme si vous n'aviez pas indiqué "height" et "width" 
pour le cadre, qui s'est cassé pour à peine ranger les boutons.

Que se passe-t-il ???!!!

Et bien, le comportement du packer est incohérent. Ou, nous pouvons dire : il dépend de nombreux facteurs de situation. 
Le packer va tenir compte de la taille d'un container si ce container est vide, mais si ce container contient d'autres 
widgets, alors la nature élastique du container se met en évidence -- les valeurs pour "height" et "width" pour le 
container sont ignorées, et la taille du container est ajustée pour contenir les widgets d'aussi près que possible.

Donc, vous ne pouvez pas vraiment contrôler la taille d'un container qui contient des widgets.

Ce que vous POUVEZ contrôler est la taille de départ de la fenêtre root entière, et vous le faites avec l'option 
"geometry" du Window Manager.

(1)

Dans ce programme, nous utilisons l'option geometry pour créer une jolie grande fenêtre autour de notre plus petit 
cadre.

(2) Notez que l'option "title",que nous utilisons aussi dans ce programme, est aussi une méthode du Window Manager. 
"Title" contrôle le texte du titre de la barre de titre de la fenêtre.

Notez aussi que les options du Window Manager peuvent de manière optionelle être indiquées avec un préfixe "wm_", par 
exemple "wm_geometry" et "wm_title". Dans ce programme, juste pour montrer que cela peut se faire de différentes 
manières, nous utilisons "geometry" et "wm_title".

Comportement Du Programme

Ce programme affiche quatre fenêtres successivement.

Notez qu'il vous faudra fermer chaque fenêtre en clickant sur le widget "close" -- le "X" dans une boîte en haut à 
droite de la barre de titre.

Dans le cas 1, nous voyons à quoi ressemble un cadre, quand height et width sont indiquées, et -- NOTEZ -- il ne 
contient pas de widget.

Dans le cas 2, nous voyons à quoi ressemble le même cadre quand des widgets (dans notre cas, trois boutons) y sont 
ajoutés. Notez que la trame a entassé les trois boutons de manière serrée.

Dans le cas 3, nous voyons à nouveau à quoi ressemble un cadre vide, mais cette fois nous utilisons l'option geometry 
pour contrôler la taille de la fenêtre en tant qu'ensemble. Nous pouvons voir l'arrière-plan bleu du cadre à l'intérieur
 du gris de la fenêtre.

Dans le case 4, nous voyons à nouveau le cadre avec trois boutons à l'intérieur, mais cette fois nous avons indiqué la 
taille du cadre avec l'option geometry. Notez que la taille de la fenêtre est la même que dans le Cas 3, mais (comme 
dans le Cas 2) le cadre s'est cassé autour des boutons, et nousne pouvons pas voir du tout l'arrière-plan bleu. 
"""

# from tkinter import *
# import tkinter as tk
#
#
# class App:
#     def __init__(self, root, use_geometry, show_buttons):
#         fm = Frame(root, width=300, height=200, bg="blue")
#         fm.pack(side=TOP, expand=NO, fill=NONE)
#
#         if use_geometry:
#             root.geometry("600x400")  # (1) Notez la methode du geometry Windows Manager
#
#         if show_buttons:
#             Button(fm, text="Button 1", width=10).pack(side=LEFT)
#             Button(fm, text="Button 2", width=10).pack(side=LEFT)
#             Button(fm, text="Button 3", width=10).pack(side=LEFT)
#
#
# case = 0
# for use_geometry in (0, 1):
#     for show_buttons in (0, 1):
#         case = case + 1
#         root = Tk()
#         root.wm_title("Case" + "-" + str(case) + "  " + "Geometry" + " - " + str(use_geometry))  # (2) Notez la methode du wm_title Window Manager
#         display = App(root, use_geometry, show_buttons)
#         root.mainloop()

"""
tt100.py
Dans ce programme, nous voyons plusieurs options de pack() pour contrôler la disposition à l'intérieur d'un cadre :

  * side
  * fill
  * expand
  * anchor

Ce programme est différent des autres programmes dans cette série. Vous n'avez pas besoin de lire le code source pour 
comprendre comment code une fonctionnalité. Vous avez besoin de LANCER le programme.

Le but de ce programme est de vous montrer les résultats des options de pack. Lancer ce programme vous permettra de 
positionner différentes options de pack et de constater les résultats des différentes combinaisons d'options.

Les Concepts Sous-Jacents Aux Options De Pack

Pour comprendre comment nous pouvons contrôler l'apparence des widgets à l'intérieur d'un container (c'est-à-dire, avec 
un cadre), il faut nous rappeler que le pack geometry manager utilise un ""cavity" model of arrangement". Chaque 
container contient une cavity, et nous plaçons des esclaves à l'intérieur du container.

En parlant à propos du positionnement et de l'affichage de components à l'intérieur d'un container, il est utile d'avoir 
à l'esprit trois concepts :

 * espace non réclamé (c'est-à-dire, la cavity)
 * espace réclamé, mais non utilisé
 * espace réclamé et utilisé

Quand vous placez un widget, comme un bouton, il est toujours placé le long d'un des quatres côtés de la cavity. 
L'option pack "side" indique quel côté utiliser. Par exemple, si nous indiquons "side=LEFT", alors le widget sera placé 
(c'est-à-dire positionné) sur le côté gauche de la cavity.

Quand un widget est placé le long d'un côté, il réclame le côté entier, bien qu'il n'utilise pas tout l'espace qu'il 
réclame. Supposons que nous plaçons un petit bouton appelé X le long du côté gauche d'une large cavity, comme dans le 
diagramme suivant.

             -------------------
    réclamé mais  |   |             |
    inutilisé---> |   |   cavity    |
                  |   | (non        |
                  |___| réclamé )   |
    réclamé et    |   |             |
    utilisé-----> | X |             |
                  |___|             |
                  |   |             |
    réclamé mais  |   |             |
    inutilisé---> |   |             |
                  |   |             |
                  -------------------

La cavity (l'espace non réclamé) est maintenant à la droite du widget. Le widget X réclame la totalité du côté gauche, 
dans une bande qui est assez large pour le contenir. Mais parce que le widget X est petit, il utilise actuellement 
seulement une petite partie de cette aire qu'il réclame. C'est la partie qu'il utilise pour s'afficher lui-même.

Comme vous pouvez le voir, le widget X a revendiqué juste l'espace dont il a besoin pour s'afficher lui-même. Si nous 
précisons l'option "expand=YES" de pack, il va réclamer TOUTE l'aire disponible. Aucune partie de la cavity ne sera pas 
réclamée. Notez que cela ne veut pas dire que le le widget X va *utiliser* toute l'aire. Il va continuer à n'utiliser 
que la petite partie dont il a besoin.

Si un widget a réclamé plus d'espace qu'il n'en utilise, il a deux choix :

 * il peut se déplacer dans l'espace non réclamé, ou
 * il peut grandir pour remplir l'espace non réclamé.

Si nous voulons qu'en grandissant il utilise l'espace non réclamé, nous pouvons utiliser l'option "fill", qui indique à 
un widget si il a le droit de grandir en remplissant l'espace non utilisé, et dans quelle direction il peut grandir.

  * "fill=NONE" il ne peut pas grandir.
  * "fill=X" il peut grandir le long de l'axe des X (horizontalement).
  * "fill=Y" il peut grandir le long de l'axe des Y (verticalement).
  * "fill=BOTH" il peut grandir à la fois horizontalement et verticalement.

Si nous voulons que, quand il grandisse, il se déplace autour de l'espace non réclamé,alors nous pouvons utiliser 
l'option "anchor",qui dit au widget où se placer dans l'espace qu'il réclame. Les valeurs de l'option anchor (ancre en 
français) sont comme la direction d'une boussole. "N" pour "nord" (c'est-à-dire centré en haut de l'aire réclamée). "NE"
 pour "nord est" (c'est-à-dire en haut à droite de l'aire réclamée), "CENTER" pour centrée dans le milieu de l'aire 
 réclamée. Et ainsi de suite.

Exécution Du Programme

Donc maintenant, lancez le programme. Vous n'avez pas besoin de lire le code. Lancez juste le programme et testez avec 
les différentes options de pack pour les trois boutons de démo.

Le cadre du Bouton A lui donne une cavité horizontale pour se déplacer -- le cadre n'est pas plus grand que le bouton.

La cavity du Bouton B lui donne une cavity verticale pour se déplacer -- le cadre n'est pas plus large que le bouton.

Et le cadre du bouton C lui donne une grande cavity -- plus large et haute que le bouton lui-même - pour se déplacer.

²Si l'apparence d'un des boutons pour certaines valeurs vous surprend, essayez de comprendre le pourquoi le bouton de 
cette apparence.

Et finalement....

Une Astuce Utile Pour Le Debugging

Notez que le packing est quelque chose de compliqué, parce que le positionnement d'un widget par rapport aux autres 
widgets placés avant dépend en partie de la façon dont les autres widgets ont été placés.

Voici une astuce utile pour le debugging. Si vous développez une disposition et rencontrez un problème, -- les choses 
ne se passent pas comme prévu -- alors donnez à chacun de vos containers (c'est-à-dire, chacun des cadres) une couleur 
d'arrière-plan différente, par exemple:

      bg="red"

ou

      bg="cyan"

ou

      bg="tan"

... ou yellow, ou blue, ou red, et ainsi de suite. 
"""
from tkinter import *
import tkinter as tk


class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        # ----- Constantes pour contoler la disposition des boutons -----
        button_width = 6
        button_padx = "2m"

        button_pady = "1m"
        buttons_frame_padx = "3m"
        buttons_frame_pady = "2m"
        buttons_frame_ipadx = "3m"
        buttons_frame_ipady = "1m"

        # ----- Fin des constantes -----

        # definition des variables Tkinter, qui seront controles par les boutons radios
        self.button_name = StringVar()
        self.button_name.set("C")

        self.side_option = StringVar()
        self.side_option.set(LEFT)

        self.fill_option = StringVar()
        self.fill_option.set(NONE)

        self.expand_option = StringVar()
        self.expand_option.set(YES)

        self.anchor_option = StringVar()
        self.anchor_option.set(CENTER)

        # ----- Fin des constantes -----

        self.geometry("640x400")

        ### Notre cadre le plus haut est appele myContainer1
        self.myContainer1 = Frame()
        self.myContainer1.pack(expand=YES, fill=BOTH)

        ### Nous utilisons l'orientation HORIZONTALE (guauche/droite) à l'interieur de myContainer1.
        ### A l'interieur de myContainer1, nous creons control_frame et demo_frame.

        # control frame - pratiquement tout sauf le cadre demo
        self.control_frame = Frame(self.myContainer1)
        self.control_frame.pack(side=LEFT, expand=NO, padx=10, pady=5, ipadx=5, ipady=5)

        # A l.interieur de control_frame nous creons un header label
        # et un buttons_frame en haut,
        # et demo_frame en bas

        myMessage = "Cette fenetre montre les effets des options de packing \nexpand, fill, et anchor.\n"
        Label(self.control_frame, text=myMessage, justify=LEFT).pack(side=TOP, anchor=W)

        # Les boutons du cadre
        self.buttons_frame = Frame(self.control_frame)
        self.buttons_frame.pack(side=TOP, expand=NO, fill=Y, ipadx=5, ipady=5)

        # Le cadre demo
        self.demo_frame = Frame(self.myContainer1)
        self.demo_frame.pack(side=RIGHT, expand=YES, fill=BOTH)

        ### A l'interieur du cadre demo, nous creons top_frame et bottom_frame.
        ### Ils seront nos cadres de demonstration.
        # top frame
        self.top_frame = Frame(self.demo_frame)
        self.top_frame.pack(side=TOP, expand=YES, fill=BOTH)

        # button frame
        self.bottom_frame = Frame(self.demo_frame, borderwidth=5, relief=RIDGE,
                                  height=50, bg="cyan", )
        self.bottom_frame.pack(side=TOP, fill=X)

        ### Maintennant nous allons placer 2 autres cadres, left_frame and right_frame,
        ### à l'interieur de top frame. Nous allons utiliser l'orientation HORIZONTALE (guauche/droite)
        ### à l'interieur de top_frame.

        # left_frame
        self.left_frame = Frame(self.top_frame, background="red", borderwidth=5, relief=RIDGE, width=50, )
        self.left_frame.pack(side=LEFT, expand=NO, fill=Y)

        ### right_frame
        self.right_frame = Frame(self.top_frame, background="tan", borderwidth=5, relief=RIDGE, width=250)
        self.right_frame.pack(side=RIGHT, expand=YES, fill=BOTH)

        # Nous inserons maintenant un bouton dans chacun des cadres interessants.
        button_names = ["A", "B", "C"]
        side_options = [LEFT, TOP, RIGHT, BOTTOM]
        fill_options = [X, Y, BOTH, NONE]
        expand_options = [YES, NO]
        anchor_options = [NW, N, NE, E, SE, S, SW, W, CENTER]

        self.buttonA = Button(self.bottom_frame, text="A")
        self.buttonA.pack()
        self.buttonB = Button(self.left_frame, text="B")
        self.buttonB.pack()
        self.buttonC = Button(self.right_frame, text="C")
        self.buttonC.pack()
        self.button_with_name = {"A": self.buttonA, "B": self.buttonB, "C": self.buttonC}

        # now we some subframes to the buttons_frame
        self.button_names_frame = Frame(self.buttons_frame, borderwidth=5)
        self.side_options_frame = Frame(self.buttons_frame, borderwidth=5)
        self.fill_options_frame = Frame(self.buttons_frame, borderwidth=5)
        self.expand_options_frame = Frame(self.buttons_frame, borderwidth=5)
        self.anchor_options_frame = Frame(self.buttons_frame, borderwidth=5)

        self.button_names_frame.pack(side=LEFT, expand=YES, fill=Y, anchor=N)
        self.side_options_frame.pack(side=LEFT, expand=YES, anchor=N)
        self.fill_options_frame.pack(side=LEFT, expand=YES, anchor=N)
        self.expand_options_frame.pack(side=LEFT, expand=YES, anchor=N)
        self.anchor_options_frame.pack(side=LEFT, expand=YES, anchor=N)

        Label(self.button_names_frame, text="\nButton").pack()
        Label(self.side_options_frame, text="Side\nOption").pack()
        Label(self.fill_options_frame, text="Fill\nOption").pack()
        Label(self.expand_options_frame, text="Expand\nOption").pack()
        Label(self.anchor_options_frame, text="Anchor\nOption").pack()

        for option in button_names:
            button = Radiobutton(self.button_names_frame, text=str(option), indicatoron=1,
                                 value=option, command=self.button_refresh, variable=self.button_name)
            button['width'] = button_width
            button.pack(side=TOP)

        for option in side_options:
            button = Radiobutton(self.side_options_frame, text=str(option), indicatoron=0,
                                 value=option, command=self.demo_update, variable=self.side_option)
            button["width"] = button_width
            button.pack(side=TOP)

        for option in fill_options:
            button = Radiobutton(self.fill_options_frame, text=str(option), indicatoron=0,
                                 value=option, command=self.demo_update, variable=self.fill_option)
            button["width"] = button_width
            button.pack(side=TOP)

        for option in expand_options:
            button = Radiobutton(self.expand_options_frame, text=str(option), indicatoron=0,
                                 value=option, command=self.demo_update, variable=self.expand_option)
            button["width"] = button_width
            button.pack(side=TOP)

        for option in anchor_options:
            button = Radiobutton(self.anchor_options_frame, text=str(option), indicatoron=0,
                                 value=option, command=self.demo_update, variable=self.anchor_option)
            button["width"] = button_width
            button.pack(side=TOP)

        self.cancelButtonFrame = Frame(self.button_names_frame)
        self.cancelButtonFrame.pack(side=BOTTOM, expand=YES, anchor=SW)

        self.cancelButton = Button(self.cancelButtonFrame,
                                   text="Cancel", background="red",
                                   width=button_width,
                                   padx=button_padx,
                                   pady=button_pady
                                   )
        self.cancelButton.pack(side=BOTTOM, anchor=S)

        self.cancelButton.bind("<Button-1>", self.cancelButtonClick)
        self.cancelButton.bind("<Return>", self.cancelButtonClick)

        # Nous placons les boutons dans leur position de depart.
        self.demo_update()

    def button_refresh(self):
        button = self.button_with_name[self.button_name.get()]
        properties = button.pack_info()
        self.fill_option.set(properties["fill"])
        self.side_option.set(properties["side"])
        self.expand_option.set(properties["expand"])
        self.anchor_option.set(properties["anchor"])

    def demo_update(self):
        button = self.button_with_name[self.button_name.get()]
        button.pack(fill=self.fill_option.get()
                    , side=self.side_option.get()
                    , expand=self.expand_option.get()
                    , anchor=self.anchor_option.get()
                    )

    def cancelButtonClick(self, event):
        self.destroy()


if __name__ == "__main__":
    myapp = MyApp()
    myapp.mainloop()
